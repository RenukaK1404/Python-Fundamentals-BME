g=list(map(int,input("Enter steps").split()))
l=len(g)
total=0
for i in range(l):
    total+= g[i]
avg = total/l
print("Total steps=", total)
print("Average steps=", avg)
if avg<4000:
    print("sedentary")
elif avg>=4000 and avg<=8000:
    print("Normal")
else:
    print("Very active")
ma=max(g)
mn=min(g)
print("Maximum steps=", ma)
print("Minimum steps=",mn)