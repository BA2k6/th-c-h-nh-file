f = open("DaysoINP.txt", "r")
x = f.readline().strip()
n = list(map(int, f.readline().split()))
a = [i for i in n if i %2 == 0]
f1 = open("DaysoOUT.txt", "w")
for i in a:
    f1.write(f'{i} ')
f.close()
f1.close()



