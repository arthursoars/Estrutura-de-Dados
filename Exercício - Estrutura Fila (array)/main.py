from fila_circular import FilaCircular

def main():
    capacidade = 5
    fila = FilaCircular(capacidade)
    
    print("Fila criada com capacidade:", capacidade)
    
    # Inserir elementos
    print("Inserindo elementos:")
    for i in range(capacidade):
        fila.inserir(i)
        print(f"Inserido {i}: {fila}")

    # Testar fila cheia
    print("A fila está cheia?", fila.esta_cheia())
    
    # Consultar o início da fila
    print("Início da fila:", fila.consultar_inicio())
    
    # Remover elementos
    print("Removendo elementos:")
    for _ in range(capacidade):
        print(f"Removido {fila.remover()}: {fila}")

    # Testar fila vazia
    print("A fila está vazia?", fila.esta_vazia())
    
    # Tentar inserir quando a fila está vazia
    print("Inserindo mais elementos após remoção:")
    fila.inserir(10)
    print(f"Inserido 10: {fila}")

    fila.inserir(20)
    print(f"Inserido 20: {fila}")

if __name__ == "__main__":
    main()
