from paddleocr import PaddleOCR
import json

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
# need to run only once to download and load model into memory
ocr = PaddleOCR(lang="en")

#load image into paddle ocr
image_path = "data/sample//img/X00016469612.jpg"

def run_paddle_ocr(image_path):
    result = ocr.predict(image_path)
    
    #result including text, bounding boxes (recognition), and scores
    output = []
    for index in range (0, len(result[0]["rec_texts"])):
        characters = result[0]["rec_texts"][index]
        bounding_box_coordinates = result[0]["rec_boxes"][index].tolist()
        recognition_scores = result[0]["rec_scores"][index]

        output.append((characters, bounding_box_coordinates, recognition_scores))

    return output

char_details = run_paddle_ocr(image_path)
print(char_details[0])