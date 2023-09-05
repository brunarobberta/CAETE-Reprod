import random
import math
import matplotlib.pyplot as plt

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

n_pls = 10
years = 0

pls = []

# Geração das propriedades das espécies
for i in range(n_pls):
    wood_density = round(random.uniform(0.5, 0.9), 1)
    wood_density = wood_density / 1000
    cstem = round(random.uniform(5, 20), 1)
    cstem = cstem * 1000
    diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)
    height = round(Kallom2 * diam ** Kallom3, 1)
    mass_seed = (height / 10) ** (0.08) ** (1 / 0.43)

    pls.append({
        'seed_bank': 0,
        'npp_disponivel': 0,
        'npp_rep': 0,
        'mass_seed': mass_seed,
        'wood_density': wood_density,
        'cstem': cstem,
        'diam': diam,
        'height': height,
    })

def reproduction(temperature, precipitation, seed_bank, mass_seed, npp_rep):
    seed_production = 0
    if 23 <= temperature <= 30 and 50 <= precipitation <= 200:
        seed_production = npp_rep / mass_seed
        seed_bank += int(seed_production)
    return seed_bank, seed_production, npp_rep

def germination(seed_bank, germination_temperature):
    if seed_bank > 0 and 23 <= germination_temperature <= 30:
        germinated_seeds = int(seed_bank * 0.5)
        seed_bank -= germinated_seeds
        return germinated_seeds
    return 0

while years < 10:
    for day in range(365):
        temperature = round(random.uniform(23, 30), 1)
        precipitation = round(random.uniform(50, 200), 1)
        
        for pls_id, plss in enumerate(pls):
            if years == 0:
                plss['seed_bank'] = 0

            npp_disponivel = round(random.uniform(0, 1.3), 1)
            npp_disponivel = npp_disponivel * 1000
            npp_cstem = npp_disponivel * 0.35
            npp_disponivel -= npp_cstem
            npp_rep = npp_disponivel * 0.1

            germination_temperature = round(random.uniform(23, 30), 1)

            if npp_rep <= 0:
                continue
            else:
                plss['npp_rep'] = npp_rep

            print(f"Species {pls_id + 1} - Year {years + 1}, Day {day + 1}")
            print("temperature:", temperature, "°C")
            print("precipitation:", precipitation, "mm")
            print("wood_density:", plss['wood_density'], "g/cm³")
            print("cstem:", plss['cstem'], "gC")
            print("diam:", plss['diam'], "cm")
            print("height:", plss['height'], "cm")
            print("mass_seed:", plss['mass_seed'])
            print("npp_rep", npp_rep)
            print("npp_disponivel", npp_disponivel)

            print("\nReproduction:")
            print(f"Seed bank before reproduction pls {pls_id + 1}: {plss['seed_bank']}")
            plss['seed_bank'], seed_production, plss['npp_rep'] = reproduction(temperature, precipitation, plss['seed_bank'], plss['mass_seed'], npp_rep)
            print(f"seed bank after reproduction pls {pls_id + 1}: {plss['seed_bank']}")

            print("\nGermination:")
            germinated_seeds = germination(plss['seed_bank'], germination_temperature)
            plss['seed_bank'] += germinated_seeds
            print(f"sementes germinadas pls {pls_id + 1}: {germinated_seeds}")
            print(f"seed bank after germination pls {pls_id + 1}: {plss['seed_bank']}")

            decayed_seeds = int(plss['seed_bank'] * 0.5)
            plss['seed_bank'] -= decayed_seeds
            print(f"Year {years + 1} - plss {pls_id + 1} - Decayed seeds: {decayed_seeds}")
        
    years += 1
