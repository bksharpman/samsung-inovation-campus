# surname = input()
# name = input()
# f_name = input()
# print(f"{surname.capitalize()} {name.capitalize()[0]}.{f_name.capitalize()[0]}")


# passwd = input()
# answer = ((len(passwd)>=8) and (any(i.islower() for i in passwd)) and (any(i.isupper() for i in passwd)) and (any(i.isdigit() for i in passwd)))
# print(answer)


# a_var = input()
# b_var = a_var.replace("a","x").replace("b","a").replace("x","b").replace("A","X").replace("B","A").replace("X","B")
# print(b_var)


# string = "3-комнатная квартира, 117.2 м², 2/12 этаж, Гагарина — Ескараева"
# string = string.split(", ")

# #4
# rooms_parts = string[0]
# rooms = int(rooms_parts.split('-')[0])

# #5
# square_parts = string[1]
# square = float(square_parts.split(' ')[0])

# #6
# floors = 0
# totalFloors = 0
# floors_parts = string[2]
# floors = int()
# if '/' in floors_parts:
#   floors = int(floors_parts.split('/')[0])
#   totalFloors = (floors_parts.split('/')[1].split(' ')[0])
# elif ' ' in floors_parts:
#   floors = int(floors_parts.split(' этаж')[0])
# else:
#   pass

# #7
# address = ""
# crossing = ""
# address_parts = string[3]
# if '—' in address_parts:
#   address = address_parts.split(' — ')[0]
#   crossing = address_parts.split(' — ')[1]
# else:
#   address = address_parts


# print(f"Комнатность: {rooms}")
# print(f"Площадь: {square} кв. м")
# print(f"Этаж: {floors} из {totalFloors}")
# print(f"Адрес: {address}")
# print(f"Пересечение с улицой: {crossing}")
