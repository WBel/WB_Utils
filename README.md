# WB_Utils v 1.0

*William Bélanger - william@unstandardstudio.com*

Hi there, my name's William. I'm a character artist at Unstandard Studio. Beside from doing characters, I also do rigging. And it's during
a course on mechanical rigging that I went and created this tool. Following Tim Coleman's initial code, and adding my own touch.
Here's the link to is toolkit, which is open source: https://github.com/tccoleman/WB_Utils some of it doesn't work anymore with recent versions of Maya (2023), so that's what I'm trying to fix in my own. Anyway, I'm not your typical programmer, so there might be bugs, but feel free to E-Mail me and I'll try to get back to you and fix those.

##
## Installation
Use one of two ways to download the WB_Utils from GitHub
##### 1) Using GitHub Desktop
- Download and install GitHub Desktop from https://desktop.github.com/
- Launch GitHub Desktop and click on “Clone a Repository from the Internet”
- Click on "URL" tab, put in https://github.com/WBel/WB_Utils as URL
- Choose your "maya/scripts" directory and the local path *Usually in the document folder*
- Click the "Clone" button which will download the toolkit into your maya script directory

##### 2) Downloading zip file from GitHub
- Download the `WB_Utils.zip` file and unzip it.  
- Inside the `WB_Utils` folder that was unzipped, there will be another `WB_Utils` folder.  Copy and paste that folder into your `<USER>/Documents/maya/scripts/` directory.   
- Launch Maya.
- Once in Maya, open the Script Editor and run the following code to see if the toolkit was installed correctly.
#

    import WB_Utils
    WB_Utils.run_test()
You should see a "True" or a installation successful message if it was successful.



##
## Utility Script Library
Contain various Python scripts with functions to aid in the creation of rigs.

You can test if your installation was successful by running the code below to create locators at the selected objects or points.  Select objects or components to create locators at and run the code below in the Maya Script Editor
#### Running utility functions example
    from WB_Utils.utils import locator
    reload(locator)
    locator.selected_points()


##
## Custom Shelf
Custom Maya tool shelf for quick access to often used utility functions and tools.
#### To Load Custom Maya Tool shelf
    from WB_Utils.shelves import shelf_WB_Utils
    reload(shelf_WB_Utils)
    shelf_WB_Utils.load(name="WB_Utils")


#### Automatically load shelf at Maya startup
Add these lines to your `<USER>/Documents/maya/scripts/userSetup.py` file

    import maya.utils

    # Load Mech Rig Custom Shelf at Maya startup
    from WB_Utils.shelves import shelf_WB_Utils

    def load_WB_Utils():
    	shelf_WB_Utils.load(name="WB_Utils")

    maya.utils.executeDeferred("load_WB_Utils()")


##
## Tools
Functions of the WB Utils tools.

### Settings
#### Reload shelf
Reloads shelf.

### Rename tool
Opens popup window to rename selected objects.
Also contains search and replace, and add suffix and prefix functions.

### Group and offset tool
Creates a group and offset transform node on top of selected objects.
Replaces suffix; (Make sure your controllers uses the _ctl or _ctrl suffixes)

### Locator tool
#### Create locator at selected position
Creates locator at the position of all selected objects.

#### Create locator at selected position/rotation
Creates locator at the position and rotation of all selected objects.

#### Create locator at selection center
Creates locator at the center of all selected objects.

### Mirror Joints
Opens popup window to mirror joints. Much like Maya's built in one.

### Mirror Controls
Opens popup window to mirror controls.
