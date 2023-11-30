import datetime

print('Zuerst ein paar fragen. Falls Sie verlassen mochten, geben Sie ein Q')
while True:
    n = input('Bitte geben Sie ihre namen ein : ')
    if n =='Q' or n=='q':
        break


    else:
        print(f'Moin {n} Wilkommen zu unserer blogpost \n')
        x = input('Gefallt dir testing ? Sag uns warum ? -> ')
        d = datetime.datetime.now()
        with open('gasteNamen.txt', 'a') as handle:
            handle.write(n)
            handle.write('\n')
            handle.write(x)
            handle.write('\n')
            handle.write(d.strftime("%c")+' ')
            handle.write('\n')