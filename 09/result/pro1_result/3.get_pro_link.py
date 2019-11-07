import sys,re,os,string

###################
def MAKE_MATRIX(taxid):	
	ENSPLIST = []
	fp=open("ensplist_"+taxid+".list","r")
	for line in fp:
		line_temp = string.split(line.strip())
		ENSPLIST.append(line_temp[0])	
	fp.close()

	#################
	PAIR = {}
	fp=open("link_"+taxid+".list","r")
	for line in fp:
		line_temp = string.split(line)
		temp = string.split(line_temp[0],".")
		if( not temp[1] in PAIR ):
			PAIR[temp[1]] = {}

		temp2 = string.split(line_temp[1],".")
		PAIR[temp[1]][temp2[1]] = line_temp[2]
	fp.close()
	###############


	fpout=open("mymatrix_"+taxid+".table","w")
	wlist = ['enspname'] + ENSPLIST
	wstr = ",".join(wlist)
	fpout.write(wstr+"\n")
	for ensp in ENSPLIST:
		#PAIR = {}
		#fp=open("link_"+taxid+".list","r")
		#for line in fp:
		#	line_temp = string.split(line)
		#	temp = string.split(line_temp[0],".")
		#	if( temp[1] == ensp ):
		#		temp2 = string.split(line_temp[1],".")
		#		PAIR[temp2[1]] = line_temp[2]
		#fp.close()
		
		CURPAIR = PAIR[ensp]

		wlist = [ensp]
		for wtemp in ENSPLIST:
			value = "0.0"
			if( wtemp == ensp ):
				value = "1.0"
			elif( wtemp in CURPAIR ):
				value = "%.3f" % (float(CURPAIR[wtemp])/1000)
			wlist.append(value)
		wstr = ",".join(wlist)
		fpout.write(wstr+"\n")
	fpout.close()
	 
###################
# main
###################
MAKE_MATRIX("sub")
