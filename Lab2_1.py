import math as m

a = 4
b = 6
x = a
h = 0.2

while x <= b:
    x = round(x, 2)
    if x < 4.5:
     sum = m.cos(pow(x, 2))    
    elif x < 5:
     sum = x + m.log1p(pow(x, 7))
    else:
      sum = m.log10(pow(m.e, x) + 4)
    print(f"x: {x}")
    print(f"Result: {sum}")
    x += h
print("The end.")