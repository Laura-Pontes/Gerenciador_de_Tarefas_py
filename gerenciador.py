from tarefas import Tarefas

class Gerenciador:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, descricao: str):
        descricao = descricao.strip()
        if not descricao:
            raise ValueError('Adicione uma descrição.')
        tarefa = Tarefas(descricao)
        self.tarefas.append(tarefa)
        return tarefa
    
    def listar(self):
        if not self.tarefas:
            print('Você não tem nenhuma atividade/tarefa adicionada.')
            return
        for i, t in enumerate(self.tarefas, 1):
            status = 'Completa' if t.completo else 'Incompleta'
            print(f'{i}. [{status}] {t.descricao}')

    def completar(self, numero: int):
        if numero < 1 or numero > len(self.tarefas):
            raise IndexError('Verifique se o número da atividade/tarefa está correto.')
        self.tarefas[numero - 1].marca_completo()