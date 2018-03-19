import csv
import os
import shutil
import imghdr

src='/home/aniket/PGR'
csvFilePath='/home/aniket/s3/appgrimage.csv'
destination='/home/aniket/s3/exp2/Images_png'

with open(csvFilePath) as csvfile:
   readCSV=csv.reader(csvfile,delimiter=',')
   availableMetadata=[]
   for row in readCSV:
       availableMetadata.append(row[3])

allFiles=os.listdir(src)

for file in availableMetadata:
   fullpath=os.path.join(src,file)
   if (os.path.isfile(fullpath) and imghdr.what(fullpath)=='jpeg'):
      shutil.copy(fullpath,destination)

    
