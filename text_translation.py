from googletrans import Translator

#file_path = './Files/subtitles_class_1.txt'
file_path = './Files/class_1_5049.txt'

translator = Translator()

file = open(file_path, 'r', encoding='utf-8')
contents = file.read()

#loop
    #keep lines separated
    #save till "." at the end of line
    #translate
    #save

result = translator.translate(contents, dest='en')

#file_name = 'class_1.txt'
file_name = 'class_1_5049.txt'

file = open('./Files/translation_' + file_name, "w", encoding='utf-8')
file.write(result.text)   
file.close()

