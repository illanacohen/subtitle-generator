import pysubs2
import pysrt


file_path = './Files/class_1_5049.txt'

text = open(file_path, 'r', encoding='utf-8', errors='ignore')

with open(file_path[:-4] + '.srt', 'w', encoding='utf-8') as subs:
    subs.write(text.read())

subs = pysubs2.load(file_path[:4] + '.srt')
subs
