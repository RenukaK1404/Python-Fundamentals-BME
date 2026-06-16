ecg_device = {
"sampling_rate":500,
"gain":2,
"filter":"lowpass",
"channel":3
}
def updateval(para,newv):
    print("changed ",para)
    print(ecg_device[para]," to ",newv)
    ecg_device[para]=newv
    print(ecg_device)
def delval(para):
    ecg_device.pop(para)
    print("Deleted: ",para)
    print(ecg_device)
def printk():
    for k,v in ecg_device.items():
        print(k,v)
updateval("gain",5)
delval("channel")
printk()
