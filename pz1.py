#1pz

duration = int(input("Enter all the time in second: "))

days = duration // 3600 // 25
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print("days: ", days, ",", "hours: ", hours, ",", "minutes: ", minutes, ",", "seconds: ", seconds, ".", sep="")

#---------------------------------------------------------------------------------------------------------
#2pz


list = []
add_list = []
sum = 0


for i in range(1, 1001, 2):
    list.append(i**3)

for ind, val in enumerate(list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum += add_list[ind]

print(sum)

for m in list:
    add_list.append(m+17)

sum = 0

for ind, val in enumerate(add_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum += add_list[ind]

print(sum)




#--------------------------------------------------------------------------------------------------
#pz3

for procent in range (20):
    if procent % 10 == 1 and procent % 20 != 11:
        print(procent, "процент", end=" ")
    elif 1 < procent % 10 < 5 and not 11 < procent % 20 < 15:
        print(procent, "процента", end=" ")
    else:
        print(procent, "процентов", end=" ")