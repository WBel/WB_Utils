from maya import cmds

import logging


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)



def loc_atSelectedPos():
    """Locator created at each selected object/joint/vertex position"""
    sel = cmds.ls(selection=True, flatten=True)

    # If there is a valid selection
    if sel:

        # Loop through the selected nodes
        for i in range(0, len(sel)):

            # We'll store the position data returned by the xform command in the "pos" variable
            pos = list()

            # Check if node is a transform/joint OR a component vertex/CV
            # If a transform, we'll use the "piv" flag in the xform command for accuracy
            if 'transform' in cmds.nodeType(sel[i]) or 'joint' in cmds.nodeType(sel[i]):
                LOG.info('{} is a transform/joint'.format(sel[i]))
                pos = cmds.xform(sel[i], query=True, worldSpace=True, piv=True)

            # Otherwise, we'll use the "translation" flag for all else, including components
            else:
                LOG.info('{} is a component'.format(sel[i]))
                pos = cmds.xform(sel[i], query=True, worldSpace=True, translation=True)

            # Create a locator and move it to the node's position we just obtained
            loc = cmds.spaceLocator(p=[0, 0, 0])
            cmds.setAttr(loc[0] + '.translate', pos[0], pos[1], pos[2])

        LOG.info('Created locators at selected positions.')
        return True

    # If nothing is selected, let the user know
    else:
        LOG.error('Nothing selected!')
        return



def loc_atSelectedPosRot():
    """Creates new locator and snaps to selected"""
    created_locs = list()
    selection = cmds.ls(selection=True)
    for item in selection:
        loc = cmds.spaceLocator()
        cmds.select(loc[0], item)
        snap_object()
        created_locs.append(loc[0])
        LOG.info('Created {} and snapped to {}'.format(loc[0], item))
    cmds.select(created_locs)

def snap_object():
    """Snaps first selected objects to last selected object"""
    selection = cmds.ls(selection=True)
    if len(selection) >= 2:
        pos = cmds.xform(selection[-1], q=True, ws=True, t=True)
        rot = cmds.xform(selection[-1], q=True, ws=True, ro=True)
        for item in selection[:-1]:
            cmds.xform(item, ws=True, t=pos)
            cmds.xform(item, ws=True, ro=rot)
            LOG.info('Snapped {} to {}'.format(item, selection[-1]))
