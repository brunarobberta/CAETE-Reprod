import random
import math

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

n_pls = 10
years = 0

pls = []
for i in range(n_pls):
    pls.append({
        'seed_bank': 0,
        'c_storage': 0,
        'npp_rep': 0,
        'mass_seed': 0,
    })

def reproduction(temperature, precipitation, seed_bank, mass_seed, c_storage):
    seed_production = 0  # Valor padrão para seed_production
    if 23 <= temperature <= 30 and 50 <= precipitation <= 200:
        seed_production = c_storage / mass_seed
        seed_bank += int(seed_production)  # Convertendo para inteiro
    return seed_bank, seed_production, c_storage

def germination(seed_bank, germination_temperature):
    if seed_bank > 0 and 23 <= germination_temperature <= 30:
        germinated_seeds = int(seed_bank * 0.5)  # 50% das sementes no banco
        seed_bank -= germinated_seeds  # Subtrair as sementes germinadas do banco
        return germinated_seeds
    return 0

while years < 10:
    days = 0
    while days < 365:
        for pls_id, plss in enumerate(pls):
            if years == 0 and days == 0:
                plss['seed_bank'] = 0  # Set seed bank to 0 on the first day of the first year
            
            plss['c_storage'] = round(random.uniform(0, 100), 1)
            
            temperature = round(random.uniform(23, 30), 1)  # Graus Celsius
            germination_temperature = round(random.uniform(23, 30), 1) 
            precipitation = round(random.uniform(50, 200), 1)  # Milímetros
            wood_density = round(random.uniform(0.5, 0.9), 1)  # Quilogramas por metro cúbico
            cstem = round(random.uniform(1, 15), 1)  # kgC
            diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
            height = round(Kallom2 * diam ** Kallom3, 1)  # Altura em cm
            slope = 0.1
            x = height
            y = slope * x
            plss['mass_seed'] = y
            
            if plss['c_storage'] <= 0:
                days += 1
                continue
            else:
                plss['npp_rep'] = plss['c_storage']
            
            print(f"Species {pls_id + 1} - Year {years + 1}, Day {days + 1}")
            print("c_storage:", plss['c_storage'])
            print("temperature:", temperature)
            print("precipitation:", precipitation)
            print("wood_density:", wood_density)
            print("cstem:", cstem)
            print("diam:", diam)
            print("height:", height)
            print("slope:", slope)
            
            print("\nReproduction:")
            print(f"Seed bank before reproduction pls {pls_id + 1}: {plss['seed_bank']}")
            plss['seed_bank'], seed_production, plss['c_storage'] = reproduction(temperature, precipitation, plss['seed_bank'], plss['mass_seed'], plss['c_storage'])
            print(f"seed bank after reproduction pls {pls_id + 1}: {plss['seed_bank']}")

            print("\nGermination:")
            germinated_seeds = germination(plss['seed_bank'], germination_temperature)
            plss['seed_bank'] -= germinated_seeds
            print(f"sementes germinadas pls {pls_id + 1}: {germinated_seeds}")
            print(f"seed bank after germination pls {pls_id + 1}: {plss['seed_bank']}")
            
            print()
            
        for pls_id, plss in enumerate(pls):
            decayed_seeds = int(plss['seed_bank'] * 0.5)
            plss['seed_bank'] -= decayed_seeds
            print(f"Year {years + 1} - plss {pls_id + 1} - Decayed seeds: {decayed_seeds}")
        
        days += 1
    
    years += 1
