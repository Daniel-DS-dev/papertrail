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
image = cv2.imread("data/sample/img/X00016469612.jpg")
#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows

#Turn image to document
doc = DocumentFile.from_images("data/sample//img/X00016469612.jpg")
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
    seen = set()
    output = []
    for block in json_response["pages"][0]["blocks"]:
        for line in block["lines"]:
            for word in line["words"]:
                value = word["value"]
                bbox = [coord for point in word["geometry"][:2] for coord in point]
                key = (value, tuple(bbox))
                if key not in seen:
                    seen.add(key)
                    output.append((value, bbox))
    return output


output = extract_all_values(json_response)
for i in range (0, len(output)):
   print(output[i])
   


#Visualize the result.
print('MODEL IMAGE: \n')
result.show()