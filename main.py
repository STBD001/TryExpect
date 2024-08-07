x = 12
y = 0

print("I will try to divide by 0")
try:
    print(x / y)
except ZeroDivisionError:
    print("Don't divide by 0!")
    print("It's except ZeroDivisionError")
    print("-----------------------------------")

print("I will try to add two different types")
try:
    print(x + '!')
except TypeError:
    print("Data type error")
    print("It's except TypeError")
    print("-----------------------------------")

print("What if I call the Index of a list that has no value")
try:
    lista = []
    print(lista[0])
except IndexError:
    print("Not enough data in the list")
    print("It's except IndexError")
    print("-----------------------------------")

print("I will try to access a non-existent key in a dictionary")
try:
    dictionary = {'a': 1, 'b': 2}
    print(dictionary['c'])
except KeyError:
    print("Key not found in dictionary")
    print("It's except KeyError")
    print("-----------------------------------")

print("I will try to import a module that doesn't exist")
try:
    import non_existent_module
except ModuleNotFoundError:
    print("Module not found")
    print("It's except ModuleNotFoundError")
    print("-----------------------------------")

print("I will try to open a file that doesn't exist")
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
    print("It's except FileNotFoundError")
    print("-----------------------------------")

print("I will try to perform an invalid operation on a set")
try:
    my_set = {1, 2, 3}
    print(my_set[0])
except TypeError:
    print("Invalid operation on a set")
    print("It's except TypeError")
    print("-----------------------------------")
