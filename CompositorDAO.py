import traceback
import psycopg2
from Compositor import Compositor


# Classe que implementa o padrÃ£o Data Access Object (DAO) para a entidade pessoa
class CompositorDAO(object):

    # Metodo que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, local_nascimento, data_nascimento FROM compositor")
            registros = cursor.fetchall()
            for linha in registros:
                c = Compositor()
                c.id = linha[0]
                c.nome = linha[1]
                c.local_nascimento = linha[2]
                c.data_nascimento = linha[3]
                resultado.append(c)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # MÃ©todo que retorna um objeto do tipo Compositor, filtrando pelo codigo
    def listar(self, id):
        c = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, local_nascimento, data_nascimento FROM compositor WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                c = Compositor()
                c.id = linha[0]
                c.nome = linha[1]
                c.local_nascimento = linha[2]
                c.data_nascimento = linha[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    # MÃ©todo utilizado para inserir uma nova pessoa
    def inserir(self, nome, local_nascimento, data_nascimento):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO compositor (nome, local_nascimento, data_nascimento) VALUES ('{}', '{}', '{}')".format(nome, local_nascimento, data_nascimento))
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
    def atualizar(self, nome, local_nascimento, data_nascimento, id): # precisa deixar o id aqui?
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("UPDATE playlist SET nome = '{}', local_nascimento = '{}', data_nascimento = '{}' WHERE id = {}".format(nome, local_nascimento, data_nascimento, id))
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

    # Metodo utilizado para remover uma pessoa existente
    def remover(self, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM playlist WHERE id = {}".format(id))
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