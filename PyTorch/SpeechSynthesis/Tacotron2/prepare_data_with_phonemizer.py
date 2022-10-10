from phonemizer import phonemize
from phonemizer.separator import Separator

#Carefull this need to be batch like (1000 batch file)

with open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/custom_audio_text_test_filelist.txt') as a:
  lines = a.read().splitlines()
  for line in lines:
    string = line
    firstpart = line
    firstpart = firstpart.partition('|')[0]
    string = string.partition('|')[2]
    converted = phonemize(
        string,
        language='fr-fr',
        backend='espeak',
        separator=Separator(phone=None, word=' ', syllable='None'),
        strip=True,
        preserve_punctuation=True,
        njobs=4)
    written = open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/test.txt', 'a')
    written.write(firstpart + '|' + converted + '\n')
    written.close()