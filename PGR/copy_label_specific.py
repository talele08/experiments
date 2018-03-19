import csv
import os
import shutil
import imghdr

src='/home/aniket/s3/PGR'
csvFilePath='/home/aniket/s3/pgrimagelist.csv'
destination='/home/aniket/s3/images_major'

classlabelByID={'Removal of garbage': 2, 'Pot hole fill up/Repairs to the damage surface': 13, 'Absenteesim of door to door garbage collector': 11, 'Improper Sweeping': 5, 'Broken Bin': 10, 'Stagnation of water': 4, 'Desilting of Drain': 1, 'Absenteesim of sweepers': 8, 'Unsanitary conditions on the road': 12, 'Removal of Debris': 0, 'Over flowing of garbage bins': 6, 'Water pipe leakage': 14, 'Non Burning of Street Lights': 3, 'Disposal of removed silt on the Road': 7, 'Mosquito menace': 15, 'UGD Over Flow': 9}


with open(csvFilePath) as csvfile:
   readCSV=csv.reader(csvfile,delimiter=',')
   labels=[]
   availableMetadata=[]
   imageName=[]
   for row in readCSV:
       name=row[3]
       label=row[1]
       fullpath=os.path.join(src,name)
       if (os.path.isfile(fullpath) and imghdr.what(fullpath)=='jpeg' and (label in classlabelByID)):
           shutil.copy(fullpath,destination)



