class Coisa:

    def __repr__(self) -> str:
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def estaVivo(self):
        return hasattr(self, 'vivo') and self.vivo