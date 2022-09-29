#!/usr/bin/env bash

set -e

DATADIR="Custom_dataset"
FILELISTSDIR="filelists"

TESTLIST="$FILELISTSDIR/custom_audio_text_test_filelist.txt"
TRAINLIST="$FILELISTSDIR/custom_audio_text_train_filelist.txt"
VALLIST="$FILELISTSDIR/custom_audio_text_val_filelist.txt"

TESTLIST_MEL="$FILELISTSDIR/custom_mel_text_test_filelist.txt"
TRAINLIST_MEL="$FILELISTSDIR/custom_mel_text_train_filelist.txt"
VALLIST_MEL="$FILELISTSDIR/custom_mel_text_val_filelist.txt"

mkdir -p "$DATADIR/mels"
if [ $(ls $DATADIR/mels | wc -l) -ne 13100 ]; then
    python3 preprocess_audio2mel.py --wav-files "$TRAINLIST" --mel-files "$TRAINLIST_MEL" --text-cleaners "french_cleaners"
    python3 preprocess_audio2mel.py --wav-files "$TESTLIST" --mel-files "$TESTLIST_MEL" --text-cleaners "french_cleaners"
    python3 preprocess_audio2mel.py --wav-files "$VALLIST" --mel-files "$VALLIST_MEL" --text-cleaners "french_cleaners"
fi	
