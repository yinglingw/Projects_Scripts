#!/usr/bin/env python
# this script is to change the projection of your .JP2 ortho image to the correct projection which is given by .IMG FILE
# input in the command line should be 
#     ProjectionCorrection.py  DTEECfilename.IMG.aux.xml listofJP2orthos.txt
#

import sys

#this block reads in the two command line arguments
IMGaux = sys.argv[1]
print("\n\nThe file to be copied from is " + IMGaux + "\n")

JP2name  = sys.argv[2]
print("\nThe text file of JP2s to be adjusted is " + JP2name)

#this block reads the files
x = open(sys.argv[1],'rU')
ProjectionData = x.readlines()

RasterBand = """<PAMRasterBand band="1">"""
RasterBandEnd = """</PAMRasterBand>"""
LBLinfo =  """</Metadata>"""


#this block is going to take a edited dteec file and then trim it down to only the necessary info
counter = 0

for w in range(len(ProjectionData)):
	#finds the up to the end of the label info (including actual projection)
	# the counter is for finding only the first /Metadata, since there are multiple in a typical file
	if str(ProjectionData[w]).strip() == LBLinfo:
		if counter >= 1:
			pass
		else:
			LBLend = w+1
			counter = counter + 1
			
	#finds the beginning and end of the block of Rasterband data we want		
	elif str(ProjectionData[w]).strip() == RasterBand:
		Begin = w
	elif str(ProjectionData[w]).strip() == RasterBandEnd:
		End = w
		
#puts the label info (with projection) and only necessary rasterband data into a new list which is to become our file		
CorrectProjectionData = ProjectionData[:LBLend] + ProjectionData[Begin:Begin+2] + ProjectionData[End:]


JP2name = open(sys.argv[2], 'rU')
filenames = JP2name.readlines()

#this loop removes the "\n" from the end of the .txt file at each line
print "\n\nThe given file names are\n"
for k in range(len(filenames)):
	filenames[k] = filenames[k].strip("\n")
	print filenames[k] 
print"\n\n"

#this is where the magic happens
for i in range(len(filenames)):
	#creates a new name where .aux.xml is appended to the Ortho.JP2
	NewAuxXml = filenames[i] + ".aux.xml"
	
	#creates the a new file with the name we just made
	CreateAuxXml = open(NewAuxXml, 'w+')
	print NewAuxXml, "was created"
	
	#writes info from the DTEEC file into our new file
	for j in range(len(CorrectProjectionData)):
		CreateAuxXml.write(CorrectProjectionData[j])
	print NewAuxXml, "has been successfully written to"
	
	#safely closes our file
	CreateAuxXml.close()		
	print NewAuxXml, "has been closed\n\n"

#end of the code and print successful message	
print "All files have been successfully created!"

# September 2015
# Made by Will Yingling with the assitance of Kenny Fine
# And thanks to Matt Chojnacki and Anna Urso for testing it
# yingling@pirl.lpl.arizona.edu