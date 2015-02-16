__author__ = 'eric'

# ActiveCode 14: Creating a new string from another - but leaving the
#   original unchanged

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:] # doesn't change greeting

print(newGreeting)
print(greeting)            # same as it was
