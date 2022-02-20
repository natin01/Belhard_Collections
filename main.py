# a = int(input())
# b = int(input())
# c = (a**2+b**2)**0.5
# S = a*b/2
# print(f"Треугольник 1 с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}")

katet_str1 = input("Введите первые катеты а:")
katet_str2 = input("Введите вторые катеты b:")
katet_list1 = katet_str1.split()
katet_list2 = katet_str2.split()

if len(katet_list1) != len(katet_list2):
    raise RuntimeError("InconsistentDataError")

print(katet_list1)
print(len(katet_list1))

for i in range(len(katet_list1)):
    print(f"Треугольник {i+1} c катетами {katet_list1[i]} и {katet_list2[i]}")
