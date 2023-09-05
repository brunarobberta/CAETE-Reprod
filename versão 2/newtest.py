import random
import numpy as np
from random  import randint
# importing pandas package
import pandas as pd

c_storage = []
# npp_pls = []
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

        light = round((random.uniform(400, 1000)),2) #600 e 800
        print ('light', light)

        soil_water = round((random.uniform(30, 100)),2) #50 e 85
        print ('soil_water', soil_water)

        for i in range (npls):
            c_storage.append (round((random.uniform(0.5, 4.0)),2))
            print ('c_storage', c_storage)


        for i in range (npls):
            mass_seed.append (round((random.uniform (0.02, 1.5)), 2))
            print('mass_seed', mass_seed)


#
#calcular o npp disponível para reprodução em cada pls (10%)
#NAO SERA MAIS ASSIM
        #npp_rep = [item * 0.1 for item in npp_pls] 
#carbono provindo do storage = se > 0
#sera todo o storage
        if (c_storage > 0): 
             npp_rep  = [item * 0.1 for item in c_storage] 
             print(npp_rep)

#produção das sementes:
#proporção de produção das sementes  com base na temperatura e chuva
    
        if 300 <= rain <= 1000 and 20 <= temperature <= 35:             
            n_seed = [A / B  if A > 0 else 0 for A, B in zip(npp_rep, mass_seed)]
            print('n_seed', n_seed)
            seed_bank = n_seed + seed_bank

        #else:
            #n_seed = seed_bank
            #germ_seed = (tuple (item * 0.20 for item in seed_bank))

        #fazer decaimento

        if seed_bank > 0:
            continue
#germinação
#germinação das sementes no banco de sementes com base na luz e umidade do solo


        if 600 <= light <= 800 and 50 <= soil_water <= 85:
             seedlings = seed_bank * SEED_GERM_PROP
             #numero fixo
             #seed_germ_prop valor fixo a mudar no teste de sensibilidade do modelo
        else:
                #vai para o storage?
                #transformar numero de sementes em carbono no seed_bank
                c_storage = seed_bank
                #analisar storage
                #germ_seed = (item * 0.20 for item in seed_bank) #pensar se será 20%?

        print('seedlings', seedlings)

        seed_bank = seed_bank - seedlings
        


                #call establishment(seedlings);
                #call updatePLS_seedbank(seedlings); //decrement
                #number of seeds in PLS seedbank


        #parei aqui 


        ano2 = [A - B for A, B in zip (seed_bank, seedlings)]
        print('ano2', ano2)


        acumulacao = [A + B for A,B in zip(ano2, npp_pls)]
        print('acm', acumulacao)
   


        days += 1

#Atualizar seed_bank considerando o decaimento (mortalidade) anual de sementes


    years += 1 