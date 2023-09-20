
# Функция это блок кода, который можно вызывать с разными параметрами
# Функии это молотилки данных. Внутрь помещаются значения, на выходе получаем 
# результат


employees_1 = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

employees_2 = {
    'Nikita' : 1,
    'Masha' : 110000,
    'Matvey' : 90000 ,
    'Sasha' : 88123,
    'Tanya' : 193121}

# top_mgrs = [n for n, s in employees_1.items() if s >= 100000]
# top_mgrs = [n for n, s in employees_2.items() if s >= 100000]
# print(top_mgrs)

# Этап создания функции

def get_topmgrs(empl):
  return [n for n, s in empl.items() if s >= 100000]
#   print(top_mgrs)  

# Этап вызова функции

get_topmgrs(employees_1)
get_topmgrs(employees_2)

#  Воспользуемся результатом работы функции
print([employees_1[i]*1.5 for i in get_topmgrs(employees_1)])
