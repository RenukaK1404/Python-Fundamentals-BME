ecg=list(map(int,input().split()))
l=len(ecg)
for i in range(l):
    if ecg[i]>150:
        print("Abnormal at", (i+1), "secs")