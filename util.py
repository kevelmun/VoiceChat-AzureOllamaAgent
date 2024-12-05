import os
import time
start_time = time.time()


def clean_wav_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            os.remove(os.path.join(folder, filename))

def report_time(message_time):
    global start_time 
    end_time = time.time()
    elapsed_time = end_time - start_time
    start_time = time.time()
    print(f"{message_time}{elapsed_time}")