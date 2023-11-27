
class Ferchau:
    def __init__(self,id,name):
        self.name = name
        self.id=id
        print(f'{self.id} ist {self.name} und mit Ferchau beruftatig')


class Personalwesen(Ferchau):
    def __init__(self,id,name):
        print(name,'arbeitet in der Personalabteilung')
        super().__init__(id,name)

class Vertriebsteam(Ferchau):
    def __init__(self,id,name):
        if id in [102,104,110,109,108,113]:
            print(name, 'arbeitet in der Vertriebsabteilung')
        super().__init__(id,name)
        self.nachSehen()

    def nachSehen(self):
        if id not in [102, 104, 110, 109, 108, 113]:
            print(self.id, 'nicht in Vertriebs')
        else:
            print(self.id, ' vertriebs Arbeitnehmer')


m1 = Personalwesen(102,'Heike')
m2 = Vertriebsteam(109, 'Marie')