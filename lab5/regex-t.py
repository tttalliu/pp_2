# task 1
import re

with open("row.txt", "r", encoding="utf-8") as my_file:
    file_r = my_file.read()


def text_match(text):
    matches = re.findall("a{1}b*", text)
    if matches:
        return ", ".join(matches)


print(text_match(file_r))


# task2
def text_match(text):
    matches = re.findall("ab{2,3}", text)
    if matches:
        return ", ".join(matches)


print(text_match(file_r))


# task3
def text_match(text):
    matches = re.findall("[a-z]+_[a-z]+", text)
    if matches:
        return ", ".join(matches)


# task4
def text_match(text):
    matches = re.findall('[A-Z]{1}[a-z]+', text)
    if matches:
        return ', '.join(matches)
    
#task5
def text_match(text):
    matches = re.findall('a.*?b$', text)
    if matches:
        return ', '.join(matches)
    
#task6
import re

txt = "The rain in Spain"
x = re.sub("[ ,.]", ":", txt)
print(x)

#task7
import re
def snakeToCamel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snakeToCamel('we_oui'))

#task8 
import re
text = "WeREKfsOpf"
print(re.findall('[A-Z][^A-Z]*', text))

#task9
import re
def w(txt):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(w("VjbdUiihvRuhk"))

#task10
import re
def camelToSnake(str):
    m=re.findall(r'([A-Z][a-z]*)', str)
    f='_'.join(m).lower()
    return f

print(camelToSnake('WeOui'))