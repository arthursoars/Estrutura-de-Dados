class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def adicionar_no_final(self, dado):
        novo_nodo = Nodo(dado)

        if self.cabeca is None:  # Adicionar no início se a lista estiver vazia
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def adicionar_na_posicao(self, dado, posicao):
        novo_nodo = Nodo(dado)
        tamanho = self.obter_tamanho()

        if posicao < 0 or posicao > tamanho:
            raise IndexError("Posição inválida")

        if posicao == 0:  # Adicionar no início
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            contador = 0
            while atual is not None and contador < posicao - 1:
                atual = atual.proximo
                contador += 1
            if atual is None:
                raise IndexError("Posição inválida")
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def remover_na_posicao(self, posicao):
        tamanho = self.obter_tamanho()

        if posicao < 0 or posicao >= tamanho:
            raise IndexError("Posição inválida")

        if posicao == 0:  # Remover do início
            self.cabeca = self.cabeca.proximo
        else:
            atual = self.cabeca
            anterior = None
            contador = 0
            while atual is not None and contador < posicao:
                anterior = atual
                atual = atual.proximo
                contador += 1
            if atual is None:
                raise IndexError("Posição inválida")
            anterior.proximo = atual.proximo

    def esta_vazia(self):
        return self.cabeca is None

    def obter_tamanho(self):
        tamanho = 0
        atual = self.cabeca
        while atual is not None:
            tamanho += 1
            atual = atual.proximo
        return tamanho
    
    def acessar_elemento(self, posicao):
        if posicao < 0 or posicao >= self.obter_tamanho():
            raise IndexError("Posição inválida")

        atual = self.cabeca
        contador = 0
        while atual is not None:
            if contador == posicao:
                return atual.dado
            contador += 1
            atual = atual.proximo
        raise IndexError("Posição inválida")
    
    def alterar_elemento(self, posicao, novo_dado):
        if posicao < 0 or posicao >= self.obter_tamanho():
            raise IndexError("Posição inválida")

        atual = self.cabeca
        contador = 0
        while atual is not None:
            if contador == posicao:
                atual.dado = novo_dado
                return
            contador += 1
            atual = atual.proximo
        raise IndexError("Posição inválida")

    def mostrar_lista(self):
        if self.esta_vazia():
            print("Lista vazia")
        else:
            elementos = []
            atual = self.cabeca
            while atual is not None:
                elementos.append(atual.dado)
                atual = atual.proximo
            print(elementos)

def executar_testes():
    lista = ListaLigada()

    # Adicionar elementos no final
    lista.adicionar_no_final(35)
    lista.adicionar_no_final(10)
    lista.adicionar_no_final(20)
    lista.adicionar_no_final(30)
    print("Elementos da lista:")
    lista.mostrar_lista()

    # Obter tamanho da lista
    print("Tamanho da lista: ", lista.obter_tamanho())

    # Verificar se a lista está vazia
    print("A lista está vazia?", lista.esta_vazia())

    # Obter elemento em uma posição
    print("Elemento na posição 2: ", lista.acessar_elemento(2))
    print("Elemento na posição 3: ", lista.acessar_elemento(3))

    # Alterar elemento em uma posição
    print("Alterando o elemento na posição 2 para 314")
    lista.alterar_elemento(2, 314)
    lista.mostrar_lista()

    # Remover elemento em uma posição
    print("Removendo o elemento na posição 3")
    lista.remover_na_posicao(3)
    lista.mostrar_lista()

    # Adicionar na posição específica
    print("Adicionando 50 na posição 2")
    lista.adicionar_na_posicao(50, 2)
    lista.mostrar_lista()

if __name__ == "__main__":
    executar_testes()
