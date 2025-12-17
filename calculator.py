
x = 20
y = 0
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "not possible"
    return x/y

print("ADD =", add(x, y))
print("SUB =", sub(x, y))
print("MUL =", mul(x, y))
print("DIV =", div(x, y))



