from doctr.io import DocumentFile
from doctr.models import ocr_predictor


#for image preprocessing
import cv2
import numpy as np
import torch
import re
import time

#creating an instance of the model
model  = ocr_predictor("db_mobilenet_v3_large", "crnn_mobilenet_v3_large", pretrained=True)

#preview the image
image = cv2.imread("data\sample\img\X00016469612.jpg")
#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows

#Turn image to document
doc = DocumentFile.from_images("data\sample\img\X00016469612.jpg")
result = model(doc)

#Visualize the result.
#print('MODEL IMAGE: \n')
#result.show()

#export the result:
json_response = result.export()
print(json_response)

print("\n")
print("="*200)
print("\n")

#Function for getting texts and bounding boxes
def extract_all_values(json_response):
    all_vals_geometry_unclean = []
    for i in range(0, len(json_response['pages'][0]['blocks'])):
      for j in range(0, len(json_response['pages'][0]['blocks'][i]['lines'])):
        for k in range(0, len(json_response['pages'][0]['blocks'][i]['lines'][j]['words'])):

          #collect all values in the receipt and their upper range(geometry).
          bounding_box = []
          valus = json_response['pages'][0]['blocks'][i]['lines'][j]['words'][k]['value']
          for a in range(0, 2):
              for b in range (0, 2):
                  bounding_box.append(json_response['pages'][0]['blocks'][i]['lines'][j]['words'][k]['geometry'][a][b])
          all_vals_geometry_unclean.append((valus, bounding_box))

    #remove duplicates
    all_vals_geometry = []
    for v in all_vals_geometry_unclean:
      if v not in all_vals_geometry:
        all_vals_geometry.append(v)

    return all_vals_geometry


output = extract_all_values(json_response)
for i in range (0, len(output)):
   print(output[i])
   


#Visualize the result.
print('MODEL IMAGE: \n')
result.show()