class Playlist(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def ordem(self):
        return self._ordem

    @ordem.setter
    def ordem(self, ordem):
        self._ordem = ordem

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_criacao(self):
        return self._data_criacao

    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self._data_criacao = data_criacao

    @property
    def tempo_total(self):
        return self._tempo_total

    @tempo_total.setter
    def tempo_total(self, tempo_total):
        self._tempo_total = tempo_total