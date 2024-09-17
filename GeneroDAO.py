import traceback
import psycopg2
from Genero import Genero


# Classe que implementa o padrÃ£o Data Access Object (DAO) para a entidade pessoa
class GeneroDAO(object):

    # MÃ©todo que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome FROM genero")
            registros = cursor.fetchall()
            for linha in registros:
                g = Genero()
                g.id = linha[0]
                g.nome = linha[1]
                resultado.append(g)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # MÃ©todo que retorna um objeto do tipo pessoa, filtrando pelo cÃ³digo
    def listar(self, id):
        g = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome FROM genero WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                g = Genero()
                g.id = linha[0]
                g.nome = linha[1]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return g

    # MÃ©todo utilizado para inserir uma nova pessoa
    def inserir(self, nome):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO genero (nome) VALUES ('{}')".format(nome))
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
    def atualizar(self, nome, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("UPDATE genero SET nome = '{}' WHERE id = {}".format(nome, id))
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
            cursor.execute("DELETE FROM genero WHERE id = {}".format(id))
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