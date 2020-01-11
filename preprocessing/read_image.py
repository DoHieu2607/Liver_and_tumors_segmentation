import matplotlib.pyplot as plt
import pydicom as dicom
import numpy as np
from glob import glob
import pylab as pl
import os
import pandas as pd
from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

INPUT_FOLDER = "../data/MRI0003/phase1/"
patients = os.listdir(INPUT_FOLDER)
patients.sort()

lstFileDCM = []
def load_scan2(path):
    for dirName, subdirList,  fileList in os.walk(path):
        for filename in fileList:
            if ".dcm" in filename.lower():
                lstFileDCM.append(os.path.join(dirName,filename))
                # print(lstFileDCM)
    return lstFileDCM

first_patient = load_scan2(INPUT_FOLDER)
# print(first_patient)

#Get ref file
RefDs= dicom.read_file(lstFileDCM[0])

# Load dimensions based on the number of rows, columns, and slices (along the z axis )
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFileDCM))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]),float(RefDs.PixelSpacing[1]),
                    float(RefDs.SliceThickness))

x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])

ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

#loop through all the dicom files
for filenameDCM in lstFileDCM:
    #read the file
    ds = dicom.read_file(filenameDCM)
    #store the raw image data 
    ArrayDicom[:,:, lstFileDCM.index(filenameDCM)] = ds.pixel_array
    
# plt.figure(dpi=1600)
# plt.axes().set_aspect('equal','datalim')
# plt.set_cmap(plt.gray())
# plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, 55]))
# plt.imshow(ArrayDicom[:,:,24],aspect='equal',cmap=plt.gray())
# plt.show()
# for i in range(20,30,1):
#     plt.imshow(ArrayDicom[:,:,i],aspect='equal',cmap=plt.gray())
#     plt.show()
dsexp = dicom.read_file("../data/MRI0001/phase1/img0001.dcm")
print("Ds1: \n",dsexp,"\n")
dsexp2 = dicom.read_file("../data/golden/mri028/fm28.dcm")
print("Ds2: \n",dsexp2)