# file.txt translation code using translate module
from translate import Translator
my_file = open('test.txt', 'r')
text = my_file.read()
translation = Translator(to_lang='es')

to_translate = translation.translate(text)
print(to_translate)
