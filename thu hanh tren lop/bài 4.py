f = open("TBCINP.txt","r")
x = f.readlines()
n = int(x[0])
a = [int(x[i]) for i in range(1,len(x))]
tb = sum(a)/len(a)
f1 = open("TBCOUT.txt", "w")
f1.write(str(tb))

