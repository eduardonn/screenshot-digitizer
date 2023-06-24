from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import styles
from digitizer import Digitizer
from PIL import ImageGrab
import clipboard
from layout import initLayout

class GUI(QWidget):
    drawAreaBorderWidth = 2

    def __init__(self):
        super().__init__()
        self.selectedLanguageButton = None
        self.digitizer = Digitizer()
        self.drawAreaBegin = None
        self.contour = QLabel(self)
        self.contour.setStyleSheet('background: white;')
        self.contour.resize(0, 0)
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle('Screenshot Digitizer')
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        initLayout(self)
    
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Q or e.key() == Qt.Key_Escape:
          self.close()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.drawAreaBegin = (e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if not self.isDrawAreaValid(e):
            print('Invalid area')
            return
        
        img = ImageGrab.grab(bbox=(*self.drawAreaBegin, e.x(), e.y()))
        digitizedText = self.digitizer.digitize(img)
        clipboard.copy(digitizedText)
        os._exit(0)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        drawnAreaRegion = QRegion(
            self.drawAreaBegin[0],
            self.drawAreaBegin[1],
            e.x() - self.drawAreaBegin[0],
            e.y() - self.drawAreaBegin[1]
        )
        holeInWindowRegion = QRegion(self.rect()).subtracted(drawnAreaRegion)
        self.setMask(holeInWindowRegion)
        
        drawAreaRect = drawnAreaRegion.boundingRect()
        if self.isDrawAreaValid(e):
            self.contour.setGeometry(
                drawAreaRect.x() - self.drawAreaBorderWidth,
                drawAreaRect.y() - self.drawAreaBorderWidth,
                drawAreaRect.width() + self.drawAreaBorderWidth * 2,
                drawAreaRect.height() + self.drawAreaBorderWidth * 2
            )
        else:
            self.contour.resize(0, 0)

    def handleLanguageOptionClick(self, button: QPushButton):
        self.selectedLanguageButton.setStyleSheet(styles.languageOptionInactive)
        button.setStyleSheet(styles.languageOptionActive)
        self.selectedLanguageButton = button
        self.digitizer.setLanguage(self.selectedLanguageButton.text())

    def handleLineBreakOptionClick(self, button: QPushButton):
        if self.digitizer.shouldRemoveLineBreaks:
            button.setText('ON')
            button.setStyleSheet(styles.removeLineBreaksButton + 'QWidget { color: green; }')
        else:
            button.setText('OFF')
            button.setStyleSheet(styles.removeLineBreaksButton + 'QWidget { color: lightgray; }')
        self.digitizer.shouldRemoveLineBreaks = not self.digitizer.shouldRemoveLineBreaks

    def paintEvent(self, e):
        backgroundColor = QColor('black')
        backgroundColor.setAlpha(85)
        customPainter = QPainter(self)
        customPainter.fillRect(self.rect(), backgroundColor)
        super().paintEvent(e)

    def isDrawAreaValid(self, startPoint: QRect):
        return startPoint.x() > self.drawAreaBegin[0] and startPoint.y() > self.drawAreaBegin[1]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())