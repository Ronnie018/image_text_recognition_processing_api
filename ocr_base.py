import cv2
import pytesseract
import functions.functions as lf


def preProcessing(fileData, type):
  file = cv2.imread(fileData["path"])

  if file is None:
    return

  roi = lf.cropper(file, type)

  img_grayscale = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  img_binary = lf.binarize(img_grayscale, type)

  lf.showImage(img_grayscale, fileData)
  lf.showImage(img_binary, fileData)

  return img_binary

def image_reader(image):
  
  config = r'-c tessedit char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
  
  pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/Tesseract.exe"
  
  string = pytesseract.image_to_string(image, lang="eng", config=config)
  
  return string

if __name__ == "__main__":
  
  calibrationSet = [
    (0,255),
    (25,255),
    (35,255),
    (45,255),
    (65,255),
  ]

  basePath = "./assets"

  base = lf.fileSetGenerator(basePath)

  for image in base:
    image_results = []
    # processing each image in diferent calibrations
    for calibration in calibrationSet:
      
      final_image = preProcessing(image, image["taskType"])
      result = image_reader(final_image)
      image_results.append(result)
      
    # final = lf.choseBest()
    # print("final: ", final)
    print(image_results)