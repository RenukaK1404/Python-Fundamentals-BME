class pat():
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print("Name:",name,"id",id,"age:",age)
    def checkvital(self, hr):
        self.hr=hr
        if hr>80:
            print("abnmormal hr")
        else:
            print("normal")
pat(908,"Renuka",19)
pat(896,"eureka",89)