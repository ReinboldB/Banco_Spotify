from Musica import Musica
from MusicaDAO import MusicaDAO


# Classe que implementa a interface grÃ¡fica da aplicaÃ§Ã£o
class InterfaceGrafica(object):

    # MÃ©todo que imprime a tela inicial da aplicaÃ§Ã£o
    def menu_principal(self):
        print("========================")
        print("Cadastro de Música    ")
        print("========================")
        print("1 - Cadastrar Música ")
        print("0 - Sair")
        print("========================")
        opcao = int(input("Digite uma opção [0-1]: "))
        if opcao == 1:
            self.menu_cadastro_musica()
            return
        if opcao == 0:
            return
        self.menu_principal()

    # MÃ©todo que imprime a tela inicial do cadastro de pessoas
    def menu_cadastro_musica(self):
        print("============================")
        print("Cadastro de Música         ")
        print("============================")
        print("1 - Listar todas as músicas ")
        print("2 - Listar uma música      ")
        print("3 - Inserir uma música      ")
        print("4 - Atualizar a lista de músicas    ")
        print("5 - Remover uma música      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todas_musica()
            return
        if opcao == 2:
            self.menu_listar_uma_musica()
            return
        if opcao == 3:
            self.menu_inserir_uma_musica()
            return
        if opcao == 4:
            self.menu_atualizar_uma_musica()
            return
        if opcao == 5:
            self.menu_remover_uma_musica()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_cadastro_musica()

    # MÃ©todo que Ã© chamado para listar as pessoas existentes
    def menu_listar_todas_musica(self):
        dao = MusicaDAO()
        print("Listando todas as músicas...")
        musica = dao.listarTodas()
        encontrou = False
        for m in musica:
            encontrou = True
            print("ID = {} - Nome = {} - Duração = {} - Data de Criação = {}".format(m.id, m.nome, m.duracao, m.data_criacao))
        if not encontrou:
            print("Nenhuma música encontrada")
        self.menu_cadastro_musica()

    # MÃ©todo que Ã© chamado para listar uma existente, filtrando pelo cÃ³digo
    def menu_listar_uma_musica(self):
        dao = MusicaDAO()
        id = int(input("Digite o id da música: "))
        m = dao.listar(codigo)
        if m is None:
            print("Nenhum registro encontrado")
        else:
            print("ID = {} - Nome = {} - Duração = {} - Data de Criação = {}".format(m.id, m.nome, m.duracao, m.data_criacao))
        self.menu_cadastro_musica()

    # MÃ©todo que Ã© chamado para inserir uma pessoa existente
    def menu_inserir_uma_musica(self):
        dao = MusicaDAO()
        nome = input("Digite o nome da música: ")
        duracao = input("Digite a duração da música: ")
        data_criacao = input("Digite a data de criação da música: ")
        sucesso = dao.inserir(nome,duracao,data_criacao)
        if sucesso:
            print("Música inserida com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_musica()

    # MÃ©todo que Ã© chamado para atualizar uma pessoa existente
    def menu_atualizar_uma_musica(self):
        dao = MusicaDAO()

        print("Listando todas as músicas...")
        musica = dao.listarTodas()
        encontrou = False
        for m in musica:
            encontrou = True
            print("ID = {} - Nome = {} - Duração = {} - Data de Criação = {}".format(m.id, m.nome, m.duracao, m.data_criacao))
        if not encontrou:
            print("Nenhuma música encontrado")


        id = int(input("Digite o id da música a ser atualizada: "))
        nome = input("Digite o novo nome da música: ")
        duracao = input("Digite a nova duração da música: ")
        data_criacao = input("Digite a nova data de criação da música: ")
        sucesso = dao.atualizar(nome, duracao,data_criacao,id)
        if sucesso:
            print("Música atualizada com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_musica()

    # MÃ©todo que Ã© chamado para remover uma pessoa existente
    def menu_remover_uma_musica(self):
        dao = MusicaDAO()

        print("Listando todas as músicas...")
        musica = dao.listarTodas()
        encontrou = False
        for m in musica:
            encontrou = True
            print("ID = {} - Nome = {} - Duração = {} - Data de Criação = {}".format(m.id, m.nome, m.duracao, m.data_criacao))
        if not encontrou:
            print("Nenhuma música encontrado")


        id = int(input("Digite o ID da música a ser removida: "))
        sucesso = dao.remover(id)
        if sucesso:
            print("Música removida com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_musica()


# Inicializa a aplicaÃ§Ã£o
if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal()