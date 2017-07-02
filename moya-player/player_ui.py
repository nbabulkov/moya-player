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

    @QtCore.pyqtSlot()
    def playOrPause(self):
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.playButton.setText("Play")
            self.player.pause()
        else:
            self.playButton.setText("Pause")
            self.player.play()

    def initPlaylistUI(self):
        self.library = Ui_Library(self.centralwidget)

    def initControlButtons(self):
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(310, 490, 81, 41))
        self.playButton.setObjectName("playButton")

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(400, 490, 81, 41))
        self.stopButton.setObjectName("stopButton")

        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(500, 490, 71, 34))
        self.forwardButton.setObjectName("forwardButton")

        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setGeometry(QtCore.QRect(210, 490, 81, 31))
        self.backwardButton.setObjectName("backwardButton")

        self.playbackButton = PlaybackButton(self.centralwidget)
        self.playbackButton.setGeometry(QtCore.QRect(30, 490, 131, 31))
        self.playbackButton.setObjectName("playbackButton")

    def initMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

    def initStatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.forwardButton.setText(_translate("MainWindow", "Forward"))
        self.backwardButton.setText(_translate("MainWindow", "Backward"))
        self.playingLabel.setText(_translate("MainWindow", "Stoped"))
        self.playingLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.muteButton.setText(_translate("MainWindow", "Mute"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Ui_MainWindow()
    m.addSong('/home/nbabulkov/Music/war_pigs.mp3')
    sys.exit(app.exec_())
