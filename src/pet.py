from owner import Owner


class Pet:
    name: str
    type: str
    breed: str
    owner: Owner

    # Iniciar o objeto com suas propriedades
    # dica: olhar os dataclasses para tornar essa tarefa mais simples
    def __init__(self, name: str, type: str, breed: str, owner: Owner) -> None:
        self.name = name
        self.type = type
        self.breed = breed
        self.owner = owner
