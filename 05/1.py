with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\05\\chr21.hg19.mm9.net.axt", "r") as f:
    a_list = []
    b_list = []
    c_list = []
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for line in f:
        lin = line[0]
        if lin.isdigit() == True:
            a_list.append(line)
        else:
            pass
#        for n in range(1, 19568):
#            m = str(n)
#            if line.startswith(m):
#                a_list.append(line)
#    print(a_list)
    for a in a_list:
        b_list.append(a.split())
#    print(b_list)
    for b in b_list:
        c_list.append(b[2])
    zero = []
    one = []
    two = []
    three = []
    four = []
    for c in c_list:
        if 0 <= int(c) < 10000000:
            zero.append(c)
        elif 10000000 <= int(c) < 20000000:
            one.append(c)
        elif 20000000 <= int(c) < 30000000:
            two.append(c)
        elif 30000000 <= int(c) < 40000000:
            three.append(c)
        else:
            four.append(c)
#    print(len(zero))

with open("C:\\Users\\BIOPOP_SOJIN\\Desktop\\exercise\\05\\result.txt", "w") as f:
    f.write("0 <= X < 10000000, ")
    f.write(str(len(zero)))
    f.write("\n")
    f.write("10000000 <= X < 20000000, ")
    f.write(str(len(one)))
    f.write("\n")
    f.write("20000000 <= X < 30000000, ")
    f.write(str(len(two)))
    f.write("\n")
    f.write("30000000 <= X < 40000000, ")
    f.write(str(len(three)))
    f.write("\n")
    f.write("40000000 <= X < 50000000, ")
    f.write(str(len(four)))
