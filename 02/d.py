with open("C:\\Users\\biopop\\Desktop\\exercise\\02\\C_nt.fas", "r") as f:
    lines = f.readlines()
    header = []
    for i in range(len(lines)):
        if i % 6 == 0:
            line = lines[i]
            header.append(line[1:])
        else:
            pass

#for a_header in header:
#    print(a_header, end="")

with open("headers.list", "w") as f:
    for a_header in header:
        print(a_header, file=f, end="")
