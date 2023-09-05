import random
import math

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

def generate_random_values():
    # Geração de valores aleatórios conforme especificado no enunciado
    # (Valores de entrada para as simulações)
    c_storage = round(random.uniform(0, 100), 1)  # Gramas por metro quadrado
    temperature = round(random.uniform(10, 40), 1)  # Graus Celsius
    soil_moisture = round(random.uniform(0, 100), 1)  # %
    precipitation = round(random.uniform(10, 300), 1)  # Milímetros
    light = round(random.uniform(200, 800), 1)  # Nanômetros
    wood_density = round(random.uniform(0.5, 0.9), 1)  # Quilogramas por metro cúbico
    cstem = round(random.uniform(1, 15), 1)  # kgC
    
    # Garantindo que seed_germ_prop é um valor entre 1 e 100
    seed_germ_prop = round(random.uniform(1, 100), 1)  # Probabilidade de germinação (1 a 100)
    
    diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
    
    # Cálculo do slope
    slope = Kallom2 * diam ** Kallom3
    height = slope
    
    print("Generated values:")
    print('c_storage:', c_storage, 'g/m²')
    print('temperature:', temperature, '°C')
    print('soil_moisture:', soil_moisture, '%')
    print('precipitation:', precipitation, 'mm')
    print('light:', light, 'nm')
    print('wood_density:', wood_density, 'kg/m³')
    print('cstem:', cstem, 'kgC')
    print('seed_germ_prop:', seed_germ_prop, '%')
    print('diam:', diam, 'cm')
    print('height:', height, 'cm')
    
    return c_storage, temperature, soil_moisture, precipitation, light, wood_density, cstem, seed_germ_prop, diam, height

def update_pls_biomass(seedlings, pls_biomass):
    for i in range(len(seedlings)):
        pls_biomass[i] += seedlings[i]

def reproduction(c_storage, temperature, precipitation, pls_biomass, seed_bank):
    print("\nReproduction:")
    if c_storage > 0 and 23 <= temperature <= 30 and 50 <= precipitation <= 200:
        npp_rep = c_storage
        mass_seed = 0
        seedlings = []
        for _ in range(10):
            if mass_seed > 0:
                npp_rep /= mass_seed
                pls_seedbank = 1
                seedlings.append(round(pls_seedbank * (seed_germ_prop / 100), 1))
            else:
                seedlings.append(round(npp_rep, 1))
        update_pls_biomass(seedlings, pls_biomass)
        print("Produced seedlings:", seedlings)
        print("PLS Biomass after reproduction:", pls_biomass)
        return seedlings
    else:
        print("No seed production or unsuitable conditions for reproduction.")
        return [0] * 10

def germination(seed_bank, temperature, soil_moisture, pls_biomass):
    print("\nGermination:")
    if seed_bank > 0 and 25 <= temperature <= 35 and 30 <= soil_moisture <= 65:
        pls_seedbank = seed_bank
        germination_rate = seed_germ_prop / 100
        germinated_seeds = [int(pls_seedbank * germination_rate)] * 10
        seed_bank -= sum(germinated_seeds)
        update_pls_biomass(germinated_seeds, pls_biomass)
        print("Germinated seeds:", germinated_seeds)
        print("PLS Biomass after germination:", pls_biomass)
    else:
        print("Germination did not occur.")
        update_pls_biomass([0] * 10, pls_biomass)

# Valores iniciais
seed_banks = [[0] * 10]  # Lista de banco de sementes para cada ano
pls_biomass = [[] for _ in range(11)]  # Lista de listas para cada ano

# Inicializa pls_biomass para o ano 0 (dados não fornecidos no enunciado)
pls_biomass[0] = [10] * 10

# Loop anual
for year in range(1, 11): # Simulação de 10 anos
    print(f"\nYear {year}:")
    
    seed_banks.append([0] * 10)  # Inicializa o banco de sementes para o novo ano
    pls_biomass[year] = [0] * 10  # Inicializa pls_biomass para o novo ano
    
    # Loop diário para as 10 PLS
    for day in range(1, 366): # Considerando um ano com 365 dias
        print(f"\nDay {day}:")

        for i in range(10):
            c_storage, temperature, soil_moisture, precipitation, light, wood_density, cstem, seed_germ_prop, diam, height = generate_random_values()
            seedlings = reproduction(c_storage, temperature, precipitation, pls_biomass[year-1][i], seed_banks[year-1][i])
            germination(seed_banks[year-1][i], temperature, soil_moisture, pls_biomass[year][i])
            seed_banks[year][i] += sum(seedlings)

        # Atualizar o banco de sementes após o decaimento anual
        seed_banks[year] = [sb * 0.9 for sb in seed_banks[year-1]]

# TODO: Adicione aqui o código para plotar ou salvar os resultados (não fornecido no enunciado)
