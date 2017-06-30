import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import (QMediaPlayer,
                                QMediaPlaylist,
                                QMediaContent,
                                QMediaPlaylist,
                                QAudio)

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
        self._playlist.addMedia(QMediaContent(QUrl.fromLocalFile(audioFile)))

