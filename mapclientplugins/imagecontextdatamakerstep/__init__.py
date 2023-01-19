"""
MAP Client Plugin
"""

__version__ = '0.1.1'
__author__ = 'Hugh Sorby'
__stepname__ = 'Image Context Data Maker'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.imagecontextdatamaker/archive/master.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.imagecontextdatamakerstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
