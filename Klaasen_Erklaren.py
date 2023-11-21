
class Exfreundin():
    def __init__(self,name,ort,familienstand,eigenschaften=[]):
        #initialisieren attributes
        self.name=name
        self.ort=ort
        self.eigehschaften=eigenschaften
        self.familienstand=familienstand
        self.alleEinzelheiten()

    def alleEinzelheiten(self):
        print(f'Eine exfreundin war {self.name} wohnt in {self.ort} ist jetzt {self.familienstand}. Ihre Merkmale geht um folgendes :',)
        for i,merkmal in enumerate(self.eigehschaften):
            print(i+1,'.',merkmal)



Exfreundin_eins= Exfreundin('Aparajita','Bangalore','ledig',('Schön','Schlank','Ungeduldig','Nervös','Gut für eine Teilzeitfreundschaft nicht langfrischtig'))

