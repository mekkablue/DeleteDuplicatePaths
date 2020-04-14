# encoding: utf-8
from __future__ import division, print_function, unicode_literals

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
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Delete Duplicate Paths',
			'de': u'Doppelte Pfade löschen',
			'es': u'Borrar trazados duplicados',
			'fr': u'Supprimer doubles tracés',
		})
		self.keyboardShortcut = None # With Cmd+Shift
	
	@objc.python_method
	def streamlinedPathDict(self, path):
		try:
			# GLYPHS 3
			pathDict = path.propertyListValueFormat_(3)
			for node in pathDict["nodes"]:
				if "conn" in node:
					del node["conn"]
			return pathDict
		except:
			# GLYPHS 2
			pathDict = dict(path.pathDict())
			nodeList = []
			for node in pathDict["nodes"]:
				node = str(node).replace(" SMOOTH","") # we do not care if green or blue
				nodeList.append(node)
			pathDict["nodes"] = tuple(nodeList) 
			return pathDict
	
	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		try:
			# GLYPHS 3
			pathCount = len(layer.shapes)
		except:
			# GLYPHS 2
			pathCount = len(layer.paths)
		
		if pathCount > 1:
			
			# count backwards, so we do not mess up the path index numbers:
			for i in reversed(range(pathCount)):
				if i > 0:
					try:
						# GLYPHS 3
						currPath = layer.shapes[i]
					except:
						# GLYPHS 2
						currPath = layer.paths[i]
					
					if type(currPath) is GSPath:
						currPathDict = self.streamlinedPathDict(currPath)
						shouldDeletecurrPath = False
					
						# count backwards, so we do not mess up the path index numbers:
						for j in reversed(range(i)): 
							try:
								# GLYPHS 3
								otherPath = layer.shapes[j]
							except:
								# GLYPHS 2
								otherPath = layer.paths[j]
						
							otherPathDict = self.streamlinedPathDict(otherPath)
							if currPathDict == otherPathDict:
								shouldDeletecurrPath = True
					
						# delete if duplicate has been found:
						if shouldDeletecurrPath:
							try:
								# GLYPHS 3
								del layer.shapes[i]
							except:
								# GLYPHS 2
								del layer.paths[i]
						
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	