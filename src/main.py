import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1, 350) # Gerar id aleatorio entre 1 e 350 (numero de pokemons)
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f"Adicionando {pokemon_schema} ao banco de dados")
            add_pokemon_to_db(pokemon_schema)
        else:
            print(f"Nao foi possivel obter dados para o Pokemon com ID {pokemon_id}")
        time.sleep(10)
    
if __name__ == "__main__":
    main()