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
#    print(miR)
with open("C:\\Users\\biopop\\Desktop\\exercise\\04\\exist_miRNA_list.txt", "w") as f:
    miRNA_list = ""
    for h in miR:
        h = h.replace("\"", "")
        miRNA_list += h
        miRNA_list += "\n"
    f.write(miRNA_list)
