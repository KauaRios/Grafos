def bellman_ford(vertices, arestas, origem):
    distancias = {}
    for v in vertices:
        distancias[v] = float('inf')
    distancias[origem] = 0
    
    # Relaxamento de todas as arestas |V| - 1 vezes
    for i in range(len(vertices) - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                
    # Verificação de ciclos de peso negativo
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            print("\nO grafo possui ciclo negativo!")
            return None
            
    return distancias

vertices = []
arestas = []

qtd_vertices = int(input("Quantidade de vértices: "))
for i in range(qtd_vertices):
    vertice = input(f"Nome do Vértice {i+1}: ")
    vertices.append(vertice)

qtd_arestas = int(input("Quantidade de arestas: "))
for i in range(qtd_arestas):
    origem = input("Origem: ")
    destino = input("Destino: ")
    peso = int(input("Peso da aresta: "))
    arestas.append((origem, destino, peso))

vertice_inicial = input("Vértice inicial: ")
resultado = bellman_ford(vertices, arestas, vertice_inicial)

if resultado:
    print("\nMenores distâncias: ")
    for v in resultado:
        print(f"{vertice_inicial} -> {v} = {resultado[v]}")
