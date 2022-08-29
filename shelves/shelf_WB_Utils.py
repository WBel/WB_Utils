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

from WB_Utils.utils import generalTools
reload(generalTools)

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
        from WB_Utils.shelves import shelf_base
        reload(shelf_base)

        from WB_Utils.shelves import shelf_WB_Utils
        reload(shelf_WB_Utils)


        shelf_WB_Utils.load('WB_Utils')

        LOG.info("Successfully reloaded {} shelf".format('WB_Utils'))
        return True
    except:
        LOG.error("Error reloading shelf")
        return

class load(shelf_base._shelf):

    def build(self):

        # Reload shelf button
        self.addButton(label="", ann='Reload shelf', icon=ICON_DIR + "/reloadShelf.png", command= "from WB_Utils.shelves import shelf_WB_Utils; "
                                                                        "maya.utils.executeDeferred('shelf_WB_Utils.reload_shelf()')")

        # Common tools

        # Separator
        self.addSeparator()

        self.addButton(label="", ann='General tools.', icon=ICON_DIR + "/rename.png")
        general_tools_menu = cmds.popupMenu(b=1)

        self.addMenuItemDivider(general_tools_menu, divider=True, dividerLabel='CHANGE UI COLOR...')

        self.addMenuItem(general_tools_menu, 'Select UI color', command= 'from WB_Utils.utils import generalTools;'
                                                                            'reload(generalTools);'
                                                                            'generalTools.buildColorUI()')



        # Renaming tool
        self.addButton(label="", ann='Opens popup window to rename objects.', icon=ICON_DIR + "/rename.png", command= 'from WB_Utils.utils import rename;'
                                                                            'reload(rename);'
                                                                            'rename.BuildUI()')


        # Rigging Tools

        # Separator
        self.addSeparator()


        # Group Offset button
        self.addButton(label="", ann='Add transform offset and group to selected objects.', icon=ICON_DIR + "/grpOffset.png", command= 'from WB_Utils.utils import transforms;'
                                                                            'reload(transforms);'
                                                                            'transforms.add_transform()')

        # Locator button
        self.addButton(label="", ann='Create locators based on selection.', icon=ICON_DIR + "/locator.png")
        locator_tool_menu = cmds.popupMenu(b=1)

        self.addMenuItemDivider(locator_tool_menu, divider=True, dividerLabel='CREATE LOCATORS...')

        self.addMenuItem(locator_tool_menu, 'Creates locator at selected position', command= 'from WB_Utils.utils import locator;'
                                                                            'reload(locator);'
                                                                            'locator.loc_atSelectedPos()')

        self.addMenuItem(locator_tool_menu, 'Creates locator at selected position/rotation', command= 'from WB_Utils.utils import locator;'
                                                                            'reload(locator);'
                                                                            'locator.loc_atSelectedPosRot()')

        # Mirror joints button
        self.addButton(label="", ann='Opens popup window to mirror joints.', icon=ICON_DIR + "/grpOffset.png", command= 'from WB_Utils.utils import joints;'
                                                                            'reload(joints);'
                                                                            'joints.BuildUI()')
