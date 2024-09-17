class Musica(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def data_criacao(self):
        return self._data_criacao

    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self._data_criacao = data_criacao