import math
import numpy as np


while True:

    des = str(input('''retangular[a+jb] -> polar[z<0] [r]
       polar[z<0] -> retangular[a+jb] [p] ''')).upper()

    if des == "R":
        print(''' 
                  _                          _                  __                _            
         _ __ ___| |_ __ _ _ __   __ _ _   _| | __ _ _ __       \ \   _ __   ___ | | __ _ _ __ 
        | '__/ _ \ __/ _` | '_ \ / _` | | | | |/ _` | '__|  _____\ \ | '_ \ / _ \| |/ _` | '__|
        | | |  __/ || (_| | | | | (_| | |_| | | (_| | |    |_____/ / | |_) | (_) | | (_| | |   
        |_|  \___|\__\__,_|_| |_|\__, |\__,_|_|\__,_|_|         / /  | .__/ \___/|_|\__,_|_|   
                                 |___/                         /_/   |_|                       
        ''')

        a = float(input('qual é o A:'))
        b = float(input('qual é o b?'))


        # parte real
        z = math.sqrt(((a**2)+(b**2)))

        #parte imaginaria

        #caluclo arco tangente
        arco = math.atan(b/a)
        #passando de radianos para gras
        arcog = math.degrees(arco)


        print(f"a parte real(z) é {z:.2f} ")
        print(f'a parte imaginaria é {arcog:.2f}')
        print('cuidado com o sinal')

        print()
        des2 = str(input('deseja sair [S/N]')).upper()
        if des2 == 'S':
            break

    else:
        print('''         
                     _                  __             _                          _             
         _ __   ___ | | __ _ _ __       \ \   _ __ ___| |_ __ _ _ __   __ _ _   _| | __ _ _ __  
        | '_ \ / _ \| |/ _` | '__|  _____\ \ | '__/ _ \ __/ _` | '_ \ / _` | | | | |/ _` | '__| 
        | |_) | (_) | | (_| | |    |_____/ / | | |  __/ || (_| | | | | (_| | |_| | | (_| | |    
        | .__/ \___/|_|\__,_|_|         /_/  |_|  \___|\__\__,_|_| |_|\__, |\__,_|_|\__,_|_|    
        |_|                                                           |___/                     
        ''')

        h = float(input("hipotenusa:"))
        teta = float(input('a parte que não é a hipotenusa'))

        # pega o valor do cosseno em radianos e passa pra graus
        t2 = np.cos(np.radians(teta))
        re = t2 * h

        #pega o valor do cosseno em radianos e passa para graus
        t3 = np.sin(np.radians(teta))
        im = t3 * h

        print(f' re : {re:.2f}')
        print(f' im : {im:.2f}')
        print('atenção ao sinal')

        print()
        des2 = str(input('deseja sair [S/N]')).upper()
        if des2 == 'S':
            break
