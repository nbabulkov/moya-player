from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtMultimedia
from tinytag import TinyTag

PLAYER_STATES = {
    QtMultimedia.QMediaPlayer.StoppedState: "Stopped",
    QtMultimedia.QMediaPlayer.PlayingState: "Playing",
    QtMultimedia.QMediaPlayer.PausedState: "Paused"
}

class InvalidMediaException(Exception):
    pass

def loadMediaFile(filename):
    url = QtCore.QUrl.fromLocalFile(filename)
    if not url.isValid():
        raise InvalidMediaException
    return QtMultimedia.QMediaContent(url)

def getSong(audioPath):
    tags = TinyTag.get(audioPath)
    return "{} - {}".format(tags.artist, tags.title)

class Player(QtMultimedia.QMediaPlayer):
    changedStatus = QtCore.pyqtSignal('QString')

    def __init__ (self):
        super().__init__()
        self.status = 'Stopped'
        self._playlist = QtMultimedia.QMediaPlaylist()
        self._playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Sequential)
        self._playlist.setCurrentIndex(1)
        self.setPlaylist(self._playlist)
        self.setAudioRole(QtMultimedia.QAudio.MusicRole)
        self.setVolume(50)
        self.events()

    def events(self):
        self.stateChanged.connect(self.changeState)

    @QtCore.pyqtSlot()
    def mute(self):
        self.setVolume(0)

    @QtCore.pyqtSlot(QtMultimedia.QMediaPlayer.State)
    def changeState(self, state):
        song = self._playlist.currentMedia().canonicalUrl().path()
        if song is not '':
            song = getSong(song)

        self.status = "{}: {}".format(PLAYER_STATES[state], song)
        self.changedStatus.emit(self.status)

    @property
    def length(self):
        return self._playlist.mediaCount()

    @property
    def index(self):
        return self._playlist.currentIndex()

    @property
    def playlistProgress(self):
        return self.index, self.length

    def removeFromPlaylist(self, removeIndex):
        self._playlist.removeMedia(removeIndex)

    def addToPlaylist(self, audioFile, index=self.length):
        self._playlist.addMedia(loadMediaFile(audioFile))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    url = QUrl.fromLocalFile("/home/nbabulkov/Music/war_pigs.mp3")
    playlist.addMedia(QMediaContent(url))
    playlist.setCurrentIndex(1);
    player = Player()
    player.setPlaylist(playlist)
    player.play()
    sys.exit(app.exec_())
