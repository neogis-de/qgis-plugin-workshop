A faster buffer selection plugin. Spatial indexing
===================================================

Introduction
*************

In this lesson we will use a spatial index to make the buffer selection plugin faster and more efficient.


Source Code
************

The plugin of this example plugin is available at the ``python/buffer_selection_index`` folder. It is recommended to try yourself to create it following the steps described below, before using the provided plugin code.


Plugin implementation
**********************

If you try to run the buffer selection tool on a layer with a large number of points, it might take a while for the selection to be made. Most likely, the time will be too long to make the tool actually usable. This is because the mechanism that we implemented for computing the features within the specified ratio is far from efficient, since it computes the distance from the center point to each one of the features in the layer.

QGIS vector layers support spatial indexes, that can be used to reduce the number of operations needed for a task like this. We will see how to use them in this lesson.

Starting with the code that we wrote on the previous lesson, we should modify the ``BufferSelectionTool`` class, where the tool logic is implemented. This is the improved code, which makes use of spatial indexes.

::




Creating the spatial index takes time, so we do not create it each time that the tool is called, but only if needed, in case it hasn't been created before, and then we store a reference to it.

We create the index and populate it by adding the features directly from the corresponding layer. Indexes are stores in a dict, using the layer ID as key, so we can later recover them easily.


Once the index is created, whenever the canvas is clicked, instead of computing all distances we let the index do that work and return the list of indexes inside the bounding polygon with a side equal to two times the specified radius (that, is the bounding box of the circle that defines the area that we want to select). Features outside that polygon are guaranteed not to be within the radius distance, so we ignore them. With the remaining ones, we calculate the distances and refine our searh to remove those that are within the rectangle but not within the search radius.

Additional work
****************

Try the following ideas to improve the plugin and get soe extra practice.

- You can pass a circle directly to the index, and get the list of features to select in one step. Notice, however, that there is no function to create a circle, and you have to create it as a polygon. This might cause soe imprecisions if the number or sides of the polygon is not large enough. On the other hand, a larger number of points will result in a a worse performance. Try yourself to implement that mechanism for selecting features.

- If you create a detailed circle, you do not have to rebuild the geometry each time before calling the spatial index. Since the radius of the circle does not change, it is enough to just translate it to the new point where the user has clicked. Search in the QGIS API to know how to translate a geometry.



