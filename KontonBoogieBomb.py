import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QShortcut, QKeySequence
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def resource_path(name):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, name)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)

VIDEO = resource_path("KONTONBOOGIE.mp4")

dev = AudioUtilities.GetSpeakers()
dev.EndpointVolume.SetMasterVolumeLevelScalar(1.0, None)

app = QApplication(sys.argv)
win = QMainWindow()
vw = QVideoWidget()
win.setCentralWidget(vw)

p = QMediaPlayer()
ao = QAudioOutput()
ao.setVolume(1.0)
p.setAudioOutput(ao)
p.setVideoOutput(vw)
p.setSource(QUrl.fromLocalFile(VIDEO))

win.showFullScreen()
p.play()
QShortcut(QKeySequence("Alt+F11"), win, activated=win.close)

sys.exit(app.exec())