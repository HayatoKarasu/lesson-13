import random

def matrix():
    sp = []
    for i in range(n):
        sp.append([])
        for a in range(m):
            sp[i].append(random.randrange(-100,100))
    return sp


def matrix0():
    for i in range(n):
        sp2.append([0]*m)


sp0 = []
sp1 = []
sp2 = []

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

print("Получим матрицу 1")
sp0 = matrix()
for row in sp0:
    print(*row)
    
print("Получим матрицу 2")
sp1 = matrix()
for row in sp1:
    print(*row)

matrix0() #нулевая матрица

print("Складываем эти две матрицы!")

for r in range(len(sp0)):
    for b in range(len(sp0[0])):
        sp2[r][b] = sp0[r][b] + sp1[r][b]
        
for row in sp2:
    print(*row)
