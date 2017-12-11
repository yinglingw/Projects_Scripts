This README file is a associated with ProjectionCorrection.py

This script works by copying the projection data taken from the DTM's DTEEC.aux.xml file and creating new JP2.aux.xml files for the associated orthophotos. 

First, we will need to generate the projection data. 
Open ArcMap and load in the DTEEC.IMG file (this is also a good point to load in orthos, too)
Once there, navigate to this file in ArcCatalog
-Right click on the .IMG file
	>"Properties"
		-This will prompt a GUI titled "Raster Set Properties". Make sure you are on the "General" tab.
		-Scroll down to the section that is listed as "Spatial Reference" on the left. It should be in bold
			>"Edit..."   
			-This will bring up a GUI and it will show what coordinate system it is using
				>"OK"  (we aren't actually going to change anything since this projection is the correct one)
		>"Apply"
		>"OK"		

		
Now we have created the necessary .aux.xml file. 
This should be located in the same directory that houses the .IMG file and hopefully your JP2 Orthos exist there, too.
Now completely close ArcMap.


Now make a list in the command prompt (the script will want a text file) of all the JP2 Orthos that you would like to adjust the projections for.
My command of choice is 

$ ls *ORTHO.JP2 > BadOrthos.txt

A change of permissions may also be required for the .py file. In that case execute the following command in the directory it is located in

$ find . -exec chmod 775 {} +; find . -exec chgrp socset {} +----

Now we want to execute the script and it should look something like this. Note: the "python" may or may not be required, depending on your computer set up.

$ python ProjectionCorrection.py DTEEC_036859_2020_036569_2020_A01.IMG.aux.xml BadOrthos.txt

And finally, our JP2.aux.xml's have been created! If the script ran correctly, there be should a handful of successful output lines and there will be a .xml file for every ortho you specified.
And lucky for us, ArcMap is smart enough to correctly identify the .xml files in the images directory 
and apply the correction that the orthos need. 

The last step is to reopen ArcMap and the visually verify the orthos lie ontop of the DTEEC.

*This script is relatively short and simple so there aren't too many safegaurds against things it doesn't expect. 
Make sure the .aux file is the first argument and the .txt is the second one. 
If you have run this script and are still not seeing the correct change to the orthos try remaking the IMG.aux.xml file 
	and delete the incorrect ORTHO.xml files from your directory. Then run this script again.
Also, I have tried this script on a couple CTX images and it failed so that may be something to look into in the future.

Will Yingling
yingling@pirl.lpl.arizona.edu
s


		
