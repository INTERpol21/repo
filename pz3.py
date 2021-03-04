# 1----------------------------------------------------------


text = {"zero": "ноль", "one": "один", "two": "два",
        "three": "три", "four": "четыре", "five": "пять",
        "six": "шесть", "seven": "семь", "eight": "восемь",
        "nine": "девять", "ten": "десять"}


def translate(word):
    return text.get(word)


print(translate(input("Enter number: ")))

# 2--------------------------------------------------------------------

text = {"zero": "ноль", "one": "один", "two": "два",
        "three": "три", "four": "четыре", "five": "пять",
        "six": "шесть", "seven": "семь", "eight": "восемь",
        "nine": "девять", "ten": "десять"}


def translate(word):
    in_word = word.lower()
    if word.istitle() and in_word in text:
        return text.get(in_word).title()
    return text.get(word)


print(translate(input("Enter number: ")))


# 3-------------------------------------------------------------------


def rus(*args):
    name = {}
    for i in sorted(args):
        letter = i[0]
        if letter in name:
            name[letter] += [i]
        else:
            name[letter] = [i]
    return name


print(rus("Вася", "Коля", "Марина", "Илья", "Антон", "Олег", "Инна", "Оля"))


# 4------------------------------------------------

def rus(*names):
    names_dict = {}
    for name in sorted(names):
        a, b = name.split()
        val = names_dict.setdefault(b[0], {a[0]: [name]})
        n_val = val.setdefault(a[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_dict


print(rus("Петр Сергеев", "Анна Иванова", "Павел Басков",
          "Антон Журавлев", "Борис Бурков", "Олег Вельман"))
