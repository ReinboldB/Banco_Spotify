class Album(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def lancamento(self):
        return self._lancamento

    @lancamento.setter
    def lancamento(self, lancamento):
        self._lancamento = lancamento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome