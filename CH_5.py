import numpy as np
import cv2

# Weil die Kamera des Roboters nicht funktioniert hat. Wir haben versucht, ein einfaches Beispiel für das distanzmessen hochzuladen
# und zwar das distanz zwischen der Kamera und einem scharfen Objekt von einem Bild (in diesem Beispiel ist es ein  Papier)
# Wir konnten den Code nicht auf dem Roboter ausführen, da  wir die CV bibliothek nicht importieren und installieren  konnten

def find_marker(image):
	# convertieren das Bild to grayscale,(blur it) and edges finden
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

  
  	#  die contours finden  und die grßeste behalten
	# wir nehmen an dass unsere okect in dem bild ist
	(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# distanz zwischen maker und objekt rechnen un züruckgeben
	return (knownWidth * focalLength) / perWidth

# echte distanz zwischen kamera und das objekt
# in dem fall ist 13 cm(the number is virtual weil wir kein foto von dem Roboterscamera machen konnten)
KNOWN_DISTANCE = 13.0

# echte breite des objektes
# paper is 5 cm wide((the number is virtual weil wir kein foto von dem Roboterscamera machen konnten))
KNOWN_WIDTH = 5.0

# Bilder die wir nutzen werden
#(das imagepath is virtuell weil wir kein foto von dem Roboterscamera machen konnten )
IMAGE_PATHS = ["images/1.png", "images/1.png", "images/3.png"]


#  focal length bestimmen
image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH


for imagePath in IMAGE_PATHS:
	# Bild laden,Marker finden und dann distanz rechnen zwischen marker und das camera 
	image = cv2.imread(imagePath)
	marker = find_marker(image)
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

	# bounding box um das Bild zecihnen and es zeigen 
	box = np.int0(cv2.cv.BoxPoints(marker))
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fft" % (inches / 12),
		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
	cv2.imshow("image", image)
	cv2.waitKey(0)