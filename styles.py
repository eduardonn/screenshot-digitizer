text = """
  QWidget {
    color: white;
    font-family: Consolas;
    font-size: 24px;
  }
"""

languageOptionInactive = text + """
  QWidget {
    padding: 10px;
    padding-top: 100%;
    padding-bottom: 100%;
    border: 3px solid transparent;
  }
  QWidget:hover {
    background-color: rgb(40, 40, 40);
  }
"""

languageOptionActive = languageOptionInactive + """
  QWidget {
    border: 3px solid green;
  }
"""

removeLineBreaksButton = text + """
  QWidget {
    width: 60px;
    padding-top: 100%;
    padding-bottom: 100%;
  }
  QWidget:hover {
    background-color: rgb(40, 40, 40);
  }
"""