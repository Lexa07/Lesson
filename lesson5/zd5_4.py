"""4. Создать (не программно) текстовый файл со следующим
    содержимым:
    One — 1
    Two — 2
    Three — 3
    Fou
    Необходимо написать программу, открывающую файл на чтение и
    считывающую построчно данные. При этом английские числительные
    должны заменяться на русские. Новый блок строк должен записываться
    в новый текстовый файл.
"""

from translate import Translator

with open("text_4.txt", "r", encoding='utf-8') as mytext:
    for line in mytext:
        lench = int(line.find(' - '))
        lang = line[:lench]
        trans = Translator(from_lang="English", to_lang="Russian")
        result = trans.translate(lang)
        with open("translat.txt", "a") as f_obj:
            f_obj.write((''.join([result, line[lench:]])))
