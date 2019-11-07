with open("C:\\Users\\biopop\\Desktop\\exercise\\02\\year.txt", "r") as f:
    year = ""
    line = f.readlines()
    lines = str(line)
    lines = lines.replace("\\n", "")
    year += lines
    years = year.split(',')
    a_list = []
    for word in years:
        word = word.replace("'", "")
        word = word.replace("[", "")
        word = word.replace("]", "")
        a_list.append(word)
    a_dic = {}
    key,value = "",""
    for i in range(len(a_list)):
        if i % 2 == 0:
            key = a_list[i].strip()
        else:
            value = a_list[i]
        a_dic[key] = value
#    print(a_dic)

with open("C:\\Users\\biopop\\Desktop\\exercise\\02\\C_nt.fas", "r") as f:
    lines = f.readlines()
    b_dic = {}
    key, value = "",""
    for i in range(len(lines)):
        if i % 6 == 0:
            line = str(lines[i])
            line = line.replace("\n", "")
            key = line.strip()
            key = key.replace("\n", "")
        elif i % 6 == 1:
            value = lines[i]
            b_dic[lines[i-1]] = value
        elif i % 6 == 2:
            value = lines[i]
            b_dic[lines[i-2]] += value
        elif i % 6 == 3:
            value = lines[i]
            b_dic[lines[i-3]] += value
        elif i % 6 == 4:
            value = lines[i]
            b_dic[lines[i-4]] += value
        elif i % 6 == 5:
            value = lines[i]
            b_dic[lines[i-5]] += value
#        print(b_dic)

headers_list2 = {}
b_nkey = ""
for b_key in b_dic.keys():
    for a_key in a_dic.keys():
        if a_key in b_key:
            b_nkey = b_key.replace("\n", "")
            b_nkey += "."
            b_nkey += a_dic[a_key]
            headers_list2[b_nkey] = b_dic[b_key]
        else:
            pass
#print(headers_list2)

with open("C:\\Users\\biopop\\Desktop\\exercise\\02\\headers.list2", "w") as f:
    for c_key in headers_list2:
        f.write(c_key)
        f.write("\n")
        f.write(headers_list2[c_key])

        # f.write("%s\n%s" %(c_key, headers_list2[c_key]))
       
    










#for key in list(a_dic.keys()):
#    b_key = list(b_dic.keys())
#    n = b_key.index(">" + key + "\n")
#    nkey = b_key[n]
#    for k in nkey:
#        k.replace("\n", "")
#        k += "."
#        k += a_dic[key]

#print(k)
