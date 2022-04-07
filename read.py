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
    print('Введите необходимое число для операции с БД')
    print('1 - для добавление нового друга в БД')
    print('2 - сортировать всез друзей по дате рождения')
    print('3 - для печати')
    print('4 - для выхода')
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
        v = input('Выйти Y/N:').upper()
        if v == 'Y':
            break
    else:
        print('Нет такой операции в БД')
fout = open('students.dat', 'wb')
pickle.dump(mas, fout)
f.close()
fout.close()
