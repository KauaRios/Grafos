import heapq

def prim(grafo, inicio):
    visitados = set()
    fila_prioridade = []
    
    visitados.add(inicio)
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila_prioridade, (peso, inicio, vizinho))
        
    arvore_minima = []
    custo_total = 0.0
    
    while fila_prioridade:
        peso, origem, destino = heapq.heappop(fila_prioridade)
        
        if destino not in visitados:
            visitados.add(destino)
            arvore_minima.append((origem, destino, peso))
            custo_total += peso
            
            for vizinho, peso_aresta in grafo[destino]:
                if vizinho not in visitados:
                    heapq.heappush(fila_prioridade, (peso_aresta, destino, vizinho))
                    
    return arvore_minima, custo_total

print("=" * 60)
print("ALGORITMO DE PRIM - GRAFO NÃO DIRECIONADO")
print("=" * 60)

while True:
    try:
        num_vertices = int(input("Digite o número de vértices: "))
        if num_vertices <= 0:
            print("ERRO: O número de vértices deve ser maior que zero.\n")
        else:
            break
    except ValueError:
        print("ERRO: Digite apenas números inteiros.\n")

while True:
    try:
        num_arestas = int(input("Digite o número de arestas: "))
        if num_arestas <= 0:
            print("ERRO: O número de arestas deve ser maior que zero.\n")
        else:
            break
    except ValueError:
        print("ERRO: Digite apenas números inteiros.\n")

grafo = {}
for i in range(1, num_vertices + 1):
    grafo[i] = []

print("\nDigite as arestas no formato:")
print("origem destino peso")
print("Exemplo: 1 2 10\n")

i = 0
while i < num_arestas:
    print(f"\nAresta {i+1}")
    try:
        origem = int(input("Origem: "))
        destino = int(input("Destino: "))
        
        if origem not in grafo:
            print(f"Erro: O vértice {origem} não existe.")
            print(f"Os vértices válidos vão de 1 até {num_vertices}.\n")
            continue
            
        if destino not in grafo:
            print(f"Erro: O vértice {destino} não existe.")
            print(f"Os vértices válidos vão de 1 até {num_vertices}.\n")
            continue
            
        peso = float(input("Peso: "))
        grafo[origem].append((destino, peso))
        grafo[destino].append((origem, peso))
        i += 1  # Avança apenas quando a aresta for válida
        
    except ValueError:
        print("Erro: Entrada Inválida. Digite Números.\n")

vertice_inicial = 1
agm, custo_total = prim(grafo, vertice_inicial)

print("\n" + "=" * 60)
print("Árvore Geradora Mínima (PRIM)")
print("=" * 60)

for origem, destino, peso in agm:
    print(f"{origem} --- {destino} | Peso = {peso}")

print("-" * 60)
print(f"Custo total da AGM: {round(custo_total, 2)}")
