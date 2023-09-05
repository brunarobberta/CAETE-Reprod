npp_pls = [10, 80, 5]
mass_seed = [0.1, 1, 3]
  
npp_rep = [npp_pls * 0.1 / mass_seed for npp_pls, mass_seed in zip(npp_pls, mass_seed)]

print(npp_rep)

randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
#def rep(npp_pls):
#    if npp_pls > 0: 
#        print('npp total', npp_rep)
#        print('10% npp é', npp_pls)
#    else: 
#        print('não ha sementes')

#rep(npp_pls)

