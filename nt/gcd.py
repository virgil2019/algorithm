import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

x = 1
g = a
v = 0
w = b

# print(int(g/w), g%w)

while True:
    if w == 0:
        y = (g - a * x) / b
        while True:
            if x > 0:
                break
            x += b
            y -= a

        print("Result", g, x, y)
        break

    q = int(g / w)
    t = g % w
    s = x - q * v
    x = v
    g = w
    v = s
    w = t