import traceback
import psycopg2
from Genero import Genero


# Classe que implementa o padrÃ£o Data Access Object (DAO) para a entidade pessoa
class PlaylistDAO(object):

    # Metodo que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, ordem, nome, data_criacao, tempo_total FROM playlist")
            registros = cursor.fetchall()
            for linha in registros:
                p = Playlist()
                p.id = linha[0]
                p.ordem = linha[1]
                p.nome = linha[2]
                p.data_criacao = linha[3]
                p.tempo_total = linha[4]
                resultado.append(p)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # MÃ©todo que retorna um objeto do tipo pessoa, filtrando pelo codigo
    def listar(self, id):
        p = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("SELECT id, ordem, nome, data_criacao, tempo_total FROM playlist WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                p = Playlist()
                p.id = linha[0]
                p.ordem = linha[1]
                p.nome = linha[2]
                p.data_criacao = linha[3]
                p.tempo_total = linha[4]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return p

    # MÃ©todo utilizado para inserir uma nova pessoa
    def inserir(self, ordem, nome, data_criacao, tempo_total):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO playlist (ordem, nome, data_criacao, tempo_total) VALUES ('{}', '{}', '{}', '{}')".format(ordem, nome, data_criacao, tempo_total))
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
    def atualizar(self, ordem, nome, data_criacao, tempo_total, id): 
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="brujamalabel")
            cursor = connection.cursor()
            cursor.execute("UPDATE playlist SET ordem = '{}', nome = '{}', data_criacao = '{}', tempo_total = '{}' WHERE id = {}".format(ordem, nome, data_criacao, tempo_total, id))
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