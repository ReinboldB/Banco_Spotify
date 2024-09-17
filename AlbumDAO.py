import traceback
import psycopg2
from Album import Album


# Classe que implementa o padrÃ£o Data Access Object (DAO) para a entidade pessoa
class AlbumDAO(object):

    # MÃ©todo que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id,  duracao, lancamento, nome FROM album")
            registros = cursor.fetchall()
            for linha in registros:
                a = Album()
                a.id = linha[0]
                a.duracao = linha[1]
                a.lancamento = linha[2]
                a.nome = linha[3]
                resultado.append(a)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # Metodo que retorna um objeto do tipo pessoa, filtrando pelo codigo
    def listar(self, id):
        a = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, duracao, lancamento FROM album WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                a = Album()
                a.id = linha[0]
                a.nome = linha[1]
                a.duracao = linha[2]
                a.lancamento = linha[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return a

    # MÃ©todo utilizado para inserir uma nova pessoa
    def inserir(self, nome, duracao, lancamento):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO album (nome, duracao, lancamento) VALUES ('{}','{}', '{}')".format(nome, duracao, lancamento))
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
    def atualizar(self, nome, duracao, lancamento, id): 
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("UPDATE album SET nome = '{}', duracao = '{}', lancamento = '{}' WHERE id = {}".format(nome, duracao, lancamento, id))
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
            cursor.execute("DELETE FROM album WHERE id = {}".format(id))
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