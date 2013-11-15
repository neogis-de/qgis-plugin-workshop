Introduction
=============

This manual describes how to create plugins to extend the functionality of QGIS. 

It contains a set of example plugins of increasing complexity, designed to introduce the most important elements of the QGIS API and the tehcniques and methods most commonly used for developing plugins. The steps to crete each plugin are described in detail. Source code for each plugin is also provided and fully commented, so it can  be used as a reference.

Prerequisites
-------------

This manual assumes that you are familiar with the Python programming language. Python syntax is not covered in this manual.

Basic knowledge of QGIS is also assumed. You do not need to know QGIS in great detail, but you should at least be familiar with its main elements and its main concepts. Knowledge of QGIS internals is not necessary, as it will be covered in this text.

To use this manual, you will need the following sotware installed in your system

- QGIS 2.0.1. It can be downloaded from the `QGIS website <http://qgis.org>`_
- A Text editor or Python IDE. Pick up your favorite one. PyDev and PyCharm are popular IDE's among QGIS developers. To know how to prepare your environment for working with QGIS classes, you can find more information `here <http://www.qgis.org/en/docs/pyqgis_developer_cookbook/ide_debugging.html>`_
- GNU make. If you are using a Windows machine, you can install it from `here <http://gnuwin32.sourceforge.net/packages/make.htm>`
- QtDesigner. You have to download and install the `QT library installer <http://qt-project.org/downloads>`_. We will be using Qt Designer that is installed with it, to create dialogs for our plugins.
- *Plugin Builder* and *Plugin Reloader* plugins. Two plugins that we will use to siplify some tasks. In case you are not familiar with plugin installation, it will be covered briefly once we create our first plugin, so you can move on without installing this plugins if you do not know how to do it.

Additional documentation
------------------------

This manual does not cover all possible cases that you might find when writing your own plugins. It should teach you the main ideas and the classes and methods that will be enough to create your plugin in most cases, but some more advanced plugins might need additional elements not covered in this text. However, there is plenty of good documentation about QGIS and the libraries used by QGIS, which you should use when you need more detailed information. The following are the documents that you should always keep handy.

- `The QGIS API <http://qgis.org/api/>`_. It describes all the internal elements of QGIS. Not all classes and methods are exposed through the Python API, but most are. Make sure you check the documentation corresponding to the classes that are introduced in the examples of this manual, since they are not fully described in here, but they contain almost all the functionality that is needed for creating any type of plugin.

- `The PyQt documentation <http://pyqt.sourceforge.net/Docs/PyQt4/classes.html>`_. PyQt is used for creating the GUI elements of a QGIS plugin. Knowledge of PyQt is not assumed, but this manual includes just some basic ideas about PyQt. To know more about how to create more advanced interfaces and the classes and methods available for ech class, you should check the PyQt documentation

- Example plugins. Apart from the plugins that are described in detail in the lessons of this manual, there is an acoompanying set of plugins that you can use as a reference. Some of them been created specifically to be used for learning, while others are adapted from real plugins. All of them have a heavily commented source code, and all superfluous code has been removed, so you should be able to check them to get insight about a given functionality that the plugin implements. You will find a description of those extra plugin in the XXXXXXX appendix.



