#teste com massa da semente ao inves da agua

import random
import numpy as np
from random  import randint

npp_pls = []
mass_seed = []
npls = 5

for i in range (npls):
    mass_seed.append (round((random.uniform (0.02, 1.5)), 2))
    print('mass_seed', mass_seed)

years = 0
while years < 10:
    days = 0
    while days < 365:

        rain = round((random.uniform(200, 2000)),2)
        print ('rain', rain)

        temperature = round((random.uniform(15, 40)),2)
        print ('temperature', temperature)

        SEED_GERM_PROP = round((random.uniform(10, 100)),2)
        print ('seed_germ_prop', SEED_GERM_PROP)

        for i in range (npls):
            npp_pls.append (round((random.uniform(0.5, 4.0)),2))
            print ('npp_pls', npp_pls)

            #as 3 linhas anteriores deverão ser substituidas pela condição:
            #if 

        #npp_pls = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)] #argumento de função
        #ex. p no fortran (pls), vem do codigo das meninas
        #print('npp_pls', npp_pls)

        for i in range (npls):
            mass_seed.append (round((random.uniform (0.02, 1.5)), 2))
            print('mass_seed', mass_seed)

        #mass_seed = [0.1, 1, 3, 4]
        #agua = 20
#    npp_2 = npp_pls + ano2
#    print(npp_2)
    


    

#calcular o npp disponível para reprodução em cada pls (10%)
#NAO SERA MAIS ASSIM
        npp_rep = [item * 0.1 for item in npp_pls] 

#print(npp_rep)

#calcular o n de sementes produzidas para cada pls se há npp disponivel (maior que 0)
        #n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
        #print('n_seed', n_seed)

  
#n_seed = [A * 0.1 / B for A, B in zip(npp_pls, mass_seed)] #A e B são nomes genéricos nessa operação

#permanecem apenas sementes viaveis do numero total anterior (60%)
        #if years == 0:
        #    seed_bank = [item * 0.60 for item in n_seed]
        #else:
        #    seed_bank = [item * 0.60 for item in n_seed] + ano2
        
        #print('seed_bank', seed_bank)

    
#proporção de germinação das sementes no banco de sementes com base na umidade do solo = 40% ideal
    
        if (rain >= 500):
            n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
            print('n_seed', n_seed)
            seed_bank = n_seed + seed_bank

            #germ_seed = seed_bank
            #precisa de else? so se a condição if não for atendida.....
            ####### finalizamos aqui 20/06 - continuar
            #prox if = seed_bank, incluir proximo else antes de seguir o prox if pls seed_bank > 0
            #linha 62 flowchart v3
            #continuei dia 26/06
        else:
            n_seed = seed_bank
            #germ_seed = (tuple (item * 0.20 for item in seed_bank))

        print('n_seed', n_seed)

        #como inserir duas condições?

        if ((seed_bank > 0) and (temperature >= 30)):
                germ_seed = seed_bank
        else:
                germ_seed = (item * 0.20 for item in seed_bank) #pensar se será 20%?

        print('germ_seed', germ_seed)

        #ou call germination_func(PLS_seedbank);????
        if ((seed_bank > 0) and (temperature >= 30)):
                seedlings = seed_bank * SEED_GERM_PROP #definir antes?
        else: 
                germ_seed = (item * 0.20 for item in seed_bank)

                seed_bank = seed_bank - germ_seed

        print('germ_seed', germ_seed)
        


                #call establishment(seedlings);
                #call updatePLS_seedbank(seedlings); //decrement
                #number of seeds in PLS seedbank


        #parei aqui 



#sementes que continuam no bank_seed apos a germinação para o próximo ano
#    if tempo == 0:
#        ano2 = 0
#    else: 
#        ano2 = [A - B for A, B in zip(seed_bank, germ_seed)]

#        print('ano2', ano2)
        ano2 = [A - B for A, B in zip (seed_bank, germ_seed)]
        print('ano2', ano2)
#    for number in ano2:
#        ano2.append(ano2)

#    seed_bank = [A - B for A,B in zip(seed_bank, germ_seed)]
#    for seed_bank in seed_bank:
#    print(seed_bank)

        acumulacao = [A + B for A,B in zip(ano2, npp_pls)]
        print('acm', acumulacao)
   
#    seed_bank = (tuple (A - B for A, B in zip(seed_bank, germ_seed)))
#    print(seed_bank)

#    total = sum((npp_pls) + (ano2))
#    print(total)

        days += 1

#Atualizar seed_bank considerando o decaimento (mortalidade) anual de sementes


    years += 1 
