a = input()[::-1]
b = input()[::-1]
op = "<"
if int(a) == int(b):
    op = "="
elif int(a) > int(b):
    b, a = a, b

print(a[::-1], op, b[::-1])
