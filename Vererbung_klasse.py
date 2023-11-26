from programmierien_mit_python.Klaasen_Erklaren import Exfreundin


class Exfreundin_augen_color(Exfreundin):
    augen_color = None
    def __init__(self,name,ort,familienstand,augen_color,eigenschaften=[]):
        self.augen_color = augen_color
        self.eigehschaften=eigenschaften
        Exfreundin.__init__(self,name,ort,familienstand,eigenschaften=[])

    def alleEinzelheiten1(self):
        print(
            f'Eine exfreundin war {self.NameGroßbuchstaben()} wohnt in {self.ort} ist jetzt {self.familienstand} die augen sind {self.augen_color}. Ihre Merkmale geht um folgendes :', )
        for i, merkmal in enumerate(self.eigehschaften):
            print(i + 1, '.', merkmal)


exf1 = Exfreundin_augen_color('Aparajita','Bangalore','ledig','schwarz',{'Schön','Schlank','Ungeduldig','Nervös','Nicht Nett','Gut für eine Teilzeitfreundschaft nicht langfrischtig'})

exf1.alleEinzelheiten1()

exf1.augen_color = 'blau'

