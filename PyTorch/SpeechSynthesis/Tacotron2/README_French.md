1.
Ensure your Audio files are all WAV PCM 16 Bit files. You may have to convert them.

2.
Get your data into a filelist.
https://github.com/NVIDIA/tacotron2/blob/master/filelists/ljs_audio_text_val_filelist.txt
For every file in your dataset you'll have a
FILE PATH and a Quote separated by a |

3.
Clean your text according to the language (in french do not use ASCII). Then pass it to a french phonemizer

4. 
Split that filelist into 2/3 files, a train list, validation list and test list.
I normally do 95% files into the train, 5% into validation and ignore the test list.

5
Once you have the filelists ready, update
https://github.com/NVIDIA/tacotron2/blob/master/hparams.py#L28#L29
To point to your train and validation filelists.

6
Since your using another language, you will need to update the symbols list.
Change,
_punctuation and _letters Phonemes to include all the symbols you will use from your language.


6.
update the text_cleaners hparam for your language.

There are 3 cleaners you can try
Located Here

def basic_cleaners(text):

def transliteration_cleaners(text):

def english_cleaners(text):

You should probably update the hparam

        text_cleaners=['english_cleaners'],

to

        text_cleaners=['french_cleaners'],

to start with.

7.
Train from Scratch.
https://github.com/NVIDIA/tacotron2#training
or
Training using a pre-trained model
https://github.com/NVIDIA/tacotron2#training-using-a-pre-trained-model