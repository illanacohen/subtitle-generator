import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent
import audioread
from datetime import datetime, timedelta
import math
import codecs


file = codecs.open("./Files/subtitles_class_1.txt", "r", "utf-8")

a = 'hoslaksa.dsdsd'
print(a.split('.'))