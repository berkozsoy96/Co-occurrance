import string
from functools import reduce


def open_file():
    fp = open("einstein.txt")
    i = 0
    data_dict = {}
    for oku in fp:
        i += 1
        sp = oku.split(" ")
        for j in range(len(sp)):
            sp[j] = sp[j].lower()
            exclude = set(string.punctuation)
            sp[j] = ''.join(ch for ch in sp[j] if ch not in exclude)
            if len(sp[j]) > 1:
                if sp[j].endswith("\n"):
                    sp[j] = sp[j][:len(sp[j])-1]

                if data_dict.get(sp[j]) is None:
                    data_dict[sp[j]] = {i}
                else:
                    temp = data_dict.get(sp[j])
                    temp.add(i)
                    data_dict[sp[j]] = temp
    return data_dict


def find_cooccurrence(data, find):
    find = find.lower()
    find = ''.join(ch for ch in find if ch not in string.punctuation)
    sp = find.split(" ")
    bayrak = True
    if len(sp) > 1:
        for i in range(len(sp)):
            if data.get(sp[i]) is None:
                bayrak = False
                break
        for i in range(len(sp)-1):
                if bayrak:
                    sonuc = reduce(lambda x, y: x & y, [data[sp[i]], data[sp[i+1]]])
                    print(sonuc)
                else:
                    print("None")
    else:
        if data.get(sp[0]) is None:
            print("None")
        else:
            print(data[sp[0]])


def main():
    data = open_file()
    while True:
        find = input("Bulmak istediğiniz ortak kelimeleri giriniz:")
        if (find != 'q') and (find != 'Q'):
            find_cooccurrence(data, find)
        else:
            print("Bye.!")
            break

if __name__ == '__main__':
    main()
