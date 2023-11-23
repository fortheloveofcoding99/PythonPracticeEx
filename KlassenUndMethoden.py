
class Freund_freundin_bewertungen:

    merkmale = {
                'liebevoll' : +5,
                'frohlich' : +10,
                'fürsorglich': +10,
                'ordentlich': +5,
                'Schön': +5,
                'Gutaussehend': +10,
                'Schlau': +5,
                'intelligent': +10,
                'dreckig': -5,
                'unordentlich': -5,
                'verbringt viel': -5,
                'Tendenz zu flirten': -5,
                'ungeduldig': -5,
                'betrogen': -20,
                'beschwert sich': -10,
                'kein musikliebhaber': -5
    }
    def __init__(self, name,hoch,gs=[],ss=[]):
        self.Name = name
        self.Hoch = hoch
        self.Gute_Seiten = gs
        self.Schlechte_Seiten = ss
        self.einschätzen()

    def einschätzen(self):
        punkte = 0
        for gs in self.Gute_Seiten:
            if gs in self.merkmale: punkte = punkte + self.merkmale[gs]
            else: punkte += 1
        for ss in self.Schlechte_Seiten:
            if ss in self.merkmale: punkte = punkte + self.merkmale[ss]
            else: punkte -= 1
        print(f'Die name ist: {self.Name} und is {self.Hoch} gross und die bewertungen ist {punkte}')


ExFreundin1 = Freund_freundin_bewertungen('Aparajita','150cm',('Schlau','Schön','liebevoll','Tendenz zu flirten','betrogen'),('beschwert sich','schlecht'))






