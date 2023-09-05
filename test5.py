quantidade_de_repetições = 10 
while quantidade_de_repetições > 0:


    npp_pls = [10,80,5]
    mass_seed= [0.1,1,3]
    
    new_results = [x / y for x, y in zip(npp_pls, mass_seed)]
    
    npp_pls = [npp_rep * 0.1 for npp_rep in npp_pls]
    
    print(new_results)

    quantidade_de_repetições -= 1
    
##############teste 6

    else:
        print(tuple (item * 0.50 for item in seed_bank))

          else:
       print(tuple (item * 0.50 for item in germ_seed))