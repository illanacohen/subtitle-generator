from .srt_to_txt import has_no_text

original_file = './Files/subtitles_test.srt'
translated_file = './Files/translation_test.txt'

def txt_srt_converter(file_name=original_file, new_file_name=translated_file):
  with open(file_name, encoding='utf-8', errors='replace') as file:
    lines = file.readlines()
    new_file = open(new_file_name, encoding='utf-8', errors='replace')
    new_lines = new_file.readlines()
    for i in range(len(lines)):
        if has_no_text(lines[i]):
            continue
        else:
            lines[i] = new_lines[0]
            new_lines = new_lines[1:]

  new_file_name = new_file_name[:-4] + '.srt'
  with open(new_file_name, 'w') as new_file:
    for line in lines:
      new_file.write(line)
txt_srt_converter() 