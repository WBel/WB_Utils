
def BuildUI():
    winName = 'CameraAnimationTool'
    winWidth = 400
    winHeight = 130
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.1.0'

    if cmds.window(winName, exists=True):
            cmds.deleteUI(winName)
    window = cmds.window(winName, w = winWidth, h = winHeight, title = 'Camera Animation Tool', menuBar = True, rtf=True, s=False)
    cmds.columnLayout()

#Infos________

    cmds.menu(l = 'Info')

    cmds.menuItem(l = 'Developer', d = True, ld = True)
    cmds.menuItem(l = dev)
    cmds.menuItem(l = 'Join', d = True, ld = True)
    cmds.menuItem(l = mail)
    cmds.menuItem(l = 'Version', d = True, ld = True)
    cmds.menuItem(l = version)

#SET_CAMERA_________________________

    cmds.frameLayout(l = 'Camera', w = winWidth)

    tmpRowWidth = [winWidth*0.20, winWidth*0.80]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Camera name :', w = tmpRowWidth[0], align = 'center', h = 30)
    cmds.textField('name', w = tmpRowWidth[1])

    cmds.setParent('..')

#MOTION_PATH_________________________

    cmds.frameLayout(l = 'Motion path', w = winWidth)

    cmds.radioButtonGrp('mAxis', numberOfRadioButtons = 2, sl = 2, cal = "center", labelArray2=['XY', 'YZ'], w = winWidth)

    cmds.setParent('..')



#_________

    tmpRowWidth = [winWidth*0.20, winWidth*0.80]
    cmds.rowLayout(nc = 2, cw2 = tmpRowWidth)

    cmds.text(l = 'Replace with :', align = 'center', w = tmpRowWidth[0], h = 30)
    cmds.textField('newName', w = tmpRowWidth[1])

    cmds.setParent('..')

    tmpRowWidth = [winWidth]
    cmds.rowLayout(nc = 1, cw1 = tmpRowWidth[0])

    cmds.button('createCamera', l = 'Create Camera', w = tmpRowWidth[0], h = 30, c='do_createCamera()')

    cmds.setParent('..')

    cmds.separator(h = 10, w = winWidth)


    cmds.showWindow()


def do_createCamera():

    name = cmds.textField('name', q=True, tx = True)


    cameraName = cmds.camera(n = name)





mp = 'curve'
CfrontAxis = 'z'
CupAxis = 'y'
startFrame = 0
endFrame = 100




###cmds.pathAnimation(cameraName[0], fa=CfrontAxis, ua=CupAxis, inverseFront = True, stu = startFrame, etu = endFrame, c=mp)

BuildUI()
