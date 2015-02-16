__author__ = 'eric'

# ActiveCode 3 (ch08_methods2): more str methods

food = "banana bread"
print(food.capitalize()) # upper-case just the first letter of each word

print("*"+food.center(25)+"*") # center the string in width 25 field
print("*"+food.ljust(25)+"*")  # left-justify; stars added to show bounds
print("*" +food.rjust(25)+"*") # right-justify within 25 field

print(food.find("e"))   # find(st) returns index of first st (start at left)
print(food.find("na"))
print(food.find("b"))

print(food.rfind("e"))  # rfind(st) starts from right, searches left
print(food.rfind("na"))
print(food.rfind("b"))

print(food.index("e"))
