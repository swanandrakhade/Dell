import numpy as np
import dicom
import os
import datetime
import matplotlib.pyplot as plt
import glob
from collections import defaultdict
import pathlib

def store(imagelist, dir):
	pathlib.Path("/"+dir).mkdir(parents=True, exist_ok=True)
	for i in range(len(imagelist)):
		image=dicom.read_file(imagelist[i])
		image.save_as("/"+dir+"/image"+str(i), write_like_original=True)

def main():

	images= []
	images=glob.glob("**/*.dcm", recursive=True)


	print("scanning function")
	print()
	for i in range(len(images)):

		print(images[i])

	# patient=defaultdict(list)

	# for i in range(len(images)):
	# 	read=dicom.read_file(images[i])
	# 	if (str(read.PatientName) in patient):
	# 		patient[str(read.PatientName)].append(images[i])
	# 	else:
	# 		newlist=[]
			
	# 		newlist.append(images[i])
	# 		patient[str(read.PatientName)]=newlist

	# 	read=[]

	# for key in patient:
	# 	print(key, len(patient[key]))
	# 	print()


	sequencename=defaultdict(list)

	for i in range (len(images)):
		read=dicom.read_file(images[i])
		if (str(read.SeriesDescription) in sequencename):
			sequencename[str(read.SeriesDescription)].append(images[i])
		else:
			newlist=[]
			newlist.append(images[i])
			sequencename[str(read.SeriesDescription)]=newlist

		read=[]
	for key in sequencename:
		print(key, sequencename[key])
		print()

main()