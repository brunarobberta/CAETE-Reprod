import random
import numpy as np
from random  import randint

n_pls = 4
mass_seed  = np.random.randint(1,52, (4))
npp = (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1))

tempo = 0
while tempo < 10:
    

    ano2 = []
    npp_pls = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)] 
#    print(npp_pls)
    mass_seed = [0.1, 1, 3, 4]
    agua = 20
#    npp_2 = npp_pls + ano2
#    print(npp_2)
    


    

#calcular o npp disponível para reprodução em cada pls (10%)
    npp_rep = [item * 0.1 for item in npp] 
    print(npp_rep)

#print(npp_rep)

#calcular o n de sementes produzidas para cada pls se há npp disponivel (maior que 0)
    n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
    print(n_seed)

  
#n_seed = [A * 0.1 / B for A, B in zip(npp_pls, mass_seed)] #A e B são nomes genéricos nessa operação

#permanecem apenas sementes viaveis do numero total anterior (60%)
    seed_bank = [item * 0.60 for item in n_seed] + ano2
    print(seed_bank)

    
#proporção de germinação das sementes no banco de sementes com base na umidade do solo = 40% ideal
    
    if agua in range(30,50):
        germ_seed = seed_bank
    else:
       germ_seed = (tuple (item * 0.20 for item in seed_bank))

    print(germ_seed)

#sementes que continuam no bank_seed apos a germinação para o próximo ano
    ano2.append = [A - B for A, B in zip (seed_bank, germ_seed)]
    print(ano2)
#    for number in ano2:
#        ano2.append(ano2)

#    seed_bank = [A - B for A,B in zip(seed_bank, germ_seed)]
#    for seed_bank in seed_bank:
#    print(seed_bank)

    acumulacao = [A + B for A,B in zip(ano2, npp_pls)]
    print(acumulacao)
   
#    seed_bank = (tuple (A - B for A, B in zip(seed_bank, germ_seed)))
#    print(seed_bank)

#    total = sum((npp_pls) + (ano2))
#    print(total)





    tempo += 1 
