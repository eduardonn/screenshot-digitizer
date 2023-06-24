from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import styles
import typing

if typing.TYPE_CHECKING:
    from main import GUI

def initLayout(root: 'GUI'):
    background = QWidget()
    background.setStyleSheet("""
      background: black;
      max-height: 50px;
    """)
    hBoxMain = QHBoxLayout(background)
    hBoxMain.setSpacing(50)
    hBoxMain.setContentsMargins(10, 0, 10, 0)

    vBoxMain = QVBoxLayout()
    vBoxMain.addWidget(background)
    vBoxMain.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
    vBoxMain.setContentsMargins(0, 0, 0, 0)

    languageOptionLabel = QLabel('Language:')
    languageOptionLabel.setStyleSheet(styles.text)
    languageOptionButtons: list[QPushButton] = []
    for lang in root.digitizer.availableLanguages:
        languageOptionButtons.append(QPushButton(lang))

    for button in languageOptionButtons:
        if button.text() == root.digitizer.selectedLanguage:
            button.setStyleSheet(styles.languageOptionActive)
            root.selectedLanguageButton = button
        else:
            button.setStyleSheet(styles.languageOptionInactive)
    
    languageOptionButtons[0].clicked.connect(
        lambda: root.handleLanguageOptionClick(languageOptionButtons[0]))
    languageOptionButtons[1].clicked.connect(
        lambda: root.handleLanguageOptionClick(languageOptionButtons[1]))
    languageOptionButtons[2].clicked.connect(
        lambda: root.handleLanguageOptionClick(languageOptionButtons[2]))

    hBoxLanguageOption = QHBoxLayout()
    hBoxLanguageOption.setSpacing(0)
    hBoxLanguageOption.addWidget(languageOptionLabel)
    for button in languageOptionButtons:
      hBoxLanguageOption.addWidget(button)
    
    lineBreaksOptionLabel = QLabel('Line Breaks:')
    lineBreaksOptionLabel.setStyleSheet(styles.text)
    lineBreaksOptionButton = QPushButton()
    if root.digitizer.shouldRemoveLineBreaks:
        lineBreaksOptionButton.setText('OFF')
        lineBreaksOptionButton.setStyleSheet(
            styles.removeLineBreaksButton + 'QWidget { color: lightgray; }')
    else:
        lineBreaksOptionButton.setText('ON')
        lineBreaksOptionButton.setStyleSheet(
            styles.removeLineBreaksButton + 'QWidget { color: green; }')
        
    lineBreaksOptionButton.clicked.connect(
        lambda: root.handleLineBreakOptionClick(lineBreaksOptionButton))

    hBoxLineBreakOption = QHBoxLayout()
    hBoxLineBreakOption.setSpacing(10)
    hBoxLineBreakOption.addWidget(lineBreaksOptionLabel)
    hBoxLineBreakOption.addWidget(lineBreaksOptionButton)

    hBoxMain.addLayout(hBoxLanguageOption)
    hBoxMain.addLayout(hBoxLineBreakOption)

    root.setLayout(vBoxMain)