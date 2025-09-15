a = 1 # int - integer
b = 1.1 # float - floating
c = True # bool - boolean
d = "1" # str - string

#print("{a} - {b}")

# f - format позволяет вставить элементы
#print(f"{a} - {b}")

print (type(a))
print (type(b))
print (type(c))
print (type(d))

# convert float to string
#b = str(b)
#print (type(b))


# input - нужен чтоб вводить данные с консоли
# int() -  конвертация в int
#b = int(input("Enter number"))
#print(b)

test = "Test"

# [0] - вернет эллемент по 0 индексу
# вернет T
#print(test[0])
#print(test.islower())
#print(test.isupper())
#print(test.isprintable())
#print(test.find("e"))
#print(len(test))

a_list = [1,2,3,4,5,6,7,8,9] # list - список
b_list = (1,2,3,4,5,6,7,8,9) # tuple - неизменямый список

# set -  множества это набор из уникальных эллементов
c_set = {1, 1,2,3,4,5,6,7,8,9}
c_set.add(2)
c_set.remove(9)

# dict - словарь это структура данных в формате ключ значение
d_dict = {"one": 1, 2: "two"}
d_dict["one"] = 3
print(d_dict["one"])

for i in range(1,10):
    print(i)

for i in a_list:
    print(i)

a = int(input("Enter number: "))

if a % 2 == 0:
    print("это четное число")
else:
    print("это нечетное число")

b = [1,2,3,4]

if a in [1,2,3,4]:
    print("is in array")
if a in b:
    print("is in array")

if a is int:
    print("is int")
elif a is float:
    print("is float")
else: print("is not number")
