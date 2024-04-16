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