# from decouple import config

# name = config("NAME", default='Python')
# print(name)
# print(type(name))


# pwd = config("PASSWORD", default='123456', cast=int)
# print(pwd, type(pwd))

def name(fulname: str) -> list:
    return fulname.split("-")

print(name("abdymambetov-meder"))

i=2
x=[]
while i<=6:
    x.append(i)
    i=i+2

print(x)