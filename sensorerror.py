def checkread(val):
    try:
        if val<0 or val>250:
            raise Exception
        else:
            print(val,"ok")
    except Exception as e:
        print("INVALID SENSOR READING!!!")
checkread(45)
checkread(500)
checkread(89)
checkread(876)
checkread(-85)
checkread(8)

