my_tuple = ("Рубченков", "Артём", 19)

people = []
people.append(my_tuple)
print(people)

tuple1 = ("Алекссев", "Евгений", 20)
people.append(tuple1)

tuple2 = ("Николаев", "Данил", 23)
people.append(tuple2)

tuple3 = ("Егорова", "Александра", 18)
people.append(tuple3)

print(people)
list.sort(people)

print("Отсортированный список: ")
print(people)
