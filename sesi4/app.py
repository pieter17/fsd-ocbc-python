file = open('Hack8_Sample_Text.txt')
file.close()

with open("sample.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

f = open("sample.txt", 'r', encoding='utf-8')

f.read(4)

import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
assert ('windows' in sys.platform), "This code runs on Windows only."


def perkalian_dengan_0(num1):
    return 0 * num1 + 1


sepuluh_kali_0 = perkalian_dengan_0(10)
assert sepuluh_kali_0 == 0, 'fungsi masih salah'
# a+=1


def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')


try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

try:
    with open('file.log') as file:
        read_data = file.read
except:
    print('Could not open file.log')

# Have a look at the following example:

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')