f=open("C://Users//renuk//OneDrive//Desktop//may'26//p_ecg.txt","r")
data=f.readlines()
print(data)
l=[]
for i in data:
    i=i.strip()
    i=float(i)
    l.append(i)
print(l)
s=0
max=0
for i in range(0,len(l)):
    s+=i
    
avg=s/len(l)
print("Average value:",avg)
peak=l[0]
t=0
for i in range(0,len(l)):
    if l[i]>peak:
        peak=l[i]
        t=i+1
print("Maximum peak of",peak,"at",t,"secs",)
f.close()