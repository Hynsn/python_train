# -*- coding: UTF-8 -*-

import os
import re

import pandas
from datasets import load_dataset
from playsound import playsound
import wave
import playsound
import pyaudio
import wave
import sys
import pygame
import wave
from jiwer import wer

from pydub import AudioSegment


# def play_file(p, name: str):
#     wf = wave.open(name, 'r')
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#     data = wf.readframes(chunk)
#     while len(data) > 0:
#         stream.write(data)
#         data = wf.readframes(chunk)
#     stream.stop_stream()
#     stream.close()
#     chunk = 1024
#     p = pyaudio.PyAudio()
#     pygame.mixer.init()
# pygame.mixer.music.load(new_path)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.wait(100)
# play_file(p, new_path)
# p.terminate()
def dataset_to_excel(export: bool):
    out_path = 'train'
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    else:
        print(f"路径 '{out_path}' 已存在。")
    fleurs_asr = load_dataset("google/fleurs", "en_us", split="train")
    print("{},{}".format(fleurs_asr, fleurs_asr.num_rows))
    iters = fleurs_asr.to_iterable_dataset()
    file_list = []
    reference_list = []

    # 清除特殊字符
    chars_to_remove = ['\"', ',']
    regex_pattern = '[' + ''.join(chars_to_remove) + ']'
    for item in iters:

        path = os.path.normpath(item['path'])
        end = path.rindex("\\")
        name = item['audio']['path'].replace('/', '\\')
        new_path = "{}\\{}".format(path[0:end], name)
        # print("{},sample={}".format(new_path, item['num_samples']))
        if os.path.exists(new_path):
            # print(new_path)
            audio_path = item['audio']['path']
            print(audio_path)
            if export:
                sound = AudioSegment.from_file(new_path, format="wav")
                # 转换为单声道
                mono_sound = sound.set_sample_width(2)
                mono_sound.export(audio_path, format="wav")

            # 使用正则表达式去除字符
            clean_text = re.sub(regex_pattern, '', item['transcription'])
            file_list.append(item['audio']['path'])
            reference_list.append(clean_text)
            # print("{},{}".format(item['path'], item['transcription']).encode("utf-8"))

    df = pandas.DataFrame(data={'path': file_list, 'reference': reference_list})
    df.to_csv('{}/fleurs_dataset.csv'.format(out_path), index=False)
    print(df)


def get_wer(option: str, file: str, filter: bool = False):
    data = pandas.read_csv(r"{}".format(file), encoding='utf-8')
    # data["hypothesis_clean"] = [normalizer(text) for text in data["hypothesis"]]
    # data["reference_clean"] = [normalizer(text) for text in data["reference"]]
    reference = []
    hypothesis = []
    filter_counter = 0
    for index, row in data.iterrows():
        error = wer(row['reference'], row['hypothesis'])
        if error >= 1.0:
            filter_counter += 1
            if filter:
                # print(f"{row['path']},\n{row['reference']} \n{row['hypothesis']}")
                # print(f"过滤 第{index}条 WER: {error * 100:.2f} %")
                pass
            pass
        else:
            reference.append(row['reference'])
            hypothesis.append(row['hypothesis'])

    if filter:
        error1 = wer(reference, hypothesis)
        print(f"{option}过滤了{filter_counter}条,最终的WER: {error1 * 100:.2f} %")
    else:
        error = wer(list(data['reference']), list(data['hypothesis']))
        print(f"{option}最终的WER: {error * 100:.2f} %")


if __name__ == '__main__':
    # dataset_to_excel(False)
    get_wer('ios_native', 'native_iOS_out.csv')
    get_wer('k2-fsa', 'new_out_S10E.csv')
    get_wer('android_whisper', 'new_out_whisper.csv')
