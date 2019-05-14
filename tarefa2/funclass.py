class Funcionario:
    def __init__(self, nome, idDepto = None,id = None):
        self._nome = nome
        self._idDepto = idDepto
        self._id = id
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_idDepto(self):
        return self._idDepto
    def _set_idDepto(self, idDepto):
        self._idDepto = idDepto
    def __str__(self):
        return "{},{},{}".format(self.nome,self.idDepto,self.id)

    nome = property( _get_nome, _set_nome)
    idDepto = property( _get_idDepto, _set_idDepto)
    id = property( _get_id, _set_id)
