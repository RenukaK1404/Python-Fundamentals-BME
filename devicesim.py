class medicaldevice():
    def start(self):
        print("Device is starting")
class ecg(medicaldevice):
    def start(self):
        super().start()
        print("ECG is recording")
class mri(medicaldevice):
    def start(self):
        super().start()
        print("MRI is scanning")
e=ecg()
e.start()
m=mri()
m.start()