from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class BufferSelectionMapTool(QgsMapToolEmitPoint):
  def __init__(self, canvas, distance = 1):
      	self.canvas = canvas      
      	self.distance = 1
      	QgsMapToolEmitPoint.__init__(self, self.canvas)        
      
  def canvasPressEvent(self, e):  		
    	currentLayer = self.canvas.currentLayer()
      	if currentLayer.type() == QgsMapLayer.VectorLayer:
      		toSelect = []
      		pt = self.toLayerCoordinates(currentLayer, e.pos()) 
      		ptGeom = QgsGeometry.fromPoint(pt)    
      		features = currentLayer.getFeatures()
      		for feature in features:
      			geom = feature.geometry()
      			distance = geom.distance(ptGeom)      			
      			if distance < self.distance:
      				toSelect.append(feature.id())

      		currentLayer.setSelectedFeatures(toSelect)
    
