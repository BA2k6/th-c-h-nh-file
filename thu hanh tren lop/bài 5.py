with open("TBCINP2.txt", "r") as f:
    x = f.readlines()
    n =x[0]
    tb=[]
    for i in range(int(n)):
        a = [int(j) for j in (x[i+1]).split() ]
        tb.append(sum(a)/len(a))
with open ("TBCOUT2.txt", "w") as f1:
    f1.write("\n".join(map(str,tb)))


