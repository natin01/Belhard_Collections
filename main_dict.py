persons = [
    {'name': 'Anna', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 15, 'gender': 'female'},
    {'name': 'Lena', 'age': 12, 'gender': 'female'},
    {'name': 'Nastya', 'age': 33, 'gender': 'female'},
    {'name': 'Angelina', 'age': 30, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Anna', 'age': 40, 'gender': 'female'},
    {'name': 'Ira', 'age': 11, 'gender': 'female'},
    {'name': 'Polina', 'age': 17, 'gender': 'female'},
    {'name': 'Oksana', 'age': 18, 'gender': 'female'},
    {'name': 'Anna', 'age': 8, 'gender': 'female'},
    {'name': 'Yana', 'age': 43, 'gender': 'female'},
    {'name': 'Kira', 'age': 18, 'gender': 'female'},
    {'name': 'Nastya', 'age': 25, 'gender': 'female'},
    {'name': 'Tamara', 'age': 31, 'gender': 'female'},
    {'name': 'Rita', 'age': 39, 'gender': 'female'},
    {'name': 'Sveta', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Nastya', 'age': 28, 'gender': 'female'},
    {'name': 'Lera', 'age': 19, 'gender': 'female'},
    {'name': 'Sara', 'age': 10, 'gender': 'female'},
    {'name': 'Alex', 'age': 44, 'gender': 'male'},
    {'name': 'Dima', 'age': 33, 'gender': 'male'},
    {'name': 'Fedor', 'age': 38, 'gender': 'male'},
    {'name': 'Nikita', 'age': 32, 'gender': 'male'},
    {'name': 'Alex', 'age': 25, 'gender': 'male'},
    {'name': 'Foma', 'age': 7, 'gender': 'male'},
    {'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Kiril', 'age': 27, 'gender': 'male'},
    {'name': 'Mihail', 'age': 30, 'gender': 'male'}
]
# task 1
persons_num = len(persons)
print(f"Количество людей:{persons_num}")

# task 2
female_num = 0
for i in persons:
    #print (i)
    #print (i.get("gender"))
    if i.get("gender") == "female":
        female_num = female_num + 1
print(f"Количество женщин: {female_num}")
male_num = 0
for i in persons:
    if i.get("gender") == "male":
        male_num = male_num + 1
print(f"Количество мужчин: {male_num}")

# task 3
adult_num = 0
for i in persons:
    if i.get("age") >= 18:
        adult_num = adult_num + 1
print(f"Количество совершеннолетних: {adult_num}")

# task 4
for i in persons:
    print(i.get("name"))

# task 5
age_set = set()
for i in persons:
    age_set.add(i.get("age"))
print(age_set)

# task 6
from collections import Counter
names_list = list()
for i in persons:
    names_list.append(i.get("name"))
my_counter = Counter(names_list)
print(my_counter.most_common(3))

# task 7
# All male older 35, name starting with F
for i in persons:
    if i.get("gender") == "male" and i.get("age") >=35 and i.get("name")[0] =="F":
        print(i.get("name"))
