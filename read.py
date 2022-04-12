import pickle


class Stud:
    fam = None
    name = None
    nom = None
    dr = None


f = open('Friends.dat', 'rb')
mas = pickle.load(f)
while True:
    print()
    print('Введите необходимое число для операции с БД:')
    print('1 - Для добавление нового друга в БД')
    print('2 - Сортировать всез друзей по дате рождения')
    print('3 - Печать БД')
    print('4 - Редактирование имеющихся друзей')
    print('5 - Всё о друге (За просмотр информации - 500 обезьяньих долларов в BTD6)')
    print('6 - Выход')
    print()
    n = int(input())
    if n == 1:
        print('Введите фамилию, имя, номер телефона и дату рождению')
        s = input()
        x = s.split()
        st = Stud()
        st.fam = x[0]
        st.name = x[1]
        st.nom = x[2]
        st.dr = list(map(int, x[3].split('.')))
        mas.append(st)
    if n == 2:
        mas.sort(key=lambda y: int(y.dr[0]))
        mas.sort(key=lambda y: int(y.dr[1]))
        mas.sort(key=lambda y: int(y.dr[2]))

    elif n == 3:
        for x in mas:
            print(x.fam, ' ', x.name, ' ', x.nom, ' ', x.dr[0], '.', x.dr[1], '.', x.dr[2], sep='')
    elif n == 4:
        print('Введите фамилию, имя и телефон друга:')
        snt=input().split(' ',2)
        print('Введите новые данные в фoрмате: <<Фамилия>>, <<Имя>>, <<Телефон>>, <<Дата рождения>>')
        newdata=input().split(' ',3)
        fla=False
        for i in mas:
            if i.fam == snt[0] and i.name == snt[1] and i.nom == snt[2]:
                fla = True
                i.fam = newdata[0]; i.name=newdata[1]
                i.nom = newdata[2]; i.dr = list(map(int, newdata[3].split('.')))
        if fla == False:
            print('Такого нет или ошибка в ведённых данных (телефон начинать с цифры "8")')
    elif n == 5:
        print('Введите имя друга:')
        q=[]
        nam=input()
        for x in mas:
            if x.name==nam:
                q.append(x)
        if len(q)==0:
            print('Такого нет')
        elif len(q)==1:
            print(q[0].fam, ' ', q[0].name, ' ', q[0].nom, ' ', q[0].dr[0], '.', q[0].dr[1], '.', q[0].dr[2], sep='')
        else:
            print('Таких несколько:')
            for x in q:
                print(x.fam, ' ', x.name, ' ', x.nom, ' ', x.dr[0], '.', x.dr[1], '.', x.dr[2], sep='')
    elif n == 6:
        v = input('Выйти Y/N:').upper()
        if v == 'Y':
            break
    else:
        print('Нет такой операции в БД')
fout = open('students.dat', 'wb')
pickle.dump(mas, fout)
f.close()
fout.close()