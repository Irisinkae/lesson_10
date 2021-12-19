import pickle


#1.Работа с файлом
with open('test.txt', 'w') as f:
   f.write('Тестовая строка')
with open('test.txt','r') as file:
   print (file.read())



# 2.Pickle
d= {'Russia' : 'Moscow',
    'China' : 'Beijing',
    'USA' : 'Washington'}
with open('test_2.txt', 'wb') as f:
    pickle.dump(d, f)
with open('test_2.txt', 'rb') as f:
    d_new = pickle.load(f)
print(d.items())

