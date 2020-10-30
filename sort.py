import random
a = [i for i in range(10)]
random.shuffle(a)
print(a)
for i in range(10):
    min = 10
    for j in range(i, 10):
        if a[j]<=min:
            min = a[j]
    a.remove(min)
    a = a[:i] + [min] + a[i:]
print(a)