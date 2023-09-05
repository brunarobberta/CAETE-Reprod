import random
import math

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

def generate_random_values():
    # Geração de valores aleatórios 
    c_storage = round(random.uniform(0, 100), 1)  # Gramas por metro quadrado
    print('c_storage:', c_storage)
    
    temperature = round(random.uniform(10, 40), 1)  # Graus Celsius
    print('temperature:', temperature)
    
    soil_moisture = round(random.uniform(0, 100), 1)  # %
    print('soil_moisture:', soil_moisture)
    
    precipitation = round(random.uniform(10, 300), 1)  # Milímetros
    print('precipitation:', precipitation)
    
    light = round(random.uniform(200, 800), 1)  # Nanômetros
    print('light:', light)
    
    wood_density = round(random.uniform(0.5, 0.9), 1)  # Quilogramas por metro cúbico
    print('wood_density:', wood_density)
    
    cstem = round(random.uniform(1, 15), 1)  # kgC
    print('cstem:', cstem)
    
    seed_germ_prop = round(random.uniform(1, 100), 1)  # Probabilidade de germinação (1 a 100)
    print('seed_germ_prop:', seed_germ_prop)
    
    diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
    print('diam:', diam)
    
    height = round(Kallom2 * diam ** Kallom3, 1)  # Altura em cm
    print('height:', height)


    
    
    slope = 0.1
    x = height
    y = slope * x

    return c_storage, temperature, soil_moisture, precipitation, light, wood_density, cstem, seed_germ_prop, diam, height, y

def update_pls_biomass(seedlings, pls_biomass):
    pls_biomass[0] += sum(seedlings)

def reproduction(c_storage, temperature, precipitation, pls_biomass, seed_bank):
    print("\nReproduction:")
    print("Seed bank before reproduction:", seed_bank)
    if c_storage > 0 and 23 <= temperature <= 30 and 50 <= precipitation <= 200:
        npp_rep = c_storage
        mass_seed = 0
        seedlings = []
        for i in range(10):
            if mass_seed > 0:
                npp_rep /= mass_seed
                pls_seedbank = 1
                germinated_seeds = round(pls_seedbank * (seed_germ_prop / 100), 1)
                seedlings.append(germinated_seeds)
                mass_seed += germinated_seeds
            else:
                germinated_seeds = round(npp_rep, 1)
                seedlings.append(germinated_seeds)
                mass_seed += germinated_seeds
        update_pls_biomass(seedlings, pls_biomass)
        print("Produced seedlings:", seedlings)
        print("PLS Biomass after reproduction:", pls_biomass)
        seed_bank -= mass_seed
        print("Seed bank after reproduction:", seed_bank)
        return seedlings
    else:
        update_pls_biomass([c_storage], pls_biomass)
        seed_bank -= c_storage
        print("Seed bank after reproduction:", seed_bank)
        return [c_storage]

def germination(seed_bank, light, soil_moisture, pls_biomass):
    print("\nGermination:")
    print("Seed bank before germination:", seed_bank)
    if seed_bank > 0 and 600 <= light <= 700 and 30 <= soil_moisture <= 65:
        pls_seedbank = seed_bank
        germination_rate = seed_germ_prop / 100
        germinated_seeds = int(pls_seedbank * germination_rate)
        pls_biomass[0] += germinated_seeds
        seed_bank -= germinated_seeds
        print("Germinated seeds:", germinated_seeds)
        print("PLS Biomass after germination:", pls_biomass)
    else:
        print("Germination did not occur.")
        pls_biomass[0] += 0
    print("Seed bank after germination:", seed_bank)

# Listas para cada PLS
seed_banks = [[0] for _ in range(10)]  # Lista de bancos de sementes para cada PLS
pls_biomass = [[10] for _ in range(10)]  # Lista de biomassa para cada PLS

# Loop anual
for year in range(1, 11): # Simulação de 10 anos
    print(f"\nYear {year}:")

    # Loop diário para as 10 PLS
    for day in range(365): # Considerando um ano com 365 dias
        print(f"\nDay {day + 1}:")
        for i in range(10):
            c_storage, temperature, soil_moisture, precipitation, light, wood_density, cstem, seed_germ_prop, diam, height, mass_seed = generate_random_values()
            print(f"\nPLS {i + 1}:")
            print("Generated values:", c_storage, temperature, soil_moisture, precipitation, light, wood_density, cstem, seed_germ_prop, diam, height, mass_seed)
            seedlings = reproduction(c_storage, temperature, precipitation, pls_biomass[i], seed_banks[i][0])
            germination(seed_banks[i][0], light, soil_moisture, pls_biomass[i])
            seed_banks[i][0] += sum(seedlings)

        # Atualizar o banco de sementes após o decaimento anual
        for i in range(10):
            seed_banks[i][0] *= 0.9

