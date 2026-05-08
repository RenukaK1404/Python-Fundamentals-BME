ac=list(map(int,input("Enter accelerometer values: ").split()))
l=len(ac)
for i in range(l):
    if ac[i]>=2:
        print("possible fall detected at ", i,"secs")