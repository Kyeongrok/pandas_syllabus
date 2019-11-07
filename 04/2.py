with open("C:\\Users\\biopop\\Desktop\\exercise\\04\\cancer_miRNA_list.txt", "r") as f:
    order = []
    hsa = []
    for line in f:
        order.append(line.split())
#    print(order)
    for a in order:
        for b in a:
            if "-" in b:
                hsa.append(b)
            else:
                pass
#    print(hsa)

#with open("C:\\Users\\biopop\\Desktop\\exercise\\04\\unc.edu_TCGA_H-miRNA_8x15Kv2.2.adf", "r") as f:
#    b = []
#    d = []
#    m = []
#    a += f.readline()
#    for line in f:
#        b.append(line.split())
#        for c in b:
#            d.append(c[8].split("|"))
#        print(d)
#        for e in d:
#            miRNA = e[0].replace("\"", "")
#            print(miRNA)
#            for miR in hsa:
#                if miR in miRNA:
#                    print(d.index(e))
#                    m.append(d.index(e))
#                else:
#                    print(2)
#                    pass
#    print(m)
#    print(miRNA)
#    print(d)

#with open("C:\\Users\\biopop\\Desktop\\exercise\\04\\unc.edu_TCGA_H-miRNA_8x15Kv2.2.adf", "r") as f:
#    a= ""
#    for i, line in enumerate(f):
#        for o in m:
#            if o == i:
#                a += line
#            else:
#                pass
#    print(a)
        
with open("C:\\Users\\biopop\\Desktop\\exercise\\04\\unc.edu_TCGA_H-miRNA_8x15Kv2.2.adf", "r") as f:
    a_list = []
    composite = []
    hsa_list = []
    premiRNA = []
    miRNA = []
    miR = []
    for line in f:
        a_list.append(line.split())
#    print(a_list)
#a는 여기서 각 줄. 그니까 몇번째 a인지 = 몇번째 라인인지
    for a in a_list:
        composite.append(a[8])
#    print(composite)
    for b in composite:
        if "hsa" in b:
            hsa_list.append(b)
        else:
            pass
#    print(hsa_list)
    for c in hsa_list:
        premiRNA.append(c.split(","))
    for d in premiRNA:
        for e in d:
            miRNA.append(e.split("|"))
#    print(miRNA)
    for f in miRNA:
        for g in f:
            if "hsa" in g:
                miR.append(g)
    print(miR)
#    for miRNA in hsa:
#        if miRNA in miR:
            
