# a = int(input())
# b = int(input())
# c = (a**2+b**2)**0.5
# S = a*b/2
# print(f"Треугольник 1 с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}")

katet_str = input("Введите катеты:")
katet_list = katet_str.split()

#katet_list1 = (katet_list[0, len(katet_list), 2])
#katet_list2 = (katet_list[1, len(katet_list), 2])

if len(katet_list) % 2 != 0:
    raise RuntimeError("InconsistentDataError")

print(katet_list)
print(len(katet_list))
i = 0
cnt = 1
while i < len(katet_list):
    try:
        S = int(katet_list[i]) * int(katet_list[i+1]) / 2
    except:
        raise RuntimeError("NonNumericError")
    else:
        c = (int(katet_list[i])**2 + int(katet_list[i+1])**2)**0.5
        print(f"Треугольник {cnt} c катетами {katet_list[i]} и {katet_list[i+1]} имеет площадь {S} и гипотенузу {c}")
        i = i+2
        cnt = cnt + 1

