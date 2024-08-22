# Необходимо написать программу, которая будет принимать на вход строку, разбивать строку на слова по пробелу. Далее
# нужно из всех слов убрать следующие пунктуационные знаки:
#
# !,.?;:#$%^&*(),
#
# а также привести слова к нижнему регистру. В итоге нужно вывести в алфавитном порядке слова, которые состоят как
# минимум из 5 символов, а также имеют как минимум 4 уникальных символа, и которые встретились в исходном тексте
# более 2х раз.

import re

string = input()
string = string.lower()
string = re.sub(r'!|,|\.|\?|;|:|#|\$|%|\^|&|\*|\(|\)', '', string)

words = string.split()

# # поиск количества вхождений слов в тексте
pairs = {}
for word in words:
    if pairs.get(word, None) is None:
        pairs[word] = 1
    else:
        pairs[word] += 1
p = list(pairs.items())
# result = max(p, key=lambda i: i[1])
# print(result[0], result[1])

result_list = list()

for word, count in p:
    if (len(set(word)) >= 4) and (len(word) >= 5) and (count > 2):
        result_list.append(word)

result_list.sort()

for word in result_list:
    print(word)
