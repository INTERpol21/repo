# 1------------------------------------


def nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in nums(15):
    print(i)

# 3-------------------------------------

from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

res = (i for i in zip_longest(tutors, klasses))

print(type(res))
print(*islice(res, 9))
print(list(islice(res, 3)))

# 4------------------------------------------


my_list = [300, 4, 54, 2, 4, 5, 77, 200, 44, 10, 11]
more = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more)

# 5-----------------------------------------------


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(([i for i in src if src.count(i) == 1]))

my_dict = {i: 0 for i in src}

for i in src:
    if i in my_dict
        my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])



