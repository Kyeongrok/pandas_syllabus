import sys,re,os,string,glob

#####################
def SUB_MAKE_PHYLIP(fname,TOT_NAME_SEQ,TOT_NAME_LIST):
        temp=os.path.splitext(fname)
        basename=os.path.basename(fname)
        nameonly=os.path.splitext(basename)

        firstname = TOT_NAME_LIST[0]
        totlen = len(TOT_NAME_SEQ[firstname])

        fpout=open(nameonly[0]+".phy","w")
        fpout.write(" "+str(len(TOT_NAME_LIST))+" "+str(totlen)+"\n")

	start = 0
        for i in range(0,totlen,50):
               	for name in TOT_NAME_LIST:
			if( start == 0 ):
               			fpout.write("%-12s"%name)
			else:
               			fpout.write("%-12s"%' ')

			for j in range(i,i+50,10):
				fpout.write(" %-10s"%TOT_NAME_SEQ[name][j:j+10])
			fpout.write("\n")
		fpout.write("\n")
		start = 1
        fpout.close()

        return totlen

#####################
def MAKE_PHYLIP(fname):
        temp=os.path.splitext(fname)
        basename=os.path.basename(fname)
        nameonly=os.path.splitext(basename)

        fp=open(fname,"r")
        start = 0
        TOTLEN = 0
        for line in fp:
                if( line.startswith('dimensions') ):
                        line = line.strip()
                        line_temp = string.split(line[:-1])
                        for value in line_temp:
                                if( value.startswith('nchar=') ):
                                        temp = string.split(value,"=")
                                        TOTLEN = int(temp[1])
                elif( line.startswith('matrix') ):
                        start = 1
                        NAME_SEQ = {}
                        NAME_LIST = []
                elif( line.startswith(';') ):
                        start = 0

                elif( start == 1 and len(line.strip()) > 0  ):
                        line_temp = string.split(line.strip())
                        if( not line_temp[0] in NAME_LIST ):
                                NAME_LIST.append(line_temp[0])
                                NAME_SEQ[line_temp[0]] = line_temp[1]
                        else:
                                NAME_SEQ[line_temp[0]] += line_temp[1]
        fp.close()

        SUB_MAKE_PHYLIP(fname,NAME_SEQ,NAME_LIST)
######################
# main
######################
MAKE_PHYLIP("bmp10p-e.nxs")
