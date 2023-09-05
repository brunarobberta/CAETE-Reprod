import random
import numpy as np

def germinate_seeds(seed_bank, germ_prop, light, soil_water):
    if 600 <= light <= 800 and 50 <= soil_water <= 85:
        return [sb * germ_prop for sb in seed_bank]
    else:
        return [0] * len(seed_bank)

c_storage = []
mass_seed = []
npls = 5

for i in range(npls):
    mass_seed.append(round(random.uniform(0.02, 1.5), 2))
print('mass_seed', mass_seed)

# Lista para armazenar o seed_bank ao longo dos anos
seed_bank_over_time = []

years = 0
while years < 10:
    days = 0
    seed_bank = np.zeros(npls)
    seedlings = np.zeros(npls)  # Variável para armazenar as sementes germinadas a cada dia
    while days < 365:
        rain = round(random.uniform(200, 2000), 2)
        temperature = round(random.uniform(15, 40), 2)
        SEED_GERM_PROP = round(random.uniform(10, 100), 2)
        light = round(random.uniform(400, 1000), 2)
        soil_water = round(random.uniform(30, 100), 2)
        
        c_storage = np.array([round(random.uniform(0.5, 4.0), 2) for _ in range(npls)])
        print('rain', rain)
        print('temperature', temperature)
        print('seed_germ_prop', SEED_GERM_PROP)
        print('light', light)
        print('soil_water', soil_water)
        print('c_storage', c_storage)
        
        npp_rep = c_storage * 0.1
        print('npp_rep', npp_rep)

        # Produção das sementes
        seed_production = np.where(npp_rep > 0, npp_rep / mass_seed, 0)
        print('seed_production', seed_production)

        # Atualizar seed_bank com as novas sementes produzidas
        seed_bank += seed_production

        # Germinar as sementes diariamente
        seedlings = germinate_seeds(seed_bank, SEED_GERM_PROP, light, soil_water)
        seed_bank -= seedlings
        print('seedlings', seedlings)

        days += 1

    # Atualizar c_storage com a acumulação anual
    c_storage += seed_bank
    print('c_storage', c_storage)

    # Armazenar o seed_bank atual na lista seed_bank_over_time
    seed_bank_over_time.append(seed_bank[:])

    years += 1

# Imprimir o seed_bank ao longo dos anos
for year, sb in enumerate(seed_bank_over_time, start=1):
    print(f"Ano {year}: {sb}")


#um banco de sementes pra cada pls
#budget 
#commit waited mean cwn
#quanto tem atributo de uma sp multiplica 

