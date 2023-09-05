import random
import numpy as np

npp_pls = []
mass_seed = []
ano2 = []

agua = 20
npls = 5

for i in range (npls):
    npp_pls.append (round((random.uniform(0.5, 4.0)),2))
    print ('npp_pls', npp_pls)

for i in range (npls):
    mass_seed.append (round((random.uniform (0.02, 1.5)), 2))
    print('mass_seed', mass_seed)

#calcular massa total de cada pls OBS


#calcular o npp disponível para reprodução em cada pls (10%) #OBS!!!!!
npp_rep = [item * 0.1 for item in npp_pls]
print('npp_rep', npp_rep)

#calcular o n de sementes produzidas para cada pls se há npp disponivel (maior que 0)
n_seed = [A/B for A,B in zip(npp_rep, mass_seed)]
n_seed = np.array(n_seed)
print('n_seed', n_seed)

#permanecem apenas sementes viaveis do numero total anterior (60%) 
seed_bank = [item * 0.60 for item in n_seed] + ano2
print('seed_bank', seed_bank)

#proporção de germinação das sementes no banco de sementes com base na umidade do solo = 40% ideal, ver o tempo
#ver massa da semente aqui, germinação em relação a massa
#incluir umidade solo e massa? tempo de germ
    
if agua in range(30,50):
    germ_seed = seed_bank
else:
    germ_seed = (tuple (item * 0.20 for item in seed_bank))

print('germ_seed', germ_seed)

#sementes que continuam no bank_seed apos a germinação para o próximo ano
for i in range (npls):
    ano2.append ([A - B for A, B in zip (seed_bank, germ_seed)])
    print('ano2', ano2)
    

