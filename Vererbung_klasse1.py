class Versicherung:

    def __init__(self, Name, Alter, Einkommen, Stadt, max_raten, Versicherungspflichten, gh):
        self.Name = Name
        self.Alter = Alter
        self.Einkommen = Einkommen
        self.Stadt = Stadt
        self.Max_Raten = max_raten
        self.VersicherungsAnforderungen = Versicherungspflichten
        self.versicherter()
        self.gh=gh
        self.eigung()

    def versicherter(self):
        print(
            f'Name: {self.Name} \n Alter: {self.Alter} \n Einkommen : {self.Einkommen} \n Stadt : {self.Stadt} \n Max Raten : {self.Max_Raten} \n Versicherung : {self.VersicherungsAnforderungen}')

    def eigung(self):
        if self.Max_Raten > 500 and self.Einkommen > 4000 and self.Alter < 65:
            print('Alle Versicherung erhältlich')
            return 'AV'
        elif self.Max_Raten > 400 and self.Einkommen > 3000 and self.Alter < 65:
            print('Hausversicherung, Lebensversicherung und Autoversicherung')
            return 'HLAU'
        elif self.Max_Raten > 200 and self.Einkommen > 2000 and self.Alter < 65:
            print('Lebensversicherung und Autoversicherung')
            return 'LAU'
        elif self.Max_Raten > 100 and self.Einkommen > 1500 and self.Alter < 65:
            print('Lebensversicherung')
            return 'L'
        else:
            print('Bitte wenden Sie sich an den Kundendienst')
            return 'KA'
    def Ratenbetrag_erhohen(self, nr):
        print(f'Altes Ratenbetrag: {self.Max_Raten}')
        self.Max_Raten = nr
        print(f'Neues Ratenbetrag : {self.Max_Raten}')

    def Ratenbetrag_verringern(self, nr):
        print(f'Altes Ratenbetrag: {self.Max_Raten}')
        self.Max_Raten = nr
        print(f'Neues Ratenbetrag : {self.Max_Raten}')

class Vorerkrankungen():
    def __init__(self, gesundheit):
        self.gesundheit = gesundheit

    def beschreibung_gesundheit(self):
        l1 = ['Sonnenstiche', 'Allergein', 'Fieber', 'Erkaltung']
        l2 = ['Krebs','Insektenstiche']
        if self.gesundheit in l1:
            print('Kranken versicherung erlaubt')
        else:
            print('Kranken versicherung nicht erlaubt')
        print(f'Vorerkrankungen - {self.gesundheit}')

class Auto_vs(Versicherung):
    def __init__(self, Name, Alter, Einkommen, Stadt, max_raten, Versicherungspflichten,gh):

        super().__init__(Name, Alter, Einkommen, Stadt, max_raten, Versicherungspflichten,gh)
        self.minimal = 200
        self.gesundheit = Vorerkrankungen(self.gh)

    def berechtigung_uberprufen(self):
        if self.Max_Raten < self.minimal:
            print('Auto Verischerung Nicht berechtigt')
            return 'NE'
        else:
            print('Gluckwunsch Auto Versicherung erlaubt')





#person1 = Versicherung('Max', 45, 4000, 'Munchen', 300, 'Auto')

person2 = Auto_vs('Max', 45, 8000, 'Munchen', 300, 'Auto','Fieber')

person2.berechtigung_uberprufen()

person2.gesundheit.beschreibung_gesundheit()


