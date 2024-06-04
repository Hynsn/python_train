# coding:utf-8

from datasets import load_dataset

# {'id': 153, 'num_samples': 117120, 'path': None, 'audio': {'path': 'train/10061249816683447139.wav', 'array': array([ 0.        ,  0.        ,  0.        , ..., -0.00011563,
#        -0.00013185, -0.00013626]), 'sampling_rate': 16000}, 'transcription': "virgin have only purchased the good bank' of northern rock not the asset management company", 'raw_transcription': 'Virgin have only purchased the ‘good bank’ of Northern Rock, not the asset management company.', 'gender': 1, 'lang_id': 19, 'language': 'English', 'lang_group_id': 0}
fleurs = load_dataset("google/fleurs", "en_us", split="train", streaming=True)
fleurs_iter = iter(fleurs)
while fleurs_iter:
    item = next(fleurs_iter)
    # print(item)
    print("{},{}".format(item['audio']['path'], item['transcription']))
