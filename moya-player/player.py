import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import (QMediaPlayer,
                                QMediaPlaylist,
                                QMediaContent,
                                QMediaPlaylist,
                                QAudio)

class InvalidMediaException(Exception):
    pass

def loadMediaFile(filename):
    url = QUrl.fromLocalFile(filename)
    if not url.isValid():
        raise InvalidMediaException
    return QMediaContent()

class Player(QMediaPlayer):
    def __init__ (self):
        self._playlist= QMediaPlaylist()
        super().__init__()
        self.setAudioRole(QAudio.MusicRole)
        self.setVolume(50)

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
