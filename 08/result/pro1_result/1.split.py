import sys,re,os,string,math

######################
def SPLIT_FILE():
	STOR = {}
	fp=open("Height1000_compare_517_487_common_multiple.csv","r")
	head = fp.readline()
	for line in fp:
		line_temp = string.split(line.strip(),",")
		PER = float(line_temp[2])
		BOUND = int(math.ceil(PER))
		if( not BOUND in STOR ):
			STOR[BOUND] = []
		STOR[BOUND].append(line.strip()) 
	fp.close()

	########################
	NEWSTOR = {}
	hapvalue = [] 
	for i in range(100,70,-1):
		#print i
		hapvalue += STOR[i]	
		NEWSTOR[i] = hapvalue[:] 

		#print len(STOR[i]),len(NEWSTOR[i])

	for i in range(70,40,-5):
		#print i
		if( not i in NEWSTOR ):
			NEWSTOR[i] = []

		if( i in STOR ):
			temp = STOR[i]
		if( i-1 in STOR ):
			temp += STOR[i-1]
		if( i-2 in STOR ):
			temp += STOR[i-2]
		if( i-3 in STOR ):
			temp += STOR[i-3]
		if( i-4 in STOR ):
			temp += STOR[i-4]

		hapvalue += temp

		NEWSTOR[i] = hapvalue[:] 
		#print len(temp),len(NEWSTOR[i]) 

	temp = []
	for i in range(40,16,-1):
		if( i in STOR ):
			temp += STOR[i]

	hapvalue += temp
	NEWSTOR[40] = hapvalue[:]

	print len(hapvalue)

	#temp = []
	for key,value in NEWSTOR.items():
		print key,len(value)
		temp.append(key)
	#print temp

	return NEWSTOR

######################
def WRITE_FILE(NEWSTOR):
	for key, value in NEWSTOR.items():
		fpout=open("split_"+str(key)+".csv","w")
		for r in value:
			fpout.write(r+"\n")
		fpout.close()

######################
# main
######################
NEWSTOR = SPLIT_FILE()
WRITE_FILE(NEWSTOR)
