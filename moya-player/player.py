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
    def playlistSize(self):
        return self._playlist.mediaCount()

    @property
    def playlistIndex(self):
        return self._playlist.currentIndex()

    @property
    def playlistProgress(self):
        return self.playlistIndex, self.playlistSize

    @property
    def playProgress(self):
        return self.position, self.duration

    @QtCore.pyqtSlot(QtMultimedia.QMediaPlaylist.PlaybackMode)
    def setPlaybackMode(self, mode):
        self._playlist.setPlaybackMode(mode)

    @QtCore.pyqtSlot()
    def next(self):
        self._playlist.next()

    @QtCore.pyqtSlot()
    def previous(self):
        self._playlist.previous()

    def removeFromPlaylist(self, removeIndex):
        self._playlist.removeMedia(removeIndex)

    def addToPlaylist(self, audioFile):
        self._playlist.addMedia(loadMediaFile(audioFile))

    def setIndex(self, index):
        if index < self.playlistSize and self.playlistSize >= 0:
            self._playlist.setCurrentIndex(index)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    url = "/home/nbabulkov/Music/war_pigs.mp3"
    player = Player()
    player.addToPlaylist(url)
    player.play()
    sys.exit(app.exec_())

