name="waseem saleem"
name=name.capitalize()
print(name)
name=name.casefold()
print(name)
name=name.center(1)
print(name)
n=name.count('a')
print(n)
name=name.encode()
print(name)
b="blow".endswith("b")
print(b)
b="blow".endswith('w')
print(b)
b="blow".startswith("a")
print(b)
b="blow".startswith("b")
print(b)
b="good".find("o")
print(b)
b="good".rfind("o")
print(b)
b="good".index("d")
print(b)
name="waseem".format()
print(name)
name="waseem".isalpha()
print(name)
d="01234".isdecimal()
print
d="01234".isnumeric()
print("yes",d)
d="01234".isdigit()
print(d)
name="waseem saleem"
b=name.islower()
print(b)
b=name.isupper()
print(b)
b=name.upper()
print(b)
b=name.isprintable()
print(b)
b="$@#$@#$@!"
a=b.isprintable()
print(a,"yes dude")
a="       "
b=a.isspace()
print(b,"yes it is a space")
t="Welcome To The Space".istitle()
print(t,"yes it a title")
fname="waseem aleem"
######################split() convert string to bytearray
######################join() convert array to string
names=['waseem','aleem','gulzar','sadar','rabia']
names=' , '.join(names)
print(names)
name="waseem azeem"
name=name.replace('azeem','saleem')
print(name)
p="welcome to The \n world of the lands \n of the beauty"
para=p.splitlines()
print(para)
ind="HaPPy InDepence DaY"
ind=ind.swapcase()
print(ind)
