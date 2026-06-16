patients = [
    {
        "id":101,
        "name":"Arun",
        "HR":110,
        "SpO2":92,
        "BP":150
    },
    {
        "id":102,
        "name":"Meena",
        "HR":75,
        "SpO2":98,
        "BP":120
    }
]
def cal_risk(patients):
    for i in range(len(patients)):
        print("Patient ID:",patients[i]["id"])
        print("Patient name:",patients[i]["name"])
        if patients[i]["HR"]>72:
            print("High heart Rate")
        if patients[i]["SpO2"]<98:
            print("low SpO2")
        if patients[i]["BP"]>=120 or patients[i]["BP"]<=80:
            print("abnormal BP")
        print()
cal_risk(patients)
