#1. Сформировать строку, в которой содержится информация определенном слове в строке.
#Например "The [номер] symbol in [тут слово] is [значение символа по номеру в слове]". 
#Слово и номер получите с помощью input() или воспользуйтесь константой.
#Например (если слово - "Python" а символ 3) - "The 3 symbol in "Python" is t".
#2. Ввести из консоли строку. Определить количество слов в этой строке, 
#которые заканчиваются на букву "o" (учтите, что буквы бывают заглавными).
#3. Есть list с данными lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
#Напишите механизм, который cформирует новый list (например lst2), который содержит только 
#переменные типа str, которые есть в lst1.



#1
string = 'The 3 symbol in "Legace" is'
symbol = '"g"'
newString = ' {0} and symbol {1}'.format(string, symbol)
print(newString)


        
#2        
string = (input('Введите строку из слов, в которой есть слова, заканчивающееся на букву "o" '))
list = []
i = 0 
while i < len(string) and string[i] != ":": 
    word = "" 
    while i < len(string) and string[i] != ";"  and string[i] != "," and string[i] != ":": 
        word += string[i]
        i =  i + 1
    list.append(word)
    i = i + 2 
x = 0
for word in list:
    if word[len(word)-1] == 'о' or 'О':
        x = x + 1
print(x)





#3

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = [j for i, j in enumerate(lst1) if i not in [2, 3, 5, 7, 8, 11, 12]]

print(lst2)

