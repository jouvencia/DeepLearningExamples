with open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/custom_audio_text_train_filelist.txt') as a:
  lines = a.read().splitlines()
  for i, line in enumerate(lines):
    print(i, line)
    string = line
    firstpart = line
    firstpart = firstpart.partition('|')[0]
    string = string.partition('|')[2]
    written = open('/DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/filelists/custom_mel_text_train_filelist.txt', 'a')
    written.write('Custom_dataset/mels/' +  firstpart.split('.')[0] + ".pt" + '|' + string + '\n')
    written.close()
    print('Custom_dataset/mels/' +  firstpart.split('.')[0] + ".pt" + '|' + string + '\n')
print("done")