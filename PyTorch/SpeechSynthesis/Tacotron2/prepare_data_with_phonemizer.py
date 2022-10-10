from phonemizer import phonemize
from phonemizer.separator import Separator
from tacotron2.text import cleaners

#Carefull this need to be batch like (1000 batch file)

with open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/custom_audio_text_test_filelist.txt') as a:
  lines = a.read().splitlines()
  for i, line in enumerate(lines):
    if i<= 1794:
        print("skip", i)
    else:
        string = line
        firstpart = line
        firstpart = firstpart.partition('|')[0]
        string = french_clearners(string.partition('|')[2])
        converted = phonemize(
            string,
            language='fr-fr',
            backend='espeak',
            separator=Separator(phone=None, word=' ', syllable='None'),
            strip=True,
            preserve_punctuation=True,
            njobs=4)
        written = open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/test_2.txt', 'a')
        written.write(firstpart + '|' + converted + '\n')
        written.close()