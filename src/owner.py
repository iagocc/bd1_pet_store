class Owner:
    name: str
    cpf: str
    contact: str

    # Iniciar o objeto com suas propriedades
    # dica: olhar os dataclasses para tornar essa tarefa mais simples
    def __init__(self, name: str, cpf: str, contact: str) -> None:
        self.name = name
        self.cpf = cpf
        self.contact = contact
