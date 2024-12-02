import os

def clean_wav_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            os.remove(os.path.join(folder, filename))
