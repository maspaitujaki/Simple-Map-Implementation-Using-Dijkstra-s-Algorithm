from cProfile import label
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import os

from Graph import Graph

class PrettyWidget(QWidget):

    NumButtons = ['plot1','plot2', 'plot3']

    def __init__(self):


        super(PrettyWidget, self).__init__()        
        font = QFont()
        font.setPointSize(16)
        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle('S Plot')

        grid = QGridLayout()
        self.setLayout(grid)
        self.createVerticalGroupBox() 

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.verticalGroupBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)        
        grid.addWidget(self.canvas, 0, 1, 9, 9)          
        grid.addLayout(buttonLayout, 0, 0)

        self.show()


    def createVerticalGroupBox(self):
        self.verticalGroupBox = QGroupBox()

        layout = QVBoxLayout()

        self.fileNameLabel = QLabel('Choose file')
        self.fileNameLabel.setObjectName('FileNameLabel')
        layout.addWidget(self.fileNameLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.browseButton = QPushButton('browse')
        self.browseButton.setObjectName('browse')
        layout.addWidget(self.browseButton)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)
        self.browseButton.clicked.connect(self.browseFile)

        simpulAsalLabel = QLabel('Simpul Asal')
        simpulAsalLabel.setObjectName('SimpulAsal')
        layout.addWidget(simpulAsalLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.SimpulAsalComboBox = QComboBox()
        self.SimpulAsalComboBox.setObjectName('SimpulAsalComboBox')
        layout.addWidget(self.SimpulAsalComboBox)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)
        self.SimpulAsalComboBox.currentIndexChanged.connect(self.simpulAsalChanged)

        simpulTujuanLabel = QLabel('Simpul Tujuan')
        simpulTujuanLabel.setObjectName('SimpulTujuan')
        layout.addWidget(simpulTujuanLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.SimpulTujuanComboBox = QComboBox()
        self.SimpulTujuanComboBox.setObjectName('SimpulTujuanComboBox')
        layout.addWidget(self.SimpulTujuanComboBox)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        startButton = QPushButton('start')
        startButton.setObjectName('start')
        layout.addWidget(startButton)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)
        startButton.clicked.connect(self.startDikjstra)

        clearButton = QPushButton('clear')
        clearButton.setObjectName('clear')
        layout.addWidget(clearButton)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)
        clearButton.clicked.connect(self.clearAction)

        self.banyakIterasiLabel = QLabel('')
        self.banyakIterasiLabel.setObjectName('banyakIterasiLabel')
        layout.addWidget(self.banyakIterasiLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.lintasanLabel = QLabel('')
        self.lintasanLabel.setObjectName('lintasanLabel')
        layout.addWidget(self.lintasanLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.panjangLintasanLabel = QLabel('')
        self.panjangLintasanLabel.setObjectName('panjangLintasanLabel')
        layout.addWidget(self.panjangLintasanLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

        self.waktuLabel = QLabel('')
        self.waktuLabel.setObjectName('waktuLabel')
        layout.addWidget(self.waktuLabel)
        layout.setSpacing(10)
        self.verticalGroupBox.setLayout(layout)

    def clearAction(self):
        self.SimpulAsalComboBox.clear()
        self.SimpulTujuanComboBox.clear()
        self.fileNameLabel.setText("Choose File")
        self.panjangLintasanLabel.setText("")
        self.waktuLabel.setText("")
        self.banyakIterasiLabel.setText("")
        self.lintasanLabel.setText("")
        self.figure.clf()
        self.browseButton.setEnabled(True)
        

    def browseFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', 'Text files (*.txt)')
        self.fileNameLabel.setText(fname[0])
        
        if os.path.exists(fname[0]):
            self.graph = Graph(fname[0])
            self.browseButton.setEnabled(False)
            self.fig()

    def simpulAsalChanged(self):
        self.SimpulTujuanComboBox.clear()
        strArr = list(map(lambda x: str(x), self.graph.graph.keys()))
        try:
            strArr.remove(self.SimpulAsalComboBox.currentText())
            self.SimpulTujuanComboBox.addItems(strArr)
        except:
            pass

    
    def fig(self):
        self.SimpulAsalComboBox.clear()
        self.figure.clf()
        nxG = nx.DiGraph()
        G = self.graph.graph
        V = [str(key) for key, value in G.items()]
        E = []
        for key, value in G.items():
            for key2, value2 in value.items():
                E.append((str(key),str(key2), value2))
        nxG.add_nodes_from(V)
        nxG.add_weighted_edges_from(E)
        weight = nx.get_edge_attributes(nxG,'weight')
        self.pos = nx.spring_layout(nxG)
        # nx.draw(nxG,pos=self.pos, with_labels=True)
        nx.draw_networkx_nodes(nxG, self.pos)
        nx.draw_networkx_labels(nxG, self.pos)
        nx.draw_networkx_edges(nxG, self.pos,connectionstyle='arc3, rad = 0.1')
        nx.draw_networkx_edge_labels(nxG,self.pos,edge_labels=weight,label_pos=0.3)
        self.canvas.draw_idle()

        self.SimpulAsalComboBox.addItems(list(map(lambda x: str(x), self.graph.graph.keys())))

    def figPath(self, path):
        self.figure.clf()
        pathDict = {}
        for i in range(len(path)-1):
            pathDict[path[i]] = path[i+1]
        nxG = nx.DiGraph()
        G = self.graph.graph
        V = [str(key) for key, value in G.items()]
        E = []
        for key, value in G.items():
            for key2, value2 in value.items():
                # if key in pathDict.keys() and value2 == pathDict[key]:
                E.append((str(key),str(key2), value2))
        nxG.add_nodes_from(V)
        nxG.add_weighted_edges_from(E, color='black')
        weight = nx.get_edge_attributes(nxG,'weight')

        for i in range(len(path)-1):
            nxG.edges[str(path[i]), str(path[i+1])]['color'] = "red"
            # print(nxG.nodes[str(path[i])])

        edges = nxG.edges()
        # print(edges)
        colors = [nxG[u][v]['color'] for u,v in edges]

        # nx.draw(nxG,pos=self.pos, edge_color=colors, with_labels=True)
        nx.draw_networkx_nodes(nxG, self.pos)
        nx.draw_networkx_nodes(nxG, self.pos, nodelist=list(map(lambda x: str(x), path)), node_color='red')
        nx.draw_networkx_labels(nxG, self.pos)
        nx.draw_networkx_edges(nxG, self.pos,connectionstyle='arc3, rad = 0.1', edge_color=colors)
        nx.draw_networkx_edge_labels(nxG,self.pos,edge_labels=weight,label_pos=0.3)
        self.canvas.draw_idle()

    def startDikjstra(self):
        simpulAsal = int(self.SimpulAsalComboBox.currentText())
        simpulTujuan = int(self.SimpulTujuanComboBox.currentText())

        result = self.graph.findShortestPath(simpulAsal, simpulTujuan)

        self.figPath(result.get('path'))
        
        lintasan = ''
        for i in range(len(result.get('path'))):
            lintasan += str(result.get('path')[i])
            if (i != len(result.get('path')) - 1):
                lintasan += " -> "
        self.lintasanLabel.setText('Lintasan: ' + lintasan)
        self.banyakIterasiLabel.setText('Banyak Iterasi: ' + str(result.get('iterasi')))
        self.waktuLabel.setText("Waktu eksekusi: " + str(result.get('waktu')) + " ms")
        self.panjangLintasanLabel.setText("Panjang lintasan: " + str(result.get('distance')))


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    import sys  
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = PrettyWidget() 
    screen.show()   
    sys.exit(app.exec_())

"""
Modify base on:
http://stackoverflow.com/questions/36086361/embed-matplotlib-in-pyqt-with-multiple-plot/36093604

"""