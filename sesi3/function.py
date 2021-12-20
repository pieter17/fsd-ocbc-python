# Function definition is here
def penjumlahan(num1, num2, num3):
    return num1 + num2 + num3


def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)


def changeme(mylist):
    '''This changes a passed list into this function'''
    mylist = mylist + [1, 2, 3, 4]
    print("\nValues inside the function : ", mylist)
    return mylist


# Now you can call changeme function
mylist = [10, 20, 30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme(mylist)
print("\nValues outside the function - after  : ", mylist)

luas = my_function(10, 3)
print(f'luas persegi panjang {luas}')  # return untuk mengubah hasil

hasil_penjumlahan = penjumlahan(50, 60, 4)
print(f'hasil penjumlahan = {hasil_penjumlahan}')


def save_data(name, age):
    print(f'name : {name}')
    print(f'Aget + 10 : {age+10}')


def printinfo(name, age=26):
    '''This prints info into this function'''
    print("Name:", name)
    print("Age:", age)
    return


printinfo(age=50, name="hacktiv8")
printinfo(name='hacktiv')


# Function definition is here
def printinfo(arg1, *vartuple):
    # def printinfo(arg1, arg2, arg3, arg4):
    '''This prints a variable passed arguments'''
    print('arg1     : ', arg1)
    print('vartuple : ', vartuple)
    print('')

    for var in vartuple:
        print('isi vartuple : ', var)


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50, "a")


def person_car(total_data, **kwargs):
    '''Create a function to print who owns what car'''
    print('Total Data : ', total_data)
    for key, value in kwargs.items():
        print('Person : ', key)
        print('Car    : ', value)
        print('')


person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# Parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs = {
#     'jimmy': 'chevrolet',
#     'frank': 'ford',
#     'tina': 'honda'
# }

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))


def penjumlahan_pengurangan(num1, num2):
    sums = num1 + num2
    subt = num1 - num2
    return sums, subt


print(penjumlahan_pengurangan(10, 2))
