import dicom

def main():
  ds=dicom.read_file("image-000001.dcm")

  ds[0x10, 0x10].value = 'Testname1'
  print(ds)
  print()
  print(ds.PatientsName)
main()