import cv2
import numpy as np
class CoverDescriptor:
	def __init__(self, kpMethod = "SIFT" , descMethod="SIFT"):
		self.kpMethod = kpMethod
		self.descMethod = descMethod

	def describe(self, image):
		detector = cv2.FeatureDetector_create(self.kpMethod)
		kps = detector.detect(image)

		extractor = cv2.DescriptorExtractor_create(self.descMethod)

		(kps, descs) = extractor.compute(image, kps)
		kps = np.float32([kp.pt for kp in kps])
		return (kps, descs)
