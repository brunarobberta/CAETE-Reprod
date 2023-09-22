import random
import math
#import pandas as pd 
import numpy as np
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
    #wood_density = round(random.uniform(0.5, 0.9), 1)  # Quilogramas por metro cúbico
    wood_density = round(random.uniform(0.34, 1.06), 1)  # g/cm3
    wood_density = wood_density * 1000000  # Converte para grama por m3
    wood_density = wood_density / 2 #converte em gC/m3
    wood_density = wood_density / 1000 #converte em kg/m3
    npp_disponivel = round(random.uniform(0, 1.3), 1)  # quilogramas de carbono por m2
    npp_disponivel = npp_disponivel * 1000  # converte para gramas de carbono por m2
    npp_cstem = npp_disponivel * 0.35
    npp_rep = (npp_disponivel - npp_cstem) * 0.10  # 10% do que sobra após a alocação para c_stem
    cstem = npp_cstem 
    #cstem = round(random.uniform(5, 20), 1)  # kgC
    #cstem = cstem * 1000  # Converte em g de carbono
    #diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
    diam = round(4 * cstem * 1.0e3) / (wood_density * 1.0e6 * pi * Kallom2)**(1 / (2 + Kallom3))

    height = round(Kallom2 * diam ** Kallom3, 1)  # Altura em cm

    # Cálculo da massa da semente
    #mass_seed = (height / 10) ** 0.08 ** (1 / 0.43)
    mass_seed = (10 ** (0.08 * (height / 10))) ** (1 / 0.43)


    pls.append({
        'seed_bank': 0,
        'npp_disponivel': npp_disponivel,
        'npp_rep': npp_rep,
        'mass_seed': mass_seed,
        'wood_density': wood_density,
        'cstem': cstem,
        'diam': diam,
        'height': height,
        'npp_cstem': npp_cstem,
    })

def reproduction(temperature, precipitation, seed_bank, mass_seed, npp_rep):
    seed_production = 0  # Valor padrão para seed_production
    if 23 <= temperature <= 30 and 50 <= precipitation <= 200 and npp_rep <= 0:
        seed_production = npp_rep / mass_seed
        seed_bank += int(seed_production)  # Convertendo para inteiro
    return seed_bank, seed_production, npp_rep


def germination(seed_bank, temperature):
    if seed_bank > 0 and 23 <= temperature <= 30:
        germinated_seeds = int(seed_bank * 0.5)  # 50% das sementes no banco
        seed_bank -= germinated_seeds  # Subtrair as sementes germinadas do banco
        return germinated_seeds
    return 0
####inserie as q nao germinam vao pra liteira

# Lista para armazenar os dados para o gráfico
data_points = []


while years < 10:
    for day in range(365):
        temperature = round(random.uniform(20, 40), 1)  # Graus Celsius
        precipitation = round(random.uniform(50, 250), 1)  # Milímetros
        print("------------------------------------------------------------------------------")
        for pls_id, plss in enumerate(pls):
            if years != 0 and day == 0:
                decayed_seeds = int(plss['seed_bank'] * 0.5)
                print(f"Banco de sementes antes do decaimento das sementes (pls {pls_id + 1}): {plss['seed_bank']}")
                plss['seed_bank'] -= decayed_seeds
                print(f"Banco de sementes após do decaimento das sementes (pls {pls_id + 1}): {plss['seed_bank']}")

                print(f"Ano {years + 1} (plss {pls_id + 1}) - Sementes decaídas: {decayed_seeds}")


            #npp_disponivel = round(random.uniform(0, 1.3), 1)  # quilogramas de carbono por m2
            #npp_disponivel = npp_disponivel * 1000  # converte para gramas de carbono por m2
            #npp_cstem = npp_disponivel * 0.35
            #npp_disponivel -= npp_cstem
            #npp_rep = npp_disponivel * 0.1

            #germination_temperature = round(random.uniform(23, 30), 1)  # Graus Celsius

        #    if npp_rep <= 0:
        #        continue
        #    else:
        #        plss['npp_rep'] = npp_rep

            print(f"Espécie {pls_id + 1} - Ano {years + 1}, Dia {day + 1}")
            print("temperatura:", temperature, "°C")
            print("precipitação:", precipitation, "mm")
            print("densidade da madeira:", plss['wood_density'], "kg/m³")
            print("npp_cstem", plss['npp_cstem'], "gC")
            print("cstem:", plss['cstem'], "gC")
            print("diam:", plss['diam'], "cm")
            print("altura:", plss['height'], "cm")
            print("massa da semente:", plss['mass_seed'], "g")
            print("npp_rep", plss['npp_rep'])
            print("npp_disponivel", plss ['npp_disponivel'])

            print("\nReprodução:")
            print(f"Banco de sementes antes da reprodução (pls {pls_id + 1}): {plss['seed_bank']}")
            plss['seed_bank'], seed_production, plss['npp_rep'] = reproduction(temperature, precipitation, plss['seed_bank'], plss['mass_seed'], plss['npp_rep'])
            print(f"Sementes produzidas (pls {pls_id + 1}): {int(seed_production)}")
            print(f"Banco de sementes após a reprodução (pls {pls_id + 1}): {plss['seed_bank']}")

            print("\nGerminação:")
            germinated_seeds = germination(plss['seed_bank'], temperature)
            print(f"Banco de sementes antes de subtrair sementes germinadas (pls {pls_id + 1}): {plss['seed_bank']}")
            print(f"Sementes germinadas (pls {pls_id + 1}): {germinated_seeds}")
            plss['seed_bank'] -= germinated_seeds
            print(f"Banco de sementes após subtrair sementes germinadas (pls {pls_id + 1}): {plss['seed_bank']}")
        

        # Loop sobre as espécies e coleta de dados relevantes
            for plss in pls:
                data_points.append({
                    'wood_density': plss['wood_density'],
                    'mass_seed': plss['mass_seed']
                })

    years += 1

# Separa os dados em listas para os eixos x e y
wood_densities = [point['wood_density'] for point in data_points]
mass_seeds = [point['mass_seed'] for point in data_points]

# Ajuste uma regressão linear
coefficients = np.polyfit(wood_densities, mass_seeds, 1)
poly = np.poly1d(coefficients)

# Plota o gráfico com a linha de regressão
plt.figure(figsize=(10, 6))
plt.scatter(wood_densities, mass_seeds, color='blue', marker='o', label='Dados')
plt.plot(wood_densities, poly(wood_densities), color='red', label='Regressão Linear')
plt.title('Trade-off entre Massa da Semente e Densidade da Madeira')
plt.xlabel('Densidade da Madeira (kg/m³)')
plt.ylabel('Massa da Semente (g)')
plt.legend()
plt.grid(True)
plt.show()
