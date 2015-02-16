__author__ = 'eric'

# ActiveCode 13 (cg08_imm1): strings are immutable (illegal to change elt)

greeting = "Hello, world!"
greeting[0] = 'J'            # ERROR!
print(greeting)
