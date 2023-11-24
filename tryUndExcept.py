class tempo:
    fahrzeug = 'Auto'
    def __init__(self, auto_name, tempo):
        self.auto_name = auto_name
        self.tempo = tempo

    def tempo_in_Km(self,tempo):
        try:
            s = float(tempo)
            km = s * 1.609
            return ('Das tempo auf km ist'+km)
        except:
            return 'Bitte gib eine zahl ein'

Auto_eins = tempo('Audi',150)

print(Auto_eins.__dict__)
print(Auto_eins.tempo_in_Km())