import random
import math
#import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

n_pls = 10
years = 0
total_carbon_accumulated = {'root': [0] * n_pls, 'leaf': [0] * n_pls, 'cstem': [0] * n_pls}


liteira = {}  # Inicialize o dicionário da liteira
pls = []

# Definindo as taxas de turnover (tempo de residência do C em anos) para os compartimentos
taxa_turnover_npp_leaf = 2.0 # Sugestão da Bia
taxa_turnover_npp_root = 2.0 # Sugestão da Bia
taxa_turnover_npp_cstem = 50.0 # Sugestão da Bia


# Geração das propriedades dos PLSs
for i in range(n_pls):
    wood_density = round(random.uniform(0.34, 1.06), 1)  # g/cm3
    wood_density = wood_density * 1000000  # Converte para grama por m3
    wood_density = wood_density / 2 #converte em gC/m3, para posteriormente calcular o diâmetro do caule, segundo Smith et al (2001)

    npp_init_ = round(random.uniform(0.5, 1.3), 1)  # quilogramas de carbono por m2
    npp_init = npp_init_ * 1000  # converte para gramas de carbono por m2

    #biomassa total: carbono no caule, raiz, folha
    #caule 35% cstem 
    #raiz 34%
    #folha 27%
    npp_root = npp_init * 0.34
    npp_leaf = npp_init * 0.27
 #De acordo com os levantamentos realizados de 2015 a 2022 nos plots da área experimental do AmazonFACE, a NPP anual corresponde a: 35% wood, 34% Fine roots, 27% leaves, 4% Reproduction
    npp_cstem = npp_init * 0.35
    npp_rep = npp_init * 0.04


    diam = (4 * npp_cstem) / (wood_density * pi * Kallom2)
    diam = diam ** (1 / (2 + Kallom3))

    height = Kallom2 * (diam ** Kallom3)

    # Cálculo da massa da semente
    mass_seed = (height / (10 ** 0.08)) ** (1 / 0.43) #massa da semente em mg
    print("mass_seed antes de kg", mass_seed )
    mass_seed = mass_seed / 1000000 #transformando em kg
    

    WD_to_print = wood_density/1000
    log_mass_seed = math.log(mass_seed * 1000000,10)

    pls.append({
        'seed_bank': 0,
        'npp_init_': npp_init_,
        'npp_init': npp_init,
        'npp_rep': npp_rep,
        'npp_root': npp_root,
        'npp_leaf': npp_leaf,
        #'total_biomass': total_biomass,
        'mass_seed': mass_seed,
        #'wood_density': wood_density,
        'wood_density': WD_to_print, #in Kg/m3
        'npp_cstem': npp_cstem,
        'diam': diam,
        'height': height,
        'npp_cstem': npp_cstem,
        'diam_': diam_,
        'log_mass_seed': log_mass_seed,
        'npp_root_year': 0,  
        'npp_leaf_year': 0,
        'npp_cstem_year': 0,
        'carbon_accumulated_root': 0,  
        'carbon_accumulated_leaf': 0,
        'carbon_accumulated_cstem': 0,
    })

def reproduction(temperature, precipitation, seed_bank, mass_seed, npp_rep):
    seed_production = 0  # Valor padrão para seed_production
    if 24 <= temperature <= 33 and 60 <= precipitation <= 200 and npp_rep > 0:
        seed_production = npp_rep / mass_seed
        seed_bank += int(seed_production)  # Convertendo para inteiro
    return seed_bank, seed_production, npp_rep


def germination(seed_bank, temperature):
    if seed_bank > 0 and 23 <= temperature <= 30:
        germinated_seeds = int(seed_bank * 0.5)  # 50% das sementes no banco
        seed_bank -= germinated_seeds  # Subtrair as sementes germinadas do banco
        return germinated_seeds
    return 0

# Lista para armazenar os dados para o gráfico
data_points = []


while years < 10:

    # Inicialize as variáveis de acumulação no início de cada ano
    for pls_id, plss in enumerate(pls):
        plss['carbon_accumulated_root'] = 0
        plss['carbon_accumulated_leaf'] = 0
        plss['carbon_accumulated_cstem'] = 0

    for pls_id, plss in enumerate(pls):
        # Valores de npp por ano para incremento de carbono na planta
        npp_year_ = round(random.uniform(0.5, 1.3), 1)  # quilogramas de carbono por m2
        npp_year = npp_year_ * 1000  # converte para gramas de carbono por m2

        npp_root_year = npp_year * 0.34
        npp_leaf_year = npp_year * 0.27
        npp_cstem_year = npp_year * 0.35

        # Atualizando os valores de carbono nos compartimentos considerando o incremento anual
        plss['npp_root'] += npp_root_year
        plss['npp_leaf'] += npp_leaf_year
        plss['npp_cstem'] += npp_cstem_year

        # Atualização das variáveis de carbono acumulado
        plss['carbon_accumulated_root'] += npp_root_year + total_carbon_accumulated['root'][pls_id]
        plss['carbon_accumulated_leaf'] += npp_leaf_year + total_carbon_accumulated['leaf'][pls_id]
        plss['carbon_accumulated_cstem'] += npp_cstem_year + total_carbon_accumulated['cstem'][pls_id]

        # Atualizando o total acumulado para o próximo ano
        total_carbon_accumulated['root'][pls_id] = plss['carbon_accumulated_root']
        total_carbon_accumulated['leaf'][pls_id] = plss['carbon_accumulated_leaf']
        total_carbon_accumulated['cstem'][pls_id] = plss['carbon_accumulated_cstem']

        # Print da taxa de acumulação individual para cada planta
        print(f"Início do Ano {years + 1} - Taxa de Acumulação - PLS {pls_id + 1} - Root: {plss['carbon_accumulated_root']} gC, Leaf: {plss['carbon_accumulated_leaf']} gC, Cstem: {plss['carbon_accumulated_cstem']} gC", end='\r')

    # Verificação do turnover anual segundo smith 2001 Cnew=Cold×(1−turnc)
    if years % 2 == 0:
        print("\nTurnover aconteceu no ano", years)
        for pls_id, plss in enumerate(pls):
            turnover_carbon_leaf = plss['npp_leaf'] * taxa_turnover_npp_leaf
            turnover_carbon_root = plss['npp_root'] * taxa_turnover_npp_root
            plss['npp_leaf'] *= (1 - taxa_turnover_npp_leaf)
            plss['npp_root'] *= (1 - taxa_turnover_npp_root)
            plss['carbon_accumulated_root'] -= turnover_carbon_root
            plss['carbon_accumulated_leaf'] -= turnover_carbon_leaf
            # Enviar para a liteira
            liteira[pls_id] = liteira.get(pls_id, 0) + turnover_carbon_leaf + turnover_carbon_root
            # Print do turnover da folha, raiz e caule
            print(f"Turnover na folha (pls {pls_id + 1}): {turnover_carbon_leaf} gC")
            print(f"Turnover na raiz (pls {pls_id + 1}): {turnover_carbon_root} gC")

    if years % 50 == 0:
        print("\nTurnover cstem aconteceu no ano", years)
        for pls_id, plss in enumerate(pls):
            turnover_carbon_cstem = plss['npp_cstem'] * taxa_turnover_npp_cstem
            plss['npp_cstem'] *= (1 - taxa_turnover_npp_cstem)
            plss['carbon_accumulated_cstem'] -= turnover_carbon_cstem
            # Enviar para a liteira
            liteira[pls_id] = liteira.get(pls_id, 0) + turnover_carbon_cstem
            # Print do turnover do cstem
            print(f"Turnover no cstem (pls {pls_id + 1}): {turnover_carbon_cstem} gC")


################reduzIndo a biomassa das folhas e raízes a cada dois anos e 
#a biomassa do caule a cada 50 anos, simulando a perda de biomassa nas plantas ao longo do tempo. 

#####ajustar a quantidade de carbono nos diferentes compartimentos da planta. 
# O cálculo � new = � old × ( 1 − turn � ) C new ​ =C old ​ ×(1−turn t ​ ) calcula a nova quantidade de carbono ( � new C new ​ ) 
# com base na quantidade antiga de carbono ( � old C old ​ ) 
#e na taxa de turnover ( turn � turn t ​ ) para um determinado tipo de tecido



    for day in range(365):
        temperature = round(random.uniform(21, 35), 1)  # Graus Celsius
        precipitation = round(random.uniform(45, 250), 1)  # Milímetros
        print("------------------------------------------------------------------------------")
        for pls_id, plss in enumerate(pls):
            if years != 0 and day == 0:
                decayed_seeds = int(plss['seed_bank'] * 0.5)
                print(f"Banco de sementes antes do decaimento das sementes (pls {pls_id + 1}): {plss['seed_bank']}")
                plss['seed_bank'] -= decayed_seeds
                print(f"Banco de sementes após do decaimento das sementes (pls {pls_id + 1}): {plss['seed_bank']}")

                print(f"Ano {years + 1} (plss {pls_id + 1}) - Sementes decaídas: {decayed_seeds}")

  
                # Atualize a liteira para a planta atual
                if pls_id not in liteira:
                    liteira[pls_id] = decayed_seeds
                else:
                    liteira[pls_id] += decayed_seeds

                print(f"Liteira após decaimento (pls {pls_id + 1}): {liteira.get(pls_id, 0)}")

            
            print(f"Espécie {pls_id + 1} - Ano {years + 1}, Dia {day + 1}")
            print("temperatura:", temperature, "°C")
            print("precipitação:", precipitation, "mm")
            print("densidade da madeira:", plss['wood_density'], "kg/m³")
            print("npp_cstem", plss['npp_cstem'], "gC")
            print("npp_root", plss['npp_root'], "gC")
            print("npp_leaf", plss['npp_leaf'], "gC")
            print("npp_cstem:", plss['npp_cstem'], "gC")
            print("diam:", plss['diam'], "m")
            print("altura:", plss['height'], "m")
            print("massa da semente:", plss['mass_seed'], "Kg")
            print("npp_rep", plss['npp_rep'])
            print("npp_init", plss ['npp_init'])
            print("npp_init_", plss ['npp_init_'])
            print("npp_root_year", plss['npp_root_year'])
            print("npp_leaf_year", plss['npp_leaf_year'])
            print("npp_cstem_year", plss['npp_cstem_year'])

            


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
                    'mass_seed': plss['mass_seed'],
                    'log_mass_seed': plss['log_mass_seed'],
                    'height': plss['height'], 
                })



    years += 1


wood_densities = [point['wood_density'] for point in data_points]
mass_seeds = [point['log_mass_seed'] for point in data_points]

Heights = [point['height'] for point in data_points]


# Ajuste uma regressão linear para o primeiro gráfico
coefficients_plot1 = np.polyfit(wood_densities, mass_seeds, 1)
poly_plot1 = np.poly1d(coefficients_plot1)

# Calcule o R² para o primeiro gráfico
slope, intercept, r_value, p_value, std_err = stats.linregress(wood_densities, mass_seeds)
r_squared_plot1 = r_value**2

# Plotagem do primeiro gráfico
plt.figure(figsize=(10, 6))
plt.scatter(wood_densities, mass_seeds, color='darkorange', label='Dados simulados')
plt.plot(wood_densities, poly_plot1(wood_densities), color='darkblue', label=f'Regressão Linear (R²={r_squared_plot1:.2f})')
plt.xlabel('Densidade da Madeira (kg/m³)')
plt.ylabel('Massa da Semente (mg) [log scale]')
plt.legend()
plt.grid(alpha=0.5)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

# Ajuste uma regressão linear para o segundo gráfico
coefficients_plot2 = np.polyfit(mass_seeds, Heights, 1)
poly_plot2 = np.poly1d(coefficients_plot2)

# Calcule o R² para o segundo gráfico
slope, intercept, r_value, p_value, std_err = stats.linregress(mass_seeds, Heights)
r_squared_plot2 = r_value**2

# Plotagem do segundo gráfico
plt.figure(figsize=(10, 6))
plt.scatter(mass_seeds, Heights, color='darkorange', label='Dados simulados')
plt.plot(mass_seeds, poly_plot2(mass_seeds), color='darkblue', label=f'Regressão Linear (R²={r_squared_plot2:.2f})')
plt.xlabel('Massa da Semente (mg) [log scale]')
plt.ylabel('Altura do PLS (m)')
plt.legend()
plt.grid(alpha=0.5)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

plt.legend()
plt.grid(True)
plt.show()

