from maya import cmds

import logging


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)



def do_LockUnlockAttr(lock = True, attrs = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']):

    sel = cmds.ls(sl=True)

    if sel:
        for i in sel:
            for attr in attrs:
                if lock:
                    cmds.setAttr('{}.{}'.format(i, attr), lock = True, k = False)
                else:
                    cmds.setAttr('{}.{}'.format(i, attr), lock = False, k = True)

    else:
        LOG.error('Nothing in selection.')


def do_createCategoryUi():
    """User prompted to enter category attr name to add to selected"""
    sel = cmds.ls(sl=True)

    if sel:
        result = cmds.promptDialog(
            title='Add category',
            message='Enter Category Name:',
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel')

        if result == 'OK':
            categoryName = cmds.promptDialog(query=True, text=True)
            do_createCategory(sel[0], categoryName)
    else:
        LOG.error('Nothing in selection.')


def do_createCategory(top_node, category_name):
    """Creates category display attr on top_node connected to a create category transform

    create_category('rig_topnode', 'rig')
    """
    if cmds.objExists(top_node):
        if not cmds.objExists(category_name):
            cat_node = cmds.createNode('transform', name=category_name)
            cmds.parent(cat_node, top_node)
            cmds.addAttr(top_node, longName=category_name, at='enum', en="off:on:reference:")
            cmds.setAttr('{}.{}'.format(top_node, category_name), lock=False, keyable=True)
            cmds.connectAttr('{}.{}'.format(top_node, category_name), '{}.visibility'.format(category_name))

            # Create category condition node and connect category attribute to it
            cond_node = cmds.createNode('condition', name='{}_{}_cond'.format(top_node, category_name))
            cmds.connectAttr('{}.{}'.format(top_node, category_name), '{}.firstTerm'.format(cond_node))
            cmds.setAttr('{}.secondTerm'.format(cond_node), 2)
            cmds.setAttr('{}.operation'.format(cond_node), 0)
            cmds.setAttr('{}.colorIfTrueR'.format(cond_node), 2)
            cmds.setAttr('{}.colorIfFalseR'.format(cond_node), 0)

            # Connect output of condition node to the display overrides of the category node
            cmds.connectAttr('{}.outColorR'.format(cond_node),
                             '{}.drawOverride.overrideDisplayType'.format(category_name))
            cmds.setAttr('{}.overrideEnabled'.format(category_name), 1)
            cmds.setAttr('{}.overrideEnabled'.format(category_name), lock=True)
            cmds.setAttr('{}.drawOverride.overrideDisplayType'.format(category_name), lock=True)

            # Set display to "on" by default and lock/hide all other attrs
            for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']: 
                cmds.setAttr('{}.{}'.format(category_name, attr), lock=True, keyable=False)
            cmds.setAttr('{}.{}'.format(top_node, category_name), 1)

            cmds.select(category_name)
            LOG.info('Created category node/attr {} on {}'.format(category_name, top_node))
            return True

        else:
            LOG.error('{} already exists'.format(category_name))
            return
    else:
        LOG.error('{} does not exist'.format(top_node))
        return
