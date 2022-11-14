import cv2
import os


def cropper(image, type):
  
  # height, width, number of channels in image
  y = getShapesForType(image.shape[0], type)
  x = getShapesForType(image.shape[1], type)
  
  # channels = image.shape[2]
  
  newCrop = image[y[0]:y[1], x[0]:x[1]]
  
  return newCrop
  
def getShapesForType(shape, type):
  if type == "A2Z":
      return (5, shape - 5)
    
  else: return (0, shape)

def showImage(image, fileData):
  print(fileData)
  cv2.imshow("final yet", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
def getPrefix(fileName, delim, pos):
  return fileName.split(delim)[pos]

def binarize(img_grayscale, taskType):
  print(taskType)
  
  black = 0 if taskType == "A2Z" else 140
  white = 120 if taskType == "A2Z" else 255
  
  print("tax =", black)
  
  _, img_binary = cv2.threshold(img_grayscale, 195, 255, cv2.THRESH_BINARY)

  return img_binary

def fileSetGenerator(path):
  fileSet = []
  for fileName in os.listdir(path):
    fileData = {
        "taskType": getPrefix(fileName, "-", 0).upper(),
        "variation": getPrefix(fileName, "_", 1),
        "path": path + "/" + fileName
      }
    fileSet.append(fileData)
  return fileSet
