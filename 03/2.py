with open("C:\\Users\\biopop\\Desktop\\exercise\\03\\order.txt", "r") as f:
    #lines = f.readlines()
    HID_Age_dic = {}
    order_list = []
    over50_HID = []
    f.readline()
    for line in f:
        order_list.append(line.split())
#    print(order_list)
    for each_list in order_list:
        key = each_list[1]
        value = each_list[4]
        HID_Age_dic[key] = value
    for (HID, age) in HID_Age_dic.items():
        age = int(age)
        if age>=50:
            #print(1)
            over50_HID.append(HID)
        else:
            #print(2)
            pass
#    print(over50_HID)


with open("C:\\Users\\biopop\\Desktop\\exercise\\03\\order.txt", "r") as f:
    order_50more = ""
    order_50more += f.readline()
    for line in f:
        for HID in over50_HID:
            if HID in line:
                order_50more += line
            else:
                pass
#    print(order_50more)

with open("C:\\Users\\biopop\\Desktop\\exercise\\03\\order_50more.txt", "w") as f:
    f.write(order_50more)










    
#    over50_HID = [HID for (HID, age) in HID_Age_dic.items() if int(age) >= 50]

   




        
#    print(HID_Age_dic)
#    for key in HID_Age_dic.keys():
#        if key == int:
#            if int(key) >= 50:
#                over50_HID.append(HID_Age_dic[key])
#            else:
#                pass
#        else:
#            pass
#    print(over50_HID)
