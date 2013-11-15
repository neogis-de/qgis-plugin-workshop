Using QSetting to remember previously used parameters
======================================================

Introduction
*************

In this lesson we will improve the random layer plugin by adding the capability to save the parameters used in its last execution, and restoring those parameters when the plugin is run again. We will see how to use the ``QSettings`` class to do that that, and we will discuss some useful QGIS settings that are available.


Source Code
************

The plugin of this example plugin is available at the ``python/random_layer_settings`` folder. It is recommended to try yourself to create it following the steps described below, before using the provided plugin code.


Plugin implementation
**********************************

Qt provides an easy way of storing settings, so they can be persisted from one session to another. We will see how to use that to store the parameters that are entered by the user, and recover them later. Also, we will use the same Qt feature to get the default encoding for layers and use it when writing our random layer. QGIS also uses Qt to store its settings, so they can be accesed in the same way that we will access the specific setting of our plugin.


The first thing to change is the ``accept()`` method in the dialog class, so it saves the entered values before closing the dialog. Here is the code of the method.

::

	def accept(self):
		self.filepath = self.txtFilepath.text()
		authid = self.txtCrs.text()
		self.crs = QgsCoordinateReferenceSystem(authid)
		if not self.crs.isValid():
			self.setYellowBackground(self.txtCrs)
			return
		try:
			self.npoints = int(self.txtNPoints.text())
		except ValueError:
			self.setYellowBackground(self.txtNPoints)
			return
		if self.npoints < 1:
			self.setYellowBackground(self.txtNPoints)
			return

		self.ok = True	

		settings = QSettings()
		settings.setValue('/RandomLayerPlugin/crs', self.txtCrs.text())
		settings.setValue('/RandomLayerPlugin/npoints', self.txtNPoints.text())
		settings.setValue('/RandomLayerPlugin/filepath', self.txtFilepath.text())

		QDialog.accept(self)    

You should construct the path that identify your setting, including the name of the plugin and the name of the setting, to avoid problems with settings used by other plugins or QGIS itself. You can add more depth to the path if you need to. All settings are stored as text, and will be recovered as such.

Now we can use the settings that we have stored, by getting the and using them as the default values for the corresponding text boxes when the dialog is opened. This has to be added to the dialog constructor, which will now look like this.

::

	class RandomLayerPluginDialog(QtGui.QDialog):

	    def __init__(self):
	        QtGui.QDialog.__init__(self)
	        # Set up the user interface from Designer.
	        self.ui = Ui_RandomLayerPlugin()
	        self.ui.setupUi(self)
	        self.ok = False
	        settings = QSettings()
	        self.txtCrs.setText(settings.value('/RandomLayerPlugin/crs', ""))
	        self.txtNPoints.setText(settings.value('/RandomLayerPlugin/npoints', ""))
	        self.txtFilepath.setText(settings.value('/RandomLayerPlugin/filepath', ""))

Apart from reading our own setting, we can read settings stored by QGIS. One of these settings is the default encoding to use when writing files. If you remember, the vector writer was created with the following line:

::

	writer = QgsVectorFileWriter(filepath, "CP1252", fields, QGis.WKBPoint, crs, "ESRI Shapefile")

The encoding is hardcoded. Instead of that, you can use the default encoding set by QGIS, replacing the above with these lines.

::

	encoding = QSettings.value('/UI/encoding', 'System')
	writer = QgsVectorFileWriter(filepath, encoding, fields, QGis.WKBPoint, crs, "ESRI Shapefile")

If no encoding is set, the call to the ``value()`` method will return ``'System'`` as default value, which will cause QGIS to use the default system encoding.



