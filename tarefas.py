class Tarefas:
    def __init__(self, descricao: str, completo: bool = False):
        self.descricao = descricao
        self.completo = completo 

    def marca_completo(self):
        self.completo = True

    def __str__(self):
        status = 'OK!' if self.completo else 'X'
        return f'{status} {self.descricao}'
