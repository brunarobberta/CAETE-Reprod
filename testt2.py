import random
import numpy as np
from random  import randint

npp_pls = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)] 
print(npp_pls)
mass_seed = [0.1, 1, 3, 4]
agua = 20
npp_rep = [item * 0.1 for item in npp_pls]
print(npp_rep)
n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
print(n_seed)
seed_bank = [item * 0.60 for item in n_seed]
print(seed_bank)
if agua in range(30,50):
    germ_seed = seed_bank
else:
    germ_seed = (tuple (item * 0.20 for item in seed_bank))
    print(germ_seed)
ano2 = [ A - B for A, B in zip (seed_bank, germ_seed)]
print(ano2)

tempo = 0
while tempo < 9:

    
    npp_pls = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]  
    print(npp_pls)
    mass_seed = [0.1, 1, 3, 4]
    agua = 20
#    npp_2 = npp_pls + ano2
#    print(npp_2)
    


    

#calcular o npp disponível para reprodução em cada pls (10%)
    npp_rep = [item * 0.1 for item in npp_pls] 

#print(npp_rep)

#calcular o n de sementes produzidas para cada pls se há npp disponivel (maior que 0)
    n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
    print(n_seed)

  
#n_seed = [A * 0.1 / B for A, B in zip(npp_pls, mass_seed)] #A e B são nomes genéricos nessa operação

#permanecem apenas sementes viaveis do numero total anterior (60%)
    seed_bank = [A + B for A, B in zip(n_seed + ano2)]
    seed_bank2 = [item * 0.60 for item in seed_bank]
    print(seed_bank2)

    
#proporção de germinação das sementes no banco de sementes com base na umidade do solo = 40% ideal
    
    if agua in range(30,50):
        germ_seed = seed_bank2
    else:
       germ_seed = (tuple (item * 0.20 for item in seed_bank2))

    print(germ_seed)

#sementes que continuam no bank_seed apos a germinação para o próximo ano
    ano2 = [ A - B for A, B in zip (seed_ban0k2, germ_seed)]
    print(ano2)

#    seed_bank = [A - B for A,B in zip(seed_bank, germ_seed)]
#    for seed_bank in seed_bank:
#    print(seed_bank)

#    acumulacao = [A + B for A,B in zip(ano2, npp_pls)]
#    print(acumulacao)



    

#    npp_pls = acumulation

#    seed_bank = (tuple (A - B for A, B in zip(seed_bank, germ_seed)))
#    print(seed_bank)

#    total = sum((npp_pls) + (ano2))
#    print(total)





    tempo += 1 


