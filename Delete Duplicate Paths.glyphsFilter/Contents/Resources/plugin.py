# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class DeleteDuplicatePaths(FilterWithoutDialog):
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Delete Duplicate Paths',
			'de': u'Doppelte Pfade löschen',
		})
		self.keyboardShortcut = None # With Cmd+Shift
	
	def streamlinedPathDict(self, path):
		pathdict = dict(path.pathDict())
		nodelist = []
		for node in pathdict["nodes"]:
			node = str(node).replace(" SMOOTH","") # we do not care if green or blue
			nodelist.append(node)
		pathdict["nodes"] = tuple(nodelist) 
		return pathdict
	
	def filter(self, layer, inEditView, customParameters):
		pathcount = len(layer.paths)
		if pathcount > 1:
			
			# count backwards, so we do not mess up the path index numbers:
			for i in range(pathcount)[::-1]: 
				if i > 0:
					currpath = layer.paths[i]
					currpathdict = self.streamlinedPathDict(currpath)
					shoulddeletecurrpath = False
					
					# count backwards, so we do not mess up the path index numbers:
					for j in range(i)[::-1]: 
						otherpath = layer.paths[j]
						otherpathdict = self.streamlinedPathDict(otherpath)
						if currpathdict == otherpathdict:
							shoulddeletecurrpath = True
					
					# delete if duplicate has been found:
					if shoulddeletecurrpath:
						del layer.paths[i]
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	