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
        'seed_germ_prop': 0
    })

def reproduction(temperature, precipitation, seed_bank, npp_rep, mass_seed, c_storage):
    print("\nReproduction:")
    print(f"Seed bank before reproduction pls {pls_id + 1}: {seed_bank}")
    if 23 <= temperature <= 30 and 50 <= precipitation <= 200:
        seed_production = npp_rep / mass_seed
        seed_bank += int(seed_production)  # Convertendo para inteiro
        print(f"seed bank after reproduction pls {pls_id + 1}: {seed_bank}")
    else:
        print("Conditions not met for reproduction")
        c_storage += npp_rep  # Devolve o valor de npp_rep para c_storage
    return seed_bank, npp_rep, c_storage

def germination(seed_bank, germination_temperature, seed_germ_prop):
    print("\nGermination:")
    print(f"Germination temperature: {germination_temperature}")
    if seed_bank > 0 and 23 <= germination_temperature <= 30:
        random_value = random.uniform(0, 100)
        if random_value <= seed_germ_prop:
            germinated_seeds = min(seed_bank, int(seed_bank * (seed_germ_prop / 100)))  # Convertendo para inteiro e limitando ao número de sementes no banco
            seed_bank -= germinated_seeds
            print(f"sementes germinadas pls {pls_id + 1}: {germinated_seeds}")
        else:
            germinated_seeds = 0
            print("Nenhuma semente germinou")
        print(f"seed bank after germination pls {pls_id + 1}: {seed_bank}")
    else:
        print("Não atendeu às condições de germinação")
    return seed_bank, germinated_seeds


while years < 10:
    days = 0
    while days < 365:
        for pls_id, plss in enumerate(pls):
            if years == 0 and days == 0:
                plss['seed_bank'] = 0  # Set seed bank to 0 on the first day of the first year
            
            plss['c_storage'] = round(random.uniform(0, 100), 1)
            
            temperature = round(random.uniform(23, 30), 1)
            precipitation = round(random.uniform(50, 200), 1)
            wood_density = round(random.uniform(0.5, 0.9), 1)
            cstem = round(random.uniform(1, 15), 1)
            plss['seed_germ_prop'] = round(random.uniform(50, 100), 1)
            diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)
            height = round(Kallom2 * diam ** Kallom3, 1)
            slope = 0.1
            x = height
            y = slope * x
            plss['mass_seed'] = y
            
            if plss['c_storage'] <= 0:
                days += 1
                continue
            else:
                plss['npp_rep'] = plss['c_storage']
            

            
            plss['seed_bank'], plss['npp_rep'], plss['c_storage'] = reproduction(temperature, precipitation, plss['seed_bank'], plss['npp_rep'], plss['mass_seed'], plss['c_storage'])
            germination_temperature = round(random.uniform(23, 30), 1)
            plss['seed_bank'], germinated_seeds = germination(plss['seed_bank'], germination_temperature, plss['seed_germ_prop'])
        
        for plss in pls:
            decayed_seeds = int(plss['seed_bank'] * 0.1)
            plss['seed_bank'] -= decayed_seeds
            plss['seed_bank'] = max(plss['seed_bank'], 0)  # Ensure the seed bank doesn't go negative
        
        days += 1
    
    years += 1
