a = int(input())
b = int(input())
corr = ((2 * a - 1) // (a + b) + (2 * b - 1) // (a + b) + 1) % 2
minimum = (((a % b) // a) * a + ((b % a) // b) * b + corr * a)
maximum = (a + b) - minimum
print(maximum)
