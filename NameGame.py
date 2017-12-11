#!/usr/bin/env python

import sys

DataFileName  = sys.argv[1]
print("\nThe text file of data to be copied from is " + DataFileName + "\n")


#this block reads the files
x = open(sys.argv[1],'rU')
filenames = x.readlines()


#just listing the files
print "Reading files"
for g in range(len(filenames)):
	print filenames[g]

	#creating name of new txt file
NewTxtFile = "CanISeeYourIDsPlease.txt"

#opening a new file with the new name
WritingToFile = open(NewTxtFile, 'w+')
print "\n\n", NewTxtFile, "was created", "\n\n"

for NumberOfNames in range(len(filenames)):
	#cleaning up the names in the given text file
	ReadingData = open(filenames[NumberOfNames].strip(), 'rU')
	InternalData = ReadingData.readlines()
	print "Currently in file", filenames[NumberOfNames].strip()
	
	#now going into a specific file
	for NumberOfLines in range(len(InternalData)):
	#fist line has lots of good data like name and id
		if NumberOfLines == 0:
			#separating by directories
			FirstLine =  InternalData[NumberOfLines].split("/")
			
			#looping over each dir name
			for w in range(len(FirstLine)):
				DirectoryName = str(FirstLine[w])
				
				#the site id is usually listed after this dir. could break here in the future
				#possibly another solution could be readin in the ROI info
				if DirectoryName == "RSL_DTMs":
					SiteID = FirstLine[w+1].split("_")
					SiteID = SiteID[0]
					
				#DTM id is usually last in the file path
				if w == len(FirstLine)-1:
					DTMID = FirstLine[w].split("_Sl")
					DTMID = DTMID[0]
					
		#fourth line has necessary data			
		if NumberOfLines == 4:
			Values = InternalData[NumberOfLines].split()
			Values.pop(0) #remove the word band
			Values.pop(0) #remove Stats

			
			#finding the data. from inside out.
			#convert strip the elemnt in Values, then convert to a number, then round the values to the tenths place 
			Min = round(float(Values[0].strip()), 1)
			Max = round(float(Values[1].strip()), 1)
			Mean = round(float(Values[2].strip()), 1)
			STDEV = round(float(Values[3].strip()), 1)

			MAS = [str(Mean), "+/-", str(STDEV)]
			MeanAndSTDEV = "".join(MAS)
			
			AllTogetherNow = [str(SiteID), "\t", str(DTMID), "\t", str(Min), "\t", str(Max), "\t", MeanAndSTDEV, "\n"]
			AllTogetherNow = "".join(AllTogetherNow)
			
			print "Writing In", AllTogetherNow
			WritingToFile.write(AllTogetherNow)
			
WritingToFile.close()
print "File has been created with success"
print "###Program is done running###"			
