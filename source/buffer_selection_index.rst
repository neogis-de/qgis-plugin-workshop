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


Once the index is created, when the canvas is clicked, instead of computing all distances, we let the idex do that work and return the list of indexes  

