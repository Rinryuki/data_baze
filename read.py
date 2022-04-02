import pickle


class Stud:
    fam = None
    name = None
    surn = None
    bal = None


f = open('students.dat', 'rb')
mas = pickle.load(f)
while True:
    print()
    print('Введите необходимое число для операции с БД')
    print('1 - для сортировки БД по убыванию среднего балла')
    print('2 - для поиска в БД студентов, имеющих двойки')
    print('3 - для редактирования записи в БД')
    print('4 - печать БД')
    print('5 - выход из БД')
    print()
    n = int(input())
    if n == 1:
        mas.sort(key=lambda y: sum(y.bal) / len(y.bal), reverse=True)
        for x in mas:
            print(x.fam, x.name, x.surn, *x.bal)
    elif n == 2:
        for x in mas:
            if 2 in x.bal:
                print(x.fam, x.name, x.surn, *x.bal)
    elif n == 3:
        fml = input('Введите фамилию студента: ')
        print('Введите полную новую запись: фамилию, имя, отчество, 5 оценок через пробел')
        new = input()
        for x in mas:
            if x.fam == fml:
                new = new.split(' ', 3)
                x.fam = new[0]
                x.name = new[1]
                x.surn = new[2]
                x.bal = list(map(int, new[3].split()))
    elif n == 4:
        for x in mas:
            print(x.fam, x.name, x.surn, *x.bal)
    elif n == 5:
        v = input('Выйти Y/N:').upper()
        if v == 'Y':
            break
    else:
        print('Нет такой операции в БД')
fout = open('students.dat', 'wb')
pickle.dump(mas, fout)
f.close()
fout.close()
