import sys,re,os,string,glob

#############################
def MAKE_INDEX():
	flist = glob.glob("/disk3/triples/4.NEWSA/0.DATA/*.faa")
	for fname in flist:
		PRONAME = []
		fp=open(fname,"r")
		for line in fp:
			if( line[0] == '>' ):
				line_temp = string.split(line)
				NAME = line_temp[0][1:]
				PRONAME.append(NAME)
		fp.close()

		NUCNAME = []
		temp = os.path.splitext(fname)
		fp=open(temp[0]+".ffn","r")
		for line in fp:
			if( line[0] == '>' ):
				line_temp = string.split(line)
				NAME = line_temp[0][1:]
				NUCNAME.append(NAME)
		fp.close()

		temp = os.path.basename(fname)
		temp1 = os.path.splitext(temp)
		fpout=open(temp1[0]+".index","w")
		for i in range(len(PRONAME)):
			fpout.write(PRONAME[i]+"\t"+NUCNAME[i]+"\n")
		fpout.close()

#############################
def READ_INDEX():
	ALLNAME = {}
	flist = glob.glob("INDEX/*.index")
	for fname in flist:
		temp = os.path.splitext(fname)
		temp1 = string.split(temp[0],"_")
		ID = "_".join(temp1[-2:])
		ALLNAME[ID] = {}
		fp=open(fname,"r")
		for line in fp:
			line_temp = string.split(line)
			ALLNAME[ID][line_temp[1]] = line_temp[0]
		fp.close()	

	return ALLNAME
#############################
def NUC_TO_PRO():
	ALLNAME = READ_INDEX()
	fpout=open("NCTC8325_NC_007795.blastn.newpara.convert","w")
	fp=open("NCTC8325_NC_007795.blastn.newpara","r")
	for line in fp:
		line_temp = string.split(line)
		idtemp = string.split(line_temp[0],"|")	
		id = "|".join(idtemp[1:])
		ID = ALLNAME['NC_007795'][id]

		mlist = string.split(line_temp[1],",")	
		plist = []
		for mid in mlist:
			temp_mid = string.split(mid,"|")
			tempsp = string.split(temp_mid[2],".")
			sp = tempsp[0]
			mymid = "|".join(temp_mid[1:])
			proid = ALLNAME[sp][mymid]
			plist.append(proid)
		fpout.write(ID+"\t"+",".join(plist)+"\n")
	fp.close()
	fpout.close()
#############################
def PRO_TO_NEWPRO():
	fpout=open("NCTC8325_NC_007795.blastp.newpara.convert","w")
	fp=open("../1.PROTEIN/NCTC8325_NC_007795.blastp.newpara","r")
	for line in fp:
		line_temp = string.split(line)
		tempid = string.split(line_temp[0],"|")
		ID = "|".join(tempid[1:])
		ID = ID[1:]

		mlist = string.split(line_temp[1],",")
		plist = []
		for mid in mlist:
			temp_mid = string.split(mid,"|")
			mymid = "|".join(temp_mid[1:])
			plist.append(mymid)

		fpout.write(ID+"\t"+",".join(plist)+"\n")
	fp.close() 
	fpout.close()
	
#############################
def COMPARE():
	MYPRO = {}
	fp=open("NCTC8325_NC_007795.blastp.newpara.convert","r")
	for line in fp:
		line_temp = string.split(line)
		MYPRO[line_temp[0]] = string.split(line_temp[1],",")
	fp.close()

	MYCONNUC = {}
	fp=open("NCTC8325_NC_007795.blastn.newpara.convert","r")
	for line in fp:
		line_temp = string.split(line)
		MYCONNUC[line_temp[0]] = string.split(line_temp[1],",")
	fp.close()

	print len(MYPRO)
	print len(MYCONNUC)

	fpout_same=open("same.list","w")
	fpout_onlynuc=open("onlynuc.list","w")
	fpout_notsame=open("notsame.list","w")
	for key,value in MYCONNUC.items():
		if( key in MYPRO ):
			if( value.sort() == MYPRO[key].sort() ):
				fpout_same.write(key+"\t"+",".join(value)+"\n")
			else:
				fpout_notsame.write(key+"\t"+",".join(value)+"\n")
		else:
			fpout_onlynuc.write(key+"\t"+",".join(value)+"\n")
	fpout_onlypro=open("onlypro.list","w")
	for key,value in MYPRO.items():
		if( not key in MYCONNUC ):
			fpout_onlypro.write(key+"\t"+",".join(value)+"\n")
	fpout_onlypro.close()

	fpout_same.close()
	fpout_onlynuc.close()
	fpout_notsame.close()
		
#############################
# main
#############################
#MAKE_INDEX()

NUC_TO_PRO()

#PRO_TO_NEWPRO()
COMPARE()
