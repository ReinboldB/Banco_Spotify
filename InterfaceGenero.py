from Genero import Genero
from GeneroDAO import GeneroDAO


# Classe que implementa a interface grÃ¡fica da aplicaÃ§Ã£o
class InterfaceGenero(object):

    # Método que imprime a tela inicial do cadastro de pessoas
    def menu_cadastro_genero(self):
        print("============================")
        print("Cadastro de Generos Musicais         ")
        print("============================")
        print("1 - Listar todos os gêneros musicais ")
        print("2 - Listar um gênero musical      ")
        print("3 - Inserir um gênero musical      ")
        print("4 - Atualizar um gênero musical    ")
        print("5 - Remover um gênero musical      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todos_genero()
            
        if opcao == 2:
            self.menu_listar_um_genero()
            
        if opcao == 3:
            self.menu_inserir_um_genero()
            
        if opcao == 4:
            self.menu_atualizar_um_genero()
            
        if opcao == 5:
            self.menu_remover_um_genero()
            
        if opcao == 0:
            return

    # MÃ©todo que Ã© chamado para listar as pessoas existentes
    def menu_listar_todos_genero(self):
        dao = GeneroDAO()
        print("Listando todos os gêneros musicais...")
        genero = dao.listarTodas()
        encontrou = False
        for g in genero:
            encontrou = True
            print("ID = {} - Nome = {}".format(g.id, g.nome))
        if not encontrou:
            print("Nenhum gênero musical encontrado")
        self.menu_cadastro_genero()

    # MÃ©todo que Ã© chamado para listar uma existente, filtrando pelo cÃ³digo
    def menu_listar_um_genero(self):
        dao = GeneroDAO()
        id = int(input("Digite o id do gênero: "))
        g = dao.listar(id)
        if g is None:
            print("Nenhum registro encontrado")
        else:
            print("ID = {} - Nome = {}".format(g.id, g.nome))
        self.menu_cadastro_genero()

    # MÃ©todo que Ã© chamado para inserir uma pessoa existente
    def menu_inserir_um_genero(self):
        dao = GeneroDAO()
        nome = input("Digite o nome do gênero musical: ")
        sucesso = dao.inserir(nome)
        if sucesso:
            print("Gênero musical inserido com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_genero()

    # MÃ©todo que Ã© chamado para atualizar uma pessoa existente
    def menu_atualizar_um_genero(self):
        dao = GeneroDAO()

        print("Listando todos os gêneros musicais...")
        genero = dao.listarTodas()
        encontrou = False
        for g in genero:
            encontrou = True
            print("ID = {} - Nome = {}".format(g.id, g.nome))
        if not encontrou:
            print("Nenhum gênero musical encontrado")


        id = int(input("Digite o id do gênero a ser atualizado: "))
        nome = input("Digite o novo nome do gênero a ser atualizado: ")
        sucesso = dao.atualizar(nome,id)
        if sucesso:
            print("Gênero musical atualizado com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_genero()

    # MÃ©todo que Ã© chamado para remover uma pessoa existente
    def menu_remover_um_genero(self):
        dao = GeneroDAO()

        print("Listando todos os gêneros musicais...")
        genero = dao.listarTodas()
        encontrou = False
        for g in genero:
            encontrou = True
            print("ID = {} - Nome = {}".format(g.id, g.nome))
        if not encontrou:
            print("Nenhum gênero musical encontrado")


        id = int(input("Digite o ID do gênero a ser removido: "))
        sucesso = dao.remover(id)
        if sucesso:
            print("Gênero musical removido com sucesso")
        else:
            print("Falha ao realizar esta operação")
        self.menu_cadastro_genero()


# Inicializa a aplicaÃ§Ã£o
if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal_geral()