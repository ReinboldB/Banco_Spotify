class Compositor(object):

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
    def local_nascimento(self):
        return self._local_nascimento

    @local_nascimento.setter
    def local_nascimento(self, local_nascimento):
        self._local_nascimento = local_nascimento

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento