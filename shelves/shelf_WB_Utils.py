"""
    Creates WB_Utils Maya shelf

    To use, run these Python commands in Maya:

        from WB_Utils.shelves import shelf_WB_Utils
        reload(shelf_WB_Utils)
        shelf_WB_Utils.load(name="WB_Utils")

"""


# Logging module is used to print output to user
import logging
LOG = logging.getLogger(__name__)


# Import python modules used in this script
from importlib import reload
import os
import sys
import subprocess


# Inherit shelf base class module whose functions we "override" to build our user_toolkit shelf
from WB_Utils.shelves import shelf_base
reload(shelf_base)

from WB_Utils.utils import transforms
reload(transforms)

from WB_Utils.utils import rename
reload(rename)

from WB_Utils.utils import locator
reload(locator)

from WB_Utils.utils import joints
reload(joints)


from WB_Utils.utils import controls
reload(controls)

# Import maya modules
from maya import cmds


# GLOBAL script variables referred to throughout this script
ICON_DIR = os.path.join(os.path.dirname(__file__), 'shelf_WB_Utils_icons')
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'shelf_WB_Utils_scripts')
PLATFORM = sys.platform

sys.path.append(SCRIPTS_DIR)


def explore_maya_project():
    """Opens explorer window to current Maya project location"""
    proj_dir = cmds.workspace(rd=True, q=True)
    subprocess.Popen(r'explorer /select,"{}scenes"'.format(proj_dir.replace("/", "\\")))
    LOG.info('Exploring to %s'.format(proj_dir))


def reload_shelf():
    """Reloads shelf"""
    try:

        cmds.evalDeferred('shelf_WB_Utils.load(name="WB_Utils")')

        LOG.info("Successfully reloaded {} shelf".format('WB_Utils'))
        return True
    except:
        LOG.error("Error reloading shelf")
        return

def reload_studioShelf():
    """Reloads shelf"""
    result = cmds.promptDialog(
        title='Version',
        message='Enter Licence:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        licenceName = cmds.promptDialog(query=True, text=True)
        if licenceName == 'Unstandard':

            try:

                cmds.evalDeferred('shelf_WB_Utils.load(name="WB_Utils", version = "Unstandard")')

                LOG.info("Successfully reloaded {} shelf".format('WB_Utils'))
                return True
            except:
                LOG.error("Error reloading shelf")
                return
        else:
            LOG.error("Non valid licence number, reloading default shelf.")
            try:
                from WB_Utils.shelves import shelf_base
                reload(shelf_base)

                from WB_Utils.shelves import shelf_WB_Utils
                reload(shelf_WB_Utils)


                shelf_WB_Utils.load('WB_Utils', version = licenceName)

                LOG.info("Successfully reloaded {} shelf".format('WB_Utils'))
                return True
            except:
                LOG.error("Error reloading shelf")
                return

class load(shelf_base._shelf):

    def build(self):


        # Settings
        self.addButton(label="", ann='Settings', icon=ICON_DIR + "/settings.png")
        settings_menu = cmds.popupMenu(b=1)

        self.addMenuItemDivider(settings_menu, divider=True, dividerLabel='CREATE LOCATORS...')

        self.addMenuItem(settings_menu, 'Reload shelf', command= 'from WB_Utils.shelves import shelf_WB_Utils;'
                                                                            'reload(shelf_WB_Utils);'
                                                                            'shelf_WB_Utils.reload_shelf()')

        self.addMenuItem(settings_menu, 'Reload Studio Shelf...', command= 'from WB_Utils.shelves import shelf_WB_Utils;'
                                                                            'reload(shelf_WB_Utils);'
                                                                            'shelf_WB_Utils.reload_studioShelf()')
        # Common tools

        # Separator
        self.addSeparator()







        # Renaming tool
        self.addButton(label="", ann='Opens popup window to rename objects', icon=ICON_DIR + "/rename.png", command= 'from WB_Utils.utils import rename;'
                                                                            'reload(rename);'
                                                                            'rename.BuildUI()')

        # Colouring Tool
        self.addButton(label="", ann='Opens popup window to color objects', icon=ICON_DIR + "/color.png", command= 'from WB_Utils.utils import colorChange;'
                                                                            'reload(colorChange);'
                                                                            'colorChange.BuildUI()')

        # Rigging Tools

        # Separator
        self.addSeparator()

        # Attributes Button
        self.addButton(label="", ann='Attributes modifier tool', icon=ICON_DIR + "/attr.png")
        locator_tool_menu = cmds.popupMenu(b=1)

        self.addMenuItem(locator_tool_menu, 'Creates visibility switch (Select rig top node)', command= 'from WB_Utils.utils import attributes;'
                                                                            'reload(attributes);'
                                                                            'attributes.do_createCategoryUi()')

        self.addMenuItem(locator_tool_menu, 'Lock all attributes channels on selected', command= 'from WB_Utils.utils import attributes;'
                                                                            'reload(attributes);'
                                                                            'attributes.do_LockUnlockAttr(lock = True)')

        self.addMenuItem(locator_tool_menu, 'Unlock all attributes channels on selected', command= 'from WB_Utils.utils import attributes;'
                                                                            'reload(attributes);'
                                                                            'attributes.do_LockUnlockAttr(lock = False)')


        # Group Offset button
        self.addButton(label="", ann='Add transform offset and group to selected objects', icon=ICON_DIR + "/grpOffset.png", command= 'from WB_Utils.utils import transforms;'
                                                                            'reload(transforms);'
                                                                            'transforms.add_transform()')


        # Locator button
        self.addButton(label="", ann='Create locators based on selection', icon=ICON_DIR + "/locator.png")
        locator_tool_menu = cmds.popupMenu(b=1)

        self.addMenuItemDivider(locator_tool_menu, divider=True, dividerLabel='CREATE LOCATORS...')

        self.addMenuItem(locator_tool_menu, 'Creates locator at selected position', command= 'from WB_Utils.utils import locator;'
                                                                            'reload(locator);'
                                                                            'locator.loc_atSelectedPos()')

        self.addMenuItem(locator_tool_menu, 'Creates locator at selected position/rotation', command= 'from WB_Utils.utils import locator;'
                                                                            'reload(locator);'
                                                                            'locator.loc_atSelectedPosRot()')

        self.addMenuItem(locator_tool_menu, 'Creates locator at center of selection', command= 'from WB_Utils.utils import locator;'
                                                                            'reload(locator);'
                                                                            'locator.loc_atSelectedCenter()')
        # Mirror joints button
        self.addButton(label="", ann='Opens popup window to mirror joints', icon=ICON_DIR + "/mirrorJoints.png", command= 'from WB_Utils.utils import joints;'
                                                                            'reload(joints);'
                                                                            'joints.BuildUI()')

        # Mirror Controls
        self.addButton(label="", ann='Mirror controls', icon=ICON_DIR + "/mirrorCtl.png", command= 'from WB_Utils.utils import controls;'
                                                                            'reload(controls);'
                                                                            'controls.BuildUI()')


        # Vray tools

        # Separator
        if self.version == 'Unstandard':

            self.addSeparator()

        # Vray object settings
            self.addButton(label="", ann='Vray object settings', icon=ICON_DIR + "/vray.png", command= 'from WB_Utils.utils import vrayUtils;'
                                                                            'reload(vrayUtils);'
                                                                            'vrayUtils.BuildUI()')
