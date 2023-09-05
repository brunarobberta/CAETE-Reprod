import random
import numpy as np

n_pls = 4
mass_seed  = np.random.randint(1,52, (4))
npp = (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1))
#npp = random.uniform(0, 5), random.uniform(0, 6)

anos = 10
while anos < 10:
    #    while n_pls < 4:

    n_pls = 4
    mass_seed  = np.random.randint(1,52, (4))
    npp = (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1)), (round(random.uniform(0,5),1))





    #calcular o npp disponível para reprodução em cada pls (10%)
    npp_rep = [item * 0.1 for item in npp] 
    print(npp_rep)

    ab = [1,2]
    print(ab)

        














    anos +=1 
