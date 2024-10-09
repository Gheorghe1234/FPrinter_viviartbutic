import cyrtranslit


class UTILITY:
    def __init__(self):
        pass

    def LANGRusToCyrilik(self, TextRUS):
        TextRUS = str(TextRUS).decode('cp1251')
        TextRUS = unicode(TextRUS).encode('utf-8')
        TextCyrylik = cyrtranslit.to_latin(TextRUS, 'ru')

        return TextCyrylik