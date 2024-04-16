import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    """
    Classe criada para gerenciar ingestao da PokemonAPI. Cria contrato de dados para validacao de dois campos.

    - `name` - str
    
    - `type` - str
    """
    name: str
    type: str

    class Config:
        from_attributes = True # Facilitar etapa de dialogo com RM


def pegar_pokemon(id: int) -> PokemonSchema:
    """
    Obtem dados de um pokemon a partir de sua id.

    Returns:
    - `PokemonSchema` - objeto classe Python com nome e tipo do pokemon.

    """
    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)

    data = response.json()
    data_types = data["types"] # 'data' seria o dicionario com dados
    types_list = []

    for type_info in data_types:
        types_list.append(type_info["type"]["name"])
    types = ", ".join(types_list)

    return PokemonSchema(name=data["name"], type=types)


if __name__ == "__main__":
    print(pegar_pokemon(25))
