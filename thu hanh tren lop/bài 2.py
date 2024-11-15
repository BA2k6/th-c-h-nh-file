f = open("DaySoINP2.txt", "r")
x = f.readline().strip()
n = list(map(int, f.readline().split()))
t = 0
for i in n :
      if int(i) % 3 == 0:
        t+=i
f1 = open("DaySoOUT2.txt", "w")
f1.write(str(t))
f.close()
f1.close()