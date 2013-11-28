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
        index = self.indices.setdefault(currentLayer.id(), self.createIndex(currentLayer))        
        toSelect = []
        pt = self.toLayerCoordinates(currentLayer, e.pos())   
        ptGeom = QgsGeometry.fromPoint(pt)            
        rect = 
        features = index.intersects(rect)
        for id in features:
          feature = currentLayer.getFeatures(QgsFeatureRequest(id))[0]
          geom = feature.geometry()
          distance = geom.distance(ptGeom)      			
          if distance < self.distance:
            toSelect.append(feature.id())
        currentLayer.setSelectedFeatures(toSelect)
    

