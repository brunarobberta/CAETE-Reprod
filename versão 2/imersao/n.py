import random
import math
import numpy as np  
import matplotlib.pyplot as plt 

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

n_pls = 5
years = 0
produced_seeds = 0
germinated_seeds = 0
seeds_to_decay = 0


pls = []
for i in range(n_pls):
    pls.append({
        'seed_bank': 0,
        'wood_density': 0,
        'cstem':0,
        'diam':0,
        'height': 0,
        'mass_seed': 0,
    })

for i in range(n_pls):
    wood_density = round(random.uniform(0.5, 0.9), 1)  # grama por cm3
    pls[i]['wood_density'] = wood_density
    #wood_density = wood_density / 1000 #converte para grama por cm3
    cstem = round(random.uniform(5, 20), 1)  # kgC
    pls[i]['cstem'] = cstem
    #cstem = cstem * 1000 #converte em g de carbono
    diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
    pls[i]['diam'] = diam

    height = round(Kallom2 * diam ** Kallom3, 1)  # Altura em m
    pls[i]['height'] = height
    
    mass_seed = (height / 10) ** (0.08) ** (1 / 0.43)
    pls[i]['mass_seed'] = mass_seed

    print(f"Species {i+1}- WD {pls[i]['wood_density']}, H {pls[i]['height']}, Seed_mass {pls[i]['mass_seed']}, Cstem {pls[i]['cstem']}, diam {pls[i]['diam']}",)
 
def reproduction(mass_seed, npp_rep):
    seed_production = 0  # Valor padrão para seed_production
    #if 23 <= temperature <= 30 and 50 <= precipitation <= 200:
    seed_production = npp_rep / mass_seed
        #seed_bank += int(seed_production)  # Convertendo para inteiro
    return seed_production

def germination(seed_bank):
    #if seed_bank > 0 and 23 <= germination_temperature <= 30:
        germinated_seeds = int(seed_bank * 0.5)  # 50% das sementes no banco
        #seed_bank -= germinated_seeds  # Subtrair as sementes germinadas do banco
        return germinated_seeds


while years < 3:
    print('ANO:', {years+1})
    
    days = 0
    while days < 365:
        #tazer os testes de produção e germinaço com condiçoes climatics para ca
        temperature = round(random.uniform(20, 41), 1)  # Graus Celsius
        precipitation = round(random.uniform(50, 2500), 1)  # Milímetros

        #for pls_id, plss in enumerate(pls):
        for pls_id in range(n_pls):
            npp_disponivel = round(random.uniform(0, 1.3), 1) #quilogramas de carbono por m2
            npp_disponivel = npp_disponivel * 1000 #convertendo para gramas de carbono por m2
            #pls[plss]['npp_disponivel'] = npp_disponivel
            #print(f"Seed bank before reproduction pls {pls_id}: {pls[pls_id]['seed_bank']}")
            
            if 23 <= temperature <= 30 and 50 <= precipitation <= 200 and npp_disponivel > 0: 
                npp_rep = npp_disponivel * 0.1 
                #plss['npp_rep'] = npp_rep   
                print(f"Seed bank before reproduction pls {pls_id}: {pls[pls_id]['seed_bank']}")

                print(f"Species {pls_id} - Year {years + 1}, Day {days + 1}")
                print("temperature:", temperature, "°C")
                print("precipitation:", precipitation, "mm")
                print("\nReproduction:")
                #print(f"Seed bank before reproduction pls {pls_id + 1}: {produced_seeds}")
                #print(f"Seed bank before reproduction pls {pls_id}: {produced_seeds}")

                s_mass = pls[pls_id]['mass_seed']

                produced_seeds = reproduction(s_mass, npp_rep)
                produced_seeds = int(produced_seeds)

                pls[pls_id]['seed_bank'] += produced_seeds

                print(f"Number of seeds in PLS  {pls_id} - seedbank: {produced_seeds}")

            #else: print('******NAO PRODUZIU SEMENTES*************')
            else: pass

            if pls[pls_id]['seed_bank'] > 0 and 23 <= temperature <= 30:

                print("\nGermination:")
                pls_seeds = pls[pls_id]['seed_bank']
                germinated_seeds = int(pls_seeds * 0.5)
                #germinated_seeds = germination(pls_seeds)

                pls[pls_id]['seed_bank'] -= germinated_seeds

                print(f"sementes germinadas pls {pls_id}: {germinated_seeds}")
                print(f"seed bank after germination pls {pls_id}: {pls[pls_id]['seed_bank']}")
            #else: print('******NAO GERMINOU SEMENTES*************')
            else: pass
        days += 1
        #print("days", days)     
            
    for pls_id in range(n_pls):
        seeds_to_decay = pls[pls_id]['seed_bank']
        decayed_seeds = seeds_to_decay * 0.5
        pls[pls_id]['seed_bank'] -= decayed_seeds
        print(f"Year {years + 1} - pls {pls_id} - Decayed seeds: {decayed_seeds} - Updated seed_bank: {pls[pls_id]['seed_bank']}")
        
    years += 1
    #print("anos", years)

