import speech_recognition as sr
import os 

from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

import audioread
import math

from datetime import datetime, timedelta

r = sr.Recognizer()


AUDIO_FILE = "./Files/class_01.wav"              
text_file = './Files/class_01.txt'

def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    sound = AudioSegment.from_wav(path)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    nonsilent_ranges = detect_nonsilent(sound, min_silence_len=500, silence_thresh=sound.dBFS-14)

    for range_ in nonsilent_ranges:
        for i in [0,1]:            
            seconds = range_[i]/1000
            miliseconds,seconds = math.modf(seconds)
            miliseconds =str(miliseconds)[2:5]
            minutes,seconds = divmod(seconds, 60)
            hours,minutes = divmod(minutes, 60)
            range_[i] = "{:%H:%M:%S},{}".format(datetime(1,1,1,round(hours), round(minutes), round(seconds)), miliseconds)

    nonsilent_ranges = [f"{time[0]} --> {time[1]}" for time in nonsilent_ranges]

    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened, language='es-CL')
            except sr.UnknownValueError as e:
                print("Error:", str(e))
                line = "None"
            else:
                line = f"{text.capitalize()}"
                print(line)

            text_data = {
                "index": i,
                "interval": nonsilent_ranges[(i-1)],
                "text": line
            }
            whole_text += "{index}\n{interval}\n{text}\n\n".format(**text_data)
    file = open(text_file, "w", encoding='utf-8')
    file.write(whole_text)   
    file.close()
    return whole_text

whole_text = get_large_audio_transcription(AUDIO_FILE)


