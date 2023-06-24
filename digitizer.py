import pytesseract

class Digitizer:
    def __init__(self):
        self.shouldRemoveLineBreaks = True
        self.availableLanguages = ['ENG', 'POR', 'JAP']
        self.selectedLanguage = self.availableLanguages[0]
        pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract'

    def setLanguage(self, value):
        self.selectedLanguage = value

    def setShouldRemoveBreakLine(self, value):
        self.shouldRemoveLineBreaks = value

    def digitize(self, img):
        digitizedText = pytesseract.image_to_string(img, lang=self.selectedLanguage)
        
        if (self.shouldRemoveLineBreaks):
            digitizedText = digitizedText.replace('\n', ' ')
        
        return digitizedText