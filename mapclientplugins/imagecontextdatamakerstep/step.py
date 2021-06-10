"""
MAP Client Plugin Step
"""
import re
import json
import imagesize

from PySide2 import QtGui

from opencmiss.zinc.context import Context
# from opencmiss.utils.zinc import create_finite_element_field, create_square_2d_finite_element, \
#     create_volume_image_field, create_material_using_image_field
from opencmiss.utils.zinc.field import create_field_finite_element, create_field_volume_image
from opencmiss.utils.zinc.material import create_material_using_image_field
from opencmiss.utils.zinc.finiteelement import create_square_element

from opencmiss.utils.zinc.widgets.basesceneviewerwidget import BaseSceneviewerWidget

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.imagecontextdatamakerstep.configuredialog import ConfigureDialog


def try_int(s):
    try:
        return int(s)
    except ValueError:
        return s


def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [try_int(c) for c in re.split('([0-9]+)', s)]


class ImageContextData(object):

    def __init__(self, context, frames_per_second, image_file_names, image_dimensions):
        self._context = context
        self._shareable_widget = BaseSceneviewerWidget()
        self._shareable_widget.set_context(context)
        self._frames_per_second = frames_per_second
        self._image_file_names = image_file_names
        self._image_dimensions = image_dimensions

    def get_context(self):
        return self._context

    def get_shareable_open_gl_widget(self):
        return self._shareable_widget

    def get_frames_per_second(self):
        return self._frames_per_second

    def get_frame_count(self):
        return len(self._image_file_names)

    def get_image_file_names(self):
        return self._image_file_names

    def get_image_dimensions(self):
        return self._image_dimensions


class ImageContextDataMakerStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(ImageContextDataMakerStep, self).__init__('Image Context Data Maker', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Utility'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/imagecontextdatamakerstep/images/utility.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#image_context_data'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#2d_image_dimension'))
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#image_context_data
        self._portData1 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#images
        self._portData2 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#2d_image_dimension
        # Config:
        self._config = {'identifier': '', 'frames_per_second': 30}

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        context = Context('images')
        region = create_model(context)
        image_file_names = self._portData1.image_files()
        frames_per_second = self._config['frames_per_second']
        image_dimensions, _ = _load_images(image_file_names, frames_per_second, region)
        image_context_data = ImageContextData(context, frames_per_second, image_file_names, image_dimensions)
        self._portData0 = image_context_data
        self._portData2 = image_dimensions
        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        self._portData1 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#images

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        port_data = self._portData0  # image_context_data
        if index == 2:
            port_data = self._portData2  # 2d_image_dimension

        return port_data

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


def create_model(context):
    default_region = context.getDefaultRegion()
    region = default_region.createChild('images')
    #coordinate_field = create_finite_element_field(region)
    coordinate_field = create_field_finite_element(region)
    field_module = region.getFieldmodule()
    scale_field = field_module.createFieldConstant([2, 3, 1])
    scale_field.setName('scale')
    duration_field = field_module.createFieldConstant(1.0)
    duration_field.setManaged(True)
    duration_field.setName('duration')
    offset_field = field_module.createFieldConstant([+0.5, +0.5, 0.0])
    scaled_coordinate_field = field_module.createFieldMultiply(scale_field, coordinate_field)
    scaled_coordinate_field = field_module.createFieldAdd(scaled_coordinate_field, offset_field)
    scaled_coordinate_field.setManaged(True)
    scaled_coordinate_field.setName('scaled_coordinates')
    # create_square_2d_finite_element(field_module, coordinate_field,
    #                                 [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]])
    create_square_element(field_module, coordinate_field,
                                    [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]])

    return region


def _load_images(images, frames_per_second, region):
    field_module = region.getFieldmodule()
    frame_count = len(images)
    image_dimensions = [0, 0]
    image_based_material = None
    if frame_count > 0:
        # Assume all images have the same dimensions.
        width, height = imagesize.get(images[0])
        if width != -1 or height != -1:
            cache = field_module.createFieldcache()
            scale_field = field_module.findFieldByName('scale')
            scale_field.assignReal(cache, [width, height, 1.0])
            duration = frame_count / frames_per_second
            duration_field = field_module.findFieldByName('duration')
            duration_field.assignReal(cache, duration)
            image_dimensions = [width, height]
        #image_field = create_volume_image_field(field_module, images)
        image_field = create_field_volume_image(field_module, images)
        image_based_material = create_material_using_image_field(region, image_field)
        image_based_material.setName('images')
        image_based_material.setManaged(True)

    return image_dimensions, image_based_material
