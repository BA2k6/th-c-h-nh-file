f = open("UOCINO.txt", "r")
x = f.readline().strip()
a = []
for i in range(1, int(x)+1) :
      a.append(str(i))
f1 = open("UOCOUT.txt ", "w")
f1.write(" ".join(a))
f.close()
f1.close()



