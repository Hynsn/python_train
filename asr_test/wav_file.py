# from pydub import AudioSegment
#
# audio_file = AudioSegment.from_file("9285273522331150.wav", format="wav")
# sample_rate = audio_file.frame_rate
#
# print(f"采样率: {sample_rate} Hz")
import os

# import wave
#
# # 打开WAV文件
# with wave.open('9285273522331150.wav', 'rb') as wav_file:
#     # 获取WAV文件的采样率
#     sample_rate = wav_file.getframerate()
#     print(f"采样率: {sample_rate} Hz")

from pydub import AudioSegment

# 加载WAV文件
sound = AudioSegment.from_file("100511566475978219.wav", format="wav")
# 转换为单声道
print(sound.sample_width)
print(sound.frame_width)
print(sound.channels)
mono_sound = sound.set_sample_width(2)
path_to_create = 'train'
if not os.path.exists(path_to_create):
    # 路径不存在，创建路径
    os.makedirs(path_to_create)
    print(f"路径 '{path_to_create}' 已创建。")
else:
    # 路径已存在
    print(f"路径 '{path_to_create}' 已存在。")
# 保存为单声道WAV文件
mono_sound.export("{}/output1.wav".format(path_to_create), format="wav")
