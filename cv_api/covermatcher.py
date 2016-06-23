mport numpy as np
import cv2
class CoverMatcher:
	def __init__(self, descriptor, coverpaths):

		self.descriptor = descriptor
		self.coverPaths = coverPaths

	def search(self, querykps, queryDescs):
		results = {}

		for coverPath in self.coverPaths:
			cover = cv2.imread(coverPath)
			gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
			(kps, descs)=self.descriptor.describe(gray)
			score = self.match(querykps, queryDescs, kps, descs)
			results[coverPath] = score
		if len(results) > 0:
			results = sorted([v, k) for (k, v) in
			 results.items() if v > 0],
					reverse = True)
		return results

