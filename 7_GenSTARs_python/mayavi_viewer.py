import sys, os
from pyface.qt import QtGui, QtCore
os.environ['ETS_TOOLKIT'] = 'qt4'
import os
import csv
import pandas as pd
import numpy as np
from traits.api import HasTraits,Instance,on_trait_change,Button
from traitsui.api import View,Item,HGroup,VGroup,Group
from mayavi import mlab
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor
from scipy import misc, stats

#####################################################
## Script to visualize S2-perturbations about each PD
## HOW TO USE:
# load conda environment (see repository)
# run via CLI: python mayavi_viewer.py
#####################################################

class Mayavi_Scene(HasTraits):
    scene = Instance(MlabSceneModel, ())

    display_angle = Button('Display Euler Angles')

    @on_trait_change('display_angle')
    def view_anglesP2(self):
        viewS2 = self.scene.mlab.view(figure=Mayavi_Scene.fig1)
        azimuth = viewS2[0] #phi: 0-360
        elevation = viewS2[1] #theta: 0-180
        zoom = viewS2[2]
        print(azimuth, elevation)

    @on_trait_change('scene.activated')
    def update_scene(self):
        Mayavi_Scene.fig1 = mlab.figure(1, bgcolor=(.5,.5,.5))
        self.scene.mlab.clf(figure=Mayavi_Scene.fig1)

        pyDir = os.path.dirname(os.path.realpath(__file__)) #python file location
        starDir = os.path.join(pyDir, 'STARs')
        
        starPaths = []
        i = 0
        for root, dirs, files in os.walk(starDir):
            for file in sorted(files):
                if not file.startswith('.'): #ignore hidden files
                    if file.endswith(".star"):
                        starPaths.append(os.path.join(root, file))
                        i += 1

        starRot = [] #phi-values
        starTilt = [] #theta-values
        for z in starPaths:   
            starFile = []
            with open(z, 'r') as values: 
                for i in range(0,19): #skip header
                    next(values)
                starReader = csv.reader(values, delimiter='\t')
                for lines in starReader:
                    starFile.append(lines)
            values.close()
            
            # grab list of rot and tilt from each star file independently:
            for i in range(np.shape(starFile)[0]):
                starRot.append(starFile[i][0])
                starTilt.append(starFile[i][1])
            
        def sphere2cart(theta, phi):
            r = 100
            x = r*np.sin(phi)*np.cos(theta)
            y = r*np.sin(phi)*np.sin(theta)
            z = r*np.cos(phi)
            return x,y,z

        starRotTilt = np.column_stack((starRot,starTilt))
        if 0: #sanity-check
            print(starRotTilt[0])
            print(starRotTilt[-1])
            
        index = []    
        cartX = []
        cartY = []
        cartZ = []
        idx = 1
        for i in starRotTilt:
            x,y,z = sphere2cart(float(i[0])*np.pi/180, float(i[1])*np.pi/180)
            index.append(idx)
            cartX.append(x)
            cartY.append(y)
            cartZ.append(z)
            idx += 1
        
        # save angles to file (e.g., for rendering figures in external programs):
        if 1:
            if os.path.exists('cartXYZ.txt'):
                os.remove('cartXYZ.txt')
            cartXYZ = np.column_stack((index,cartX,cartY,cartZ))
            np.savetxt('cartXYZ.txt', cartXYZ, delimiter='\t', fmt='%1.6i %1.3f %1.3f %1.3f')

        # calculate S2-surface densities:
        if 0:
            print('Calculating densities...')
            values = np.array([cartX, cartY, cartZ])
            kde = stats.gaussian_kde(values)
            cartD = kde(values) #density
            cartD /= cartD.max() #relative density, max=1
            
            mayavi_plot = mlab.points3d(cartX, cartY, cartZ, cartD, scale_mode='none', mode='axes',
                                  scale_factor=.5, figure=Mayavi_Scene.fig1)
            mayavi_cbar = mlab.scalarbar(title='Relative\nDensity\n', orientation='vertical', \
                                         nb_labels=3, label_fmt='%.1f')
        else:
            mayavi_plot = mlab.points3d(cartX, cartY, cartZ, scale_mode='none', mode='axes',
                                  scale_factor=.5, figure=Mayavi_Scene.fig1)
            mayavi_plot.actor.property.color = (0.0, 1.0, 1.0) 

    view = View(VGroup(
                Group(
                Item('scene', editor = SceneEditor(scene_class=MayaviScene),
                    height=300, width=300, show_label=False),
                Item('display_angle',springy=False,show_label=False),
                ),
                ),
                resizable=True,
                )
                

class P1(QtGui.QWidget):
    def __init__(self, parent=None):
        super(P1, self).__init__(parent)
        layout = QtGui.QGridLayout(self)
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)
        self.viz1 = Mayavi_Scene()
        self.ui1 = self.viz1.edit_traits(parent=self, kind='subpanel').control
        layout.addWidget(self.ui1, 1, 1, 9, 9)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 500, 500)   
        tab1 = P1(self)
        self.tabs = QtGui.QTabWidget(self)
        self.tabs.addTab(tab1, 'Alignment Viewer')
        self.groupscroll = QtGui.QHBoxLayout()
        self.groupscrollbox = QtGui.QGroupBox()
        self.MVB = QtGui.QVBoxLayout()
        self.MVB.addWidget(self.tabs)
        scroll = QtGui.QScrollArea()
        widget = QtGui.QWidget(self)
        widget.setLayout(QtGui.QHBoxLayout())
        widget.layout().addWidget(self.groupscrollbox)
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        self.groupscrollbox.setLayout(self.MVB)
        self.groupscroll.addWidget(scroll)
        self.setCentralWidget(scroll)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication.instance()
    w = MainWindow()
    sys.exit(app.exec_())
