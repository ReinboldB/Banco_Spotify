import traceback
import psycopg2
from Musica import Musica


# Classe que implementa o padrÃ£o Data Access Object (DAO) para a entidade pessoa
class MusicaDAO(object):

    # MÃ©todo que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, duracao, data_criacao FROM musica")
            registros = cursor.fetchall()
            for linha in registros:
                m = Musica()
                m.id = linha[0]
                m.nome = linha[1]
                m.duracao = linha[2]
                m.data_criacao = linha[3]
                resultado.append(m)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # Metodo que retorna um objeto do tipo pessoa, filtrando pelo codigo
    def listar(self, id):
        m = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, duracao, data_criacao FROM musica WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                m = Genero()
                m.id = linha[0]
                m.nome = linha[1]
                m.duracao = linha[2]
                m.data_criacao = linha[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return m

    # MÃ©todo utilizado para inserir uma nova pessoa
    def inserir(self, nome, duracao, data_criacao):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO musica (nome, duracao, data_criacao) VALUES ('{}', '{}', '{}')".format(nome, duracao, data_criacao))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # MÃ©todo utilizado para atualizar os dados de nome, login e senha de uma pessoa existente
    def atualizar(self, nome, duracao, data_criacao, id): 
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("UPDATE musica SET nome = '{}', duracao = '{}', data_criacao = '{}' WHERE id = {}".format(nome, duracao, data_criacao, id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # MÃ©todo utilizado para remover uma pessoa existente
    def remover(self, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM musica WHERE id = {}".format(id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso