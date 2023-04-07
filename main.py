from pilhaSequencial import Pilha, PilhaException
a = Pilha()
try:
    print('estaVazia: ',a.estaVazia())
except PilhaException as pe:
    print(pe)
print('tamanho: ',a.tamanho())
for i in range(1, 10+1):
    a.empilha(i)
print('Elementos na pilha: ',a.tamanho())
try:
    print(a.estaVazia())
except PilhaException as pe:
    print(pe)
print(a.imprime())
print('desempilhado: ',a.desempilha())
print(a.imprime())