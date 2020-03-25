import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b ** 2 - 4 * a * c
x_1 = int((-b + d ** 0.5)/(2 * a))
x_2 = int((-b - d ** 0.5)/(2 * a))
print(x_2)
print(x_1)