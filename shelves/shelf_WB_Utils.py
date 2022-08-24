"""
    Creates rigging_toolkit Maya shelf

    To use, run these Python commands in Maya:

        from rigging_toolkit.shelves import shelf_rigging_toolkit
        reload(shelf_rigging_toolkit)
        shelf_rigging_toolkit.load(name="Rigging_Toolkit")

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
from rigging_toolkit.shelves import shelf_base
reload(shelf_base)

from rigging_toolkit.utils import transforms
reload(transforms)

# Import maya modules
from maya import cmds


# GLOBAL script variables referred to throughout this script
ICON_DIR = os.path.join(os.path.dirname(__file__), 'shelf_rigging_toolkit_icons')
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), 'shelf_rigging_toolkit_scripts')
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
        from rigging_toolkit.shelves import shelf_base
        reload(shelf_base)

        from rigging_toolkit.shelves import shelf_rigging_toolkit
        reload(shelf_rigging_toolkit)


        shelf_rigging_toolkit.load('Rigging_Toolkit')

        LOG.info("Successfully reloaded {} shelf".format('Rigging_Toolkit'))
        return True
    except:
        LOG.error("Error reloading shelf")
        return

class load(shelf_base._shelf):

    def build(self):

        # Reload shelf button
        self.addButton(label="", ann='Reload shelf', icon=ICON_DIR + "/reloadShelf.png", command= "from rigging_toolkit.shelves import shelf_rigging_toolkit; "
                                                                                "maya.utils.executeDeferred('shelf_rigging_toolkit.reload_shelf()')")


        # Separator
        self.addSeparator()


        # Group Offset button
        self.addButton(label="", ann='Add transform offset and group to selected objects', icon=ICON_DIR + "/grpOffset.png", command= 'from rigging_toolkit.utils import transforms;'
                                                                            'reload(transforms);'
                                                                            'transforms.add_transform()')
