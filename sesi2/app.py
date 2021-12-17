# x = 0
# y = 5

# if x < y:  # Truthy
#     print("yes")

# if y < x:  # Falsy
#     print("yes")

# if x:  # Falsy
#     print("yes")

# if y:  # Truthy
#     print("yes")

# if "aul" in "grault":  # Truthy
#     print("yes")

# if "quux" in ["foo", "bar", "baz"]:  # Falsy
#     print("yes")

# Does line execute?                        Yes    No
#                                           ---    --
# if "foo" in ["foo", "bar", "baz"]:
#     print("Outer condition is true")

#     if 10 > 20:
#         print("Inner condition 1")

#     print("Between inner conditions")

#     if 10 < 20:
#         print("Inner condition 2")

#     print("End of outer condition")
# print("After outer condition")

# x = 13
# sunny = True
# if x >= 10 and x <= 15 and sunny:
#     print(x)

# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000

# if uang > hargaBuku:
#     print("beli buku")
# else:
#     print("uang tidak cukup")

# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")

# raining = True
# print("Let's go to the", "beach" if not raining else "library")

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k, d[k])
