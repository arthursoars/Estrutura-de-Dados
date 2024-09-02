class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.vetor = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.size = 0

    def inserir(self, valor):
        if self.esta_cheia():
            raise Exception("Fila cheia")
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.size += 1

    def remover(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        valor = self.vetor[self.inicio]
        self.vetor[self.inicio] = None  # Opcional, para depuração
        self.inicio = (self.inicio + 1) % self.capacidade
        self.size -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.vetor[self.inicio]

    def esta_vazia(self):
        return self.size == 0

    def esta_cheia(self):
        return self.size == self.capacidade

    def __str__(self):
        elementos = []
        i = self.inicio
        for _ in range(self.size):
            elementos.append(self.vetor[i])
            i = (i + 1) % self.capacidade
        return ' -> '.join(map(str, elementos)) if elementos else "Fila vazia"
