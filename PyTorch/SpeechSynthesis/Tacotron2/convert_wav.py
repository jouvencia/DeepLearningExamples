import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T
import glob
from tqdm import tqdm

path_audio_files = glob.glob("/DeepLearningExamples/Pytorch/SpeechSynthesis/Tacotron2/Custom_dataset/wavs/*.wav")

for path_audio in tqdm(path_audio_files):
  waveform, sample_rate = torchaudio.load(path_audio)
  torchaudio.save("/DeepLearningExamples/Pytorch/SpeechSynthesis/Tacotron2/Custom_dataset/wavs/" +
                  path_audio.split("/")[-1], waveform, sample_rate,encoding="PCM_S", bits_per_sample=16)