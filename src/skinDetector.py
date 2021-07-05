import cv2 
import numpy as np

#  init and use segment()
class skinDetector(object):
	#class constructor
	def __init__(self,it:int):
		self.it = it
		# self.image = img                        
		# # self.image = cv2.resize(self.image,(600,600),cv2.INTER_AREA)	
		# self.HSV_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
		# self.YCbCr_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2YCR_CB)
		# self.binary_mask_image = self.HSV_image

		# threshold
		self.lower_HSV_values = np.array([0, 40, 0], dtype = "uint8");
		self.upper_HSV_values = np.array([25, 255, 255], dtype = "uint8");
		self.lower_YCbCr_values = np.array((0, 138, 67), dtype = "uint8");
		self.upper_YCbCr_values = np.array((255, 173, 133), dtype = "uint8");

	def segment(self,img):
		self.setImage(img);
		return self.find_skin()
	#function to process the image and segment the skin using the HSV and YCbCr colorspaces, followed by the Watershed algorithm
	def setImage(self,img):
		self.image = img                        
		self.HSV_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
		self.YCbCr_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2YCR_CB)
		self.binary_mask_image = self.HSV_image

	def find_skin(self):
		self.__color_segmentation()
		return self.__region_based_segmentation()

	#Apply a threshold to an HSV and YCbCr images, the used values were based on current research papers along with some
	# empirical tests and visual evaluation
	def __color_segmentation(self):
		# lower_HSV_values = np.array([0, 40, 0], dtype = "uint8")
		# upper_HSV_values = np.array([25, 255, 255], dtype = "uint8")

		# lower_YCbCr_values = np.array((0, 138, 67), dtype = "uint8")
		# upper_YCbCr_values = np.array((255, 173, 133), dtype = "uint8")

		#A binary mask is returned. White pixels (255) represent pixels that fall into the upper/lower.
		mask_YCbCr = cv2.inRange(self.YCbCr_image, self.lower_YCbCr_values, self.upper_YCbCr_values)
		mask_HSV = cv2.inRange(self.HSV_image, self.lower_HSV_values, self.upper_HSV_values) 

		self.binary_mask_image = cv2.add(mask_HSV,mask_YCbCr)

	#Function that applies Watershed and morphological operations on the thresholded image
	def __region_based_segmentation(self):
		#morphological operations
		# if(self.it>0):
		image_foreground = cv2.erode(self.binary_mask_image,None,iterations = self.it)     	#remove noise
		dilated_binary_image = cv2.dilate(self.binary_mask_image,None,iterations = self.it)   #The background region is reduced a little because of the dilate operation
		_,image_background = cv2.threshold(dilated_binary_image,1,128,cv2.THRESH_BINARY)  #set all background regions to 128

		image_marker = cv2.add(image_foreground,dilated_binary_image)   #add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.

		image_marker = cv2.add(image_foreground,image_background)   #add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.
		image_marker32 = np.int32(image_marker) #convert to 32SC1 format

		cv2.watershed(self.image,image_marker32)
		m = cv2.convertScaleAbs(image_marker32) #convert back to uint8 

		#bitwise of the mask with the input image
		_,image_mask = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		output2 = cv2.subtract(self.image,np.stack((image_mask,image_mask,image_mask),axis=2))
		# output = output-10;
		# np.
		# output = np.uint8(output)
		output = cv2.bitwise_and(self.image,self.image,mask = image_mask)
		output = cv2.addWeighted(output,1,output2,0.1,0)
		
		#show the images
		# self.show_image(self.image)
		# self.show_image(self.HSV_image)
		# self.show_image(self.YCbCr_image)
		# self.show_image(self.binary_mask_image)
		# self.show_image(image_mask)
		# just silently return
		return output;
		# self.show_image(output)
		# cv2.waitKey(self.delay)