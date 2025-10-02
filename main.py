from gerenciador import Gerenciador

def menu():
    print('MENU')
    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefas')
    print('3 - Completar Tarefa')
    print('4 - sair')

def main():
    gerenciador = Gerenciador()
    while True:
        menu()
        escolha = input('Escolha uma opção digitando os números de 1 a 4: ').strip()

        if escolha == '1':
            desc = input('Descrição da tarefa: ').strip()
            try:
                gerenciador.adicionar(desc)
                print('Tarefa adicionada com sucesso!')
            except ValueError as e:
                print('Erro:', e)

        elif escolha == '2':
            gerenciador.listar()

        elif escolha == '3':
            gerenciador.listar()
            if not gerenciador.tarefas:
                    continue
            num_str = input('Número da tarefa para marcar como completa: ').strip()
            if not num_str.isdigit():
                print('Digite um número válido!')
                continue
            num = int(num_str)
            try:
                gerenciador.completar(num)
                print('Tarefa marcada como completa!')
            except IndexError:
                print('Número da tarefa inválido!')

        elif escolha == '4':
            print('Saindo...')
            break

        else:
            print('Digite uma opção válida. 1, 2, 3 ou 4')

if __name__== '__main__':
    main()