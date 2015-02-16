__author__ = 'eric'

# ActiveCode 2 (ch08_methods1): illustrates string (str) methods

ss = "    Hello, World    "

# ss.count(s) returns count of substring s within str ss

els = ss.count("l") # count() takes a single str argument
print(els)

# ss.strip() trims leading and trailing blanks of ss, returning new str

print("***"+ss.strip()+"***")
print("***"+ss.lstrip()+"***")
print("***"+ss.rstrip()+"***")

# ss.replace(a,b) replaces each occurrence of str a with str b

news = ss.replace("o", "***")
print(news)
