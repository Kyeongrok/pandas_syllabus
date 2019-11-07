with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\06\\PRO1\\myid.list", "r") as f:
    a_list = []
    b_list = []
    c_list = []
    for line in f:
        a_list.append(line.split())
#    print(a_list)
    for a in a_list:
        b_list.append(a[0])

with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\06\\PRO1\\my_table.txt", "r") as f:
    line = f.readline()
    c_list = []
    for b in b_list:
        c_list.append(line.find(b))
#    print(c_list)


with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\06\\PRO1\\my_table.txt", "r") as f:
    d_list = []
    for line in f:
        d_list.append(line.split())
#print(d_list)
    
#with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\06\\PRO1\\My_table.txt", "w") as f:
    
