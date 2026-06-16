files=[
"patient1_CT.dcm",
"patient7_MRI.dcm",
"patient2_CT.dcm",
"patient8_CT.dcm",
"patient9_MRI.dcm",
"patient56_CT.dcm",
"notes.txt"
]
import re
ct=[]
for j in files:
    if re.findall("CT",j):
        ct.append(j)
print(ct)
mri=[]
for j in files:
    if re.findall("MRI",j):
        mri.append(j)
print(mri)