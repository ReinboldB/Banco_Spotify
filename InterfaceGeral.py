from InterfaceMusica import InterfaceMusica
from InterfaceGenero import InterfaceGenero

class Interface(object):
    
    # Método que imprime a tela inicial da aplicação
    def menu_principal_geral(self):
        print("========================")
        print("Spotify")
        print("========================")
        print("1 - Música ")
        print("2 - Gênero ")
        print("0 - Sair")
        print("========================")


        opcao = int(input("Digite uma opção [0-2]: "))  # Ajuste aqui para incluir '2'
        
        if opcao == 1:
            # Cria uma instância de InterfaceMusica e chama o método menu_principal
            musica_interface = InterfaceMusica()
            musica_interface.menu_cadastro_musica()
            self.menu_principal_geral()
            return
        if opcao == 2:
            genero_interface = InterfaceGenero()
            genero_interface.menu_cadastro_genero()
            self.menu_principal_geral()
            return
        if opcao == 0:
            self.menu_principal_geral()
            return 
        # Se a opção não for válida, chama novamente o menu
        self.menu_principal_geral()

# Inicializa a aplicação
if __name__ == '__main__':
    gui = Interface()
    gui.menu_principal_geral()