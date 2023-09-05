import random
import math

# Constantes alométricas
Kallom2 = 40.0
Kallom3 = 0.5
pi = 3.14

years = 0
seed_bank = 0  # Inicializa o banco de sementes
c_storage = 0  # Inicializa o armazenamento de carbono

while years < 10:
    days = 0
    while days < 365:
        
        c_storage = round(random.uniform(0, 100), 1)  # Gramas por metro quadrado
        print('c_storage:', c_storage)
    
        temperature = round(random.uniform(23, 30), 1)  # Graus Celsius
        print('temperature:', temperature)
    
        precipitation = round(random.uniform(50, 200), 1)  # Milímetros
        print('precipitation:', precipitation)

        wood_density = round(random.uniform(0.5, 0.9), 1)  # Quilogramas por metro cúbico
        print('wood_density:', wood_density)
    
        cstem = round(random.uniform(1, 15), 1)  # kgC
        print('cstem:', cstem)
    
        seed_germ_prop = round(random.uniform(50, 100), 1)  # Probabilidade de germinação (50 a 100)
        print('seed_germ_prop:', seed_germ_prop)
    
        diam = round((4 * cstem) / (wood_density * pi * 40) ** 0.5 + 0.5, 1)  # Diâmetro do caule em cm
        print('diam:', diam)
    
        height = round(Kallom2 * diam ** Kallom3, 1)  # Altura em cm
        print('height:', height)

        slope = 0.1
        x = height
        y = slope * x
        mass_seed = y
        print('slope:', slope)
        
        if c_storage <= 0:
            print("Skipping day due to c_storage being <= 0")
            days += 1
            continue
        else:
            npp_rep = c_storage
        
        def reproduction(temperature, precipitation, seed_bank, seed_production, c_storage):
            print("\nReproduction:")
            print("Seed bank before reproduction:", seed_bank)
            if 23 <= temperature <= 30 and 50 <= precipitation <= 200:
                seed_production = npp_rep / mass_seed
                seed_bank += int(seed_production)  # Convertendo para inteiro
                print("seed bank after reproduction", seed_bank)
            else:
                print("Conditions not met for reproduction")
                c_storage += npp_rep  # Devolve o valor de npp_rep para c_storage
            return seed_bank, npp_rep, c_storage

            
        def germination(seed_bank, germination_temperature, seed_germ_prop):
            print("\nGermination:")
            print("Germination temperature:", germination_temperature)
            if seed_bank > 0 and 23 <= germination_temperature <= 30:
                random_value = random.uniform(0, 100)
                if random_value <= seed_germ_prop:
                    germinated_seeds = min(seed_bank, int(seed_bank * (seed_germ_prop / 100)))  # Convertendo para inteiro e limitando ao número de sementes no banco
                    seed_bank -= germinated_seeds
                    print("sementes germinadas", germinated_seeds)
                else:
                    germinated_seeds = 0
                    print("Nenhuma semente germinou")
                print("seed bank after germination", seed_bank)
            else:
                print("Não atendeu às condições de germinação")
            return seed_bank, germinated_seeds
        
        seed_bank, npp_rep, c_storage = reproduction(temperature, precipitation, seed_bank, mass_seed, c_storage)
        germination_temperature = round(random.uniform(23, 30), 1)
        seed_bank, germinated_seeds = germination(seed_bank, germination_temperature, seed_germ_prop)
        

        days += 1
        
    # Simulando decaimento anual do banco de sementes (10% das sementes)
    decayed_seeds = int(seed_bank * 0.1)
    seed_bank -= decayed_seeds
    print(f"Year {years + 1} - Decayed seeds: {decayed_seeds}")
    
    years += 1
