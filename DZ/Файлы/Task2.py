# Задача 2 Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит
# слово, имеющее максимальную длину (или список слов, если таковых
# несколько).

text='''Вечерело
Жужжали мухи
Светил фонарик 
Кипела вода в чайнике 
Венера зажглась на небе 
Деревья шумели 
Тучи разошлись
Листва зеленела'''
Name_File='article.txt'
f=open(Name_File,'w+',encoding='utf-8')
f.write(text)
f.close()

def longest_words(file):
    f=open(file,'r',encoding='utf-8')
    words=[]

    for i in f:
        Word_split_in_list=i.split(' ')
        for i in Word_split_in_list:
            word=i
            # print(i1)
            Spell_the_word=[]
            for i in word:
                if i!='\n':
                    Spell_the_word.append(i)
            word_string=''.join(Spell_the_word)
            words.append(word_string)
    maxLen=len(max(words, key=len))
    # print(maxLen)
    print("Слово(ва) с макимальной длиной:")
    for i in words:
        if len(i)==maxLen:
            print(i)
    f.close()

longest_words(Name_File)
