import numpy as np
import dicom
import os
import datetime
import matplotlib.pyplot as plt
import glob
from collections import defaultdict
import pathlib
import time


def store(imagelist, dir):
  pathlib.Path("../" + dir).mkdir(parents=True, exist_ok=True)
  for i in range(len(imagelist)):
    print(imagelist[i])
    image = dicom.read_file(imagelist[i])
    image.save_as("../" + dir + "/image" + str(i)+".dcm", write_like_original=True)

# scan and save according to patient name
def scanPatientName():
  images = []
  images = glob.glob("**/*.dcm", recursive=True)
  
  print("scanning function, patient name")
  print()
  
  patient=defaultdict(list)
  
  for i in range(len(images)):
    read=dicom.read_file(images[i])
    if (str(read.PatientName) in patient):
      patient[str(read.PatientName)].append(images[i])
    else:
      newlist=[]
      newlist.append(images[i])
      patient[str(read.PatientName)]=newlist
  return patient

#scan and save according to series description
def scanSeriesDescription():
  
  print("scanning function, series description")
  images = []
  images = glob.glob("**/*.dcm", recursive=True)
  sequencename = defaultdict(list)
  
  for i in range(len(images)):
    read = dicom.read_file(images[i])
    if (str(read.SeriesDescription) in sequencename):
      sequencename[str(read.SeriesDescription)].append(images[i])
    else:
      newlist = []
      newlist.append(images[i])
      sequencename[str(read.SeriesDescription)] = newlist
  
  return sequencename
  
def main():
  startTime = time.time()
  
  
  images = []
  images = glob.glob("**/*.dcm", recursive=True)
  
  print("scanning function")
  print()
  # for i in range(len(images)):
  #   print(images[i])
  
  #scan and save according to patient name
  
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
  
  # #scan and store according to series description
  # sequencename = defaultdict(list)
  #
  # for i in range(len(images)):
  #   read = dicom.read_file(images[i])
  #   if (str(read.SeriesDescription) in sequencename):
  #     sequencename[str(read.SeriesDescription)].append(images[i])
  #   else:
  #     newlist = []
  #     newlist.append(images[i])
  #     sequencename[str(read.SeriesDescription)] = newlist
  #
  #   read = []
  # for key in sequencename:
  #   print(key, len(sequencename[key]))
  #   print()
  seq=scanSeriesDescription()
  # store(seq["Resolution Insert"], "copiedimages")
  print(len(seq))
  print(seq.keys())
  
  pat=scanPatientName()
  print(len(pat))
  print(pat.keys())

  print('The script took {0} second !'.format(time.time() - startTime))
  
  

main()
