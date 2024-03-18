from maya import cmds

import logging
import re
import pymel.core as pm
import os


logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

#UPDATE COMPRESSION________________________________

def update_compression_options(*args):
    current_format = cmds.optionMenu(format_menu, query=True, value=True)
    # Supprime les options existantes dans le menu de compression
    cmds.optionMenu(encoding_menu, edit=True, deleteAllItems=True)

    # Ajoute des options de compression basées sur le format de fichier sélectionné
    if current_format == "avi":
        cmds.menuItem(label="none", parent=encoding_menu)
        cmds.menuItem(label="Codec IYUV", parent=encoding_menu)
        cmds.menuItem(label="MS-RLE", parent=encoding_menu)
        cmds.menuItem(label="MS-CRAM", parent=encoding_menu)
        cmds.menuItem(label="MS-YUV", parent=encoding_menu)
        cmds.menuItem(label="Toshiba YUV411", parent=encoding_menu)
        cmds.menuItem(label="x264vfw", parent=encoding_menu)
        cmds.menuItem(label="Huffyyuv", parent=encoding_menu)
        cmds.menuItem(label="Lagarith", parent=encoding_menu)
        cmds.menuItem(label="XVID", parent=encoding_menu)
        # Ajouter d'autres options spécifiques au format AVI si nécessaire
    elif current_format == "qt":
        cmds.menuItem(label="Vidéo MPEG-4", parent=encoding_menu)
        cmds.menuItem(label="Sorenson Video", parent=encoding_menu)
        cmds.menuItem(label="Sorenson Video 3", parent=encoding_menu)
        cmds.menuItem(label="BMP", parent=encoding_menu)
        cmds.menuItem(label="H.264", parent=encoding_menu)
        cmds.menuItem(label="Cinepak", parent=encoding_menu)
        cmds.menuItem(label="DV/DVCPRO - NTSC", parent=encoding_menu)
        cmds.menuItem(label="DV - PAL", parent=encoding_menu)
        cmds.menuItem(label="DVCPRO - PAL", parent=encoding_menu)
        cmds.menuItem(label="H.261", parent=encoding_menu)
        cmds.menuItem(label="H.263", parent=encoding_menu)
        cmds.menuItem(label="Photo - JPEG", parent=encoding_menu)
        cmds.menuItem(label="JPEG 2000", parent=encoding_menu)
        cmds.menuItem(label="Animation JPEG A", parent=encoding_menu)
        cmds.menuItem(label="Animation JPEG B", parent=encoding_menu)
        cmds.menuItem(label="PNG", parent=encoding_menu)
        cmds.menuItem(label="Sans", parent=encoding_menu)
        cmds.menuItem(label="Animation", parent=encoding_menu)
        cmds.menuItem(label="Vidéo", parent=encoding_menu)
        cmds.menuItem(label="Graphique", parent=encoding_menu)
        cmds.menuItem(label="TGA", parent=encoding_menu)
        cmds.menuItem(label="TIFF", parent=encoding_menu)
        cmds.menuItem(label="Composant vidéo", parent=encoding_menu)
        # Ajouter d'autres options spécifiques au format MOV si nécessaire
    elif current_format == "image":
        cmds.menuItem(label="jpg", parent=encoding_menu)
        cmds.menuItem(label="png", parent=encoding_menu)

#ADD CAMERA________________________________________________________________________________

def add_camera_entry(*args):
    global camera_entries
    entry = {}
    row_layout = cmds.rowLayout(numberOfColumns=4, adjustableColumn=True, parent=column_layout)
    entry['row_layout'] = row_layout
    camera_menu = cmds.optionMenu(parent=row_layout, label="Camera")
    for cam in cmds.listCameras(perspective=True):
        cmds.menuItem(label=cam, parent=camera_menu)
    entry['camera'] = camera_menu
    entry['start_frame'] = cmds.intField(parent=row_layout, value=1)
    entry['end_frame'] = cmds.intField(parent=row_layout, value=24)
    delete_btn = cmds.button(parent=row_layout, label="Supprimer")
    entry['delete_btn'] = delete_btn
    camera_entries.append(entry)
    update_delete_buttons()

#REMOVE CAMERA________________________________

def remove_camera_entry(entry):
    camera_entries.remove(entry)
    cmds.deleteUI(entry['row_layout'])
    update_delete_buttons()

#UPDATE DELETE________________________________

def update_delete_buttons():
    for entry in camera_entries:
        cmds.button(entry['delete_btn'], e=True, command=lambda x, e=entry: remove_camera_entry(e))

#PLAYBLAST ACTIVE________________________________

def on_playblast_pressed(*args):
    export_folder = cmds.textField(folder_field, query=True, text=True)
    file_format = cmds.optionMenu(format_menu, query=True, value=True)
    encoding_format = cmds.optionMenu(encoding_menu, query=True, value=True)
    for entry in camera_entries:
        camera = cmds.optionMenu(entry['camera'], query=True, value=True)
        start_frame = cmds.intField(entry['start_frame'], query=True, value=True)
        end_frame = cmds.intField(entry['end_frame'], query=True, value=True)
        create_playblast(camera, start_frame, end_frame, file_format, encoding_format, export_folder)

#PLAYBLAST_____________________________________

def create_playblast(camera, start_frame, end_frame, format, encoding, export_folder):
    render_width = cmds.getAttr("defaultResolution.width")
    render_height = cmds.getAttr("defaultResolution.height")
    playblast_settings = {
        'format': format,
        'sequenceTime': 0,
        'clearCache': 1,
        'viewer': 1,
        'showOrnaments': 1,
        'offScreen': True,
        'fp': 4,
        'percent': 100,
        'compression': encoding,
        'quality': 100,
        'widthHeight': [render_width, render_height],
        'filename': export_folder + "/Playblast_" + camera
    }
    cmds.lookThru(camera)
    cmds.playbackOptions(min=start_frame, max=end_frame)
    cmds.playblast(**playblast_settings)

#EXPORT FOLDER_______________________________

def select_export_folder(*args):
    folder = cmds.fileDialog2(fileMode=3, dialogStyle=2)
    if folder:
        cmds.textField(folder_field, edit=True, text=folder[0])

camera_entries = []

def BuildUI():
    winName = 'Playblast'
    winWidth = 400
    dev = 'William Bélanger'
    mail = 'william@unstandardstudio.com'
    version = 'V.1.0'
    easterEgg = 'Andrew Cyr-Marcoux'

if cmds.window("advancedPlayblastWindow", exists=True):
    cmds.deleteUI("advancedPlayblastWindow")

cmds.window("advancedPlayblastWindow", title="Outil avancé de Playblast")
column_layout = cmds.columnLayout(adjustableColumn=True)

cmds.button(label="Ajouter une caméra", command=add_camera_entry)

# Sélection du format de fichier
format_menu = cmds.optionMenu(label="Format de fichier", changeCommand=update_compression_options)
cmds.menuItem(label="avi")
cmds.menuItem(label="qt")
cmds.menuItem(label="image")
# Ajouter d'autres formats au besoin

# Sélection du format de compression de fichier
encoding_menu = cmds.optionMenu(label="Compression")
# Ajouter d'autres formats au besoin
update_compression_options()
# Sélection du dossier d'exportation
default_export_folder = cmds.workspace(query=True, rd=True)
cmds.rowLayout(numberOfColumns=3, adjustableColumn=2)
cmds.text(label="Dossier d'exportation :")
folder_field = cmds.textField(text=default_export_folder)
cmds.button(label="Parcourir", command=select_export_folder)
cmds.setParent('..')

# Bouton Playblast en bas
cmds.button(label="Playblast", command=on_playblast_pressed)

cmds.showWindow("advancedPlayblastWindow")
