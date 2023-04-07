class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
class Pilha:

    def __init__(self) -> None:
        self.__dados = []
    
    def tamanho(self):
        return len(self.__dados)
    
    def estaVazia(self) -> bool:
        if self.tamanho() == 0:
            raise PilhaException('A pilha está vazia')
        raise(PilhaException('A pilha não está vazia'))
    def imprime(self):
        s = ''
        s += 'Topo -> [' 
        for i in range(self.tamanho()):
            s += f'{self.__dados[i]}, '
        s = s[:-2]
        s += ' ]'
        return s

    def empilha(self, valor):
        self.__dados.append(valor)

    def desempilha(self):
        return self.__dados.pop()

    def __str__(self) -> str:
        pass