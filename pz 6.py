# 1

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    dict = {}
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)

    for i in content:
        print(i)

# 2

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    dict = {}
    content = (line.split()[0] for line in f)

    for i in content:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    sorted_keys = sorted(dict, key=dict.get)
    print(f"Spammer {sorted_keys[-1]} - {dict[sorted_keys[-1]]} times")


#3

from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): (el[1].strip()) for el in all_list}

        with open('dict_n_h.json', 'w', encoding='utf-8') as f:
            if "None" in my_dict:
                exit(1)
            else:
                dump(my_dict, f, ensure_ascii=False, indent=4)
                print(my_dict)

#6

from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as donut_a:
    with open("bakery.csv", "r", encoding="utf-8") as donut_r:
        if len(argv) == 1:
            print(donut_r.read())
        elif len(argv) == 2:
            if "," in argv[1]:
                donut_r.read()
                print(argv[1], file=donut_a)
            else:
                print(*donut_r.readlines()[int(argv[1]) - 1:], sep="")
        else:
            print(*donut_r.read().split()[int(argv[1]):int(argv[2]) + 1], sep="\n")


#7

from sys import argv

with open("bakery.csv", "r+", encoding="utf-8") as donut_r:
    pos, val = argv[1:]
    for line in range(int(pos) - 1):
        n = donut_r.readline()

#Дальше не знаю что делать((((