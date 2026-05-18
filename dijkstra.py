import heapq
#funçao dijkstra

def dijkstra(grafo,inicio):
    distancias={vertice:float('inf')for vertice in grafo}
    distancias[inicio]=0
    fila=[(0,inicio)]
    while fila:
        distancia_atual,vertice_atual=heapq.heappop(fila)
        for vizinho,peso in grafo[vertice_atual]:
            nova_distancia=distancia_atual+peso
            if nova_distancia< distancias[vizinho]:
                distancias[vizinho]=nova_distancia
                heapq.heappush(fila,(nova_distancia,vizinho))
    return distancias      


grafo={}
qtd_vertices=int(input("quantidade de vertices:"))
#criando vertices

for i in range(qtd_vertices):
    vertice=input(f"Nome do vertice{i+1}:")
    grafo[vertice]=[]


qtd_arestas=int(input("Quantidade de arestas: "))

for i in range(qtd_arestas):
    origem=input("Origem:")
    destino=input("Destino:")
    peso=int(input("Peso da Aresta:"))
    #grafo nao direcionado

    grafo[origem].append((destino,peso))
    grafo[destino].append((origem,peso))


    inicio=input("Vertice Inicial :")
    resultado=dijkstra(grafo,inicio)
    print("\nMenores Distancias: ")
    for vertice,distancia in resultado.items():
        print(f"{inicio}->{vertice}={distancia}")
