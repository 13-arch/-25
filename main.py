'''Одна из основных операций с числами – их сравнение. Мы подозреваем, что вы в совершенстве владеете этой 
операцией и можете сравнивать любые числа, в том числе и целые. В данной задаче необходимо сравнить два целых числа.
Входные данные
В двух строчках входного файла INPUT.TXT записаны числа A и B, не превосходящие по абсолютной величине 2×109.
Выходные данные
Запишите в выходной файл OUTPUT.TXT один символ "<", если A<B, ">", если A>B и "=", если A=B.'''
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
data = data.split()
a=int(data[0])
b=int(data[1])
if a>b:
    output_data.write('>')
elif a<b:
    output_data.write('<')
elif a==b:
    output_data.write('=')
output_data.close()
input_data.close()