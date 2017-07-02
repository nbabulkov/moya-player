import player
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = player.Player()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setWindowTitle('MOYA Player')
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.initControlButtons()

        self.progressBar = QtWidgets.QSlider(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 460, 751, 20))
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")

        self.positionLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLabel.setGeometry(QtCore.QRect(30, 440, 59, 18))
        self.positionLabel.setObjectName("position")

        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(710, 440, 59, 18))
        self.durationLabel.setObjectName("duration")

        self.volumeBar = QtWidgets.QSlider(self.centralwidget)
        self.volumeBar.setGeometry(QtCore.QRect(670, 500, 101, 20))
        self.volumeBar.setOrientation(QtCore.Qt.Horizontal)
        self.volumeBar.setObjectName("volumeBar")
        self.volumeBar.setSliderPosition(50)

        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setGeometry(QtCore.QRect(610, 490, 51, 34))
        self.muteButton.setObjectName("muteButton")

        self.playingLabel = QtWidgets.QLabel(self.centralwidget)
        self.playingLabel.setGeometry(QtCore.QRect(150, 440, 491, 18))
        self.playingLabel.setObjectName("playingLabel")

        self.controlBox = QtWidgets.QHBoxLayout()
        self.controlBox.addWidget(self.progressBar)
        self.controlBox.addWidget(self.playButton)
        self.controlBox.addWidget(self.forwardButton)
        self.controlBox.addWidget(self.backwardButton)
        self.controlBox.addWidget(self.playingLabel)

        self.initPlaylistUI()

        self.setCentralWidget(self.centralwidget)

        self.initStatusBar()
        self.initMenuBar()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.events()
        self.show()

    def events(self):
        self.library.addToPlaylistButton.clicked.connect(self.addToPlaylist)
        self.library.listWidget.itemDoubleClicked.connect(self.selectPlaying)
        self.progressBar.sliderMoved.connect(self.player.setPosition)
        self.player.positionChanged.connect(self.progressBar.setValue)
        self.volumeBar.valueChanged.connect(self.player.setVolume)
        self.playButton.clicked.connect(self.playOrPause)
        self.player.durationChanged.connect(self.adjustAudioDuration)
        self.playbackButton.statusChanged.connect(self.player.setPlaybackMode)
        self.forwardButton.clicked.connect(self.player.next)
        self.backwardButton.clicked.connect(self.player.previous)
        self.player.changedStatus.connect(self.changePlaying)
        self.player.positionChanged.connect(self.adjustAudioPosition)
        self.stopButton.clicked.connect(self.player.stop)
        self.library.removeFromPlaylistButton.clicked.connect(self.removeFromPlaylist)

