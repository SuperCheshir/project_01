# Задача 3
# Поиск самых высокооплачиваемых работников

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

# Вариант 1 - цикл (развёрнутый)

# top_mgrs = []
# for name in employees.keys():
#     if employees[name] >= 100000:
#         top_mgrs.append(name)

# print(top_mgrs) 

# x = 4
# if x > 0:
#     print("Больше 0")
# else:
#     print("Меньше 0")

# print(
#      "Больше 0" if x > 0 else "Меньше 0" 
#     )

# Вариант альт - используем for

# for i in [1, 2, 3]:
#     print(i**2)

# print(
#     [i**2 for i in [1, 2, 3]]
# )
# Вариант 2 - списковые включения (однострочники)

top_mgrs = [n for n in employees if employees[n] >= 100000]
print(top_mgrs) #[True, False, True, False, False]
top_mgrs = [n for n, s in employees.items() if s >= 100000]
print(top_mgrs)