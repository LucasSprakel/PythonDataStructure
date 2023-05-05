from GraphList import Graph as GraphList
from GraphMatrix import Graph as GraphMatrix

print('Digite 1 para Matriz de Adjacência ou Digite 2 para Lista de Adjacência')
option = int(input())

if option == 1:
    while True:
        
        print('Grafo(Matriz Adjacência) by Lucas Sprakel')
        print('1- Criar um Grafo')
        print('2- Adicionar aresta')
        print('3- Mostrar matriz')
        print('4- Busca em Largura (BFS)')
        print('5- Busca em Profundidade (DFS)')
        print('6- Sair')
        
        action = int(input('Digite uma ação: '))
        
        if action == 1:
            tamanho = int(input('Qual o tamanho do Grafo(Quantos vértices)? '))
            new_graph = GraphMatrix(tamanho)
            print('\n\nGRAFO CRIADO COM SUCESSO\n\n')
        
        elif action == 2:
            v1 = int(input('Digite o primeiro vértice: '))
            v2 = int(input('Digite o segundo vértice: '))
            new_graph.add_edge(v1, v2)
            print(f'\n\nAresta entre {v1} e {v2} criada\n\n')
        
        elif action == 3:
            new_graph.show_matrix()
        
        elif action == 4:
            v1 = int(input('Digite o vértice inicial: '))
            v2 = int(input('Digite o vértice que deseja comparar: '))
            print(new_graph.bfs(v1, v2))
            print('\n\n')
        
        elif action == 5:   
            v1 = int(input('Digite o vértice inicial: '))
            print(new_graph.dfs(v1))
            print('\n\n')
        
        elif action == 6: 
            break
        
        else:
            pass

elif option == 2:
    while True:
        
        print('Grafo(Lista Adjacência) by Lucas Sprakel')
        print('1- Criar um Grafo')
        print('2- Adicionar aresta')
        print('3- Mostrar lista')
        print('4- Busca em Largura (BFS)')
        print('5- Busca em Profundidade (DFS)')
        print('6- Sair')
        
        action = int(input('Digite uma ação: '))
        
        if action == 1:
            tamanho = int(input('Qual o tamanho do Grafo(Quantos vértices)? '))
            new_graph = GraphList(tamanho)
            print('\n\nGRAFO CRIADO COM SUCESSO\n\n')
        
        elif action == 2:
            v1 = int(input('Digite o primeiro vértice'))
            v2 = int(input('Digite o segundo vértice'))
            new_graph.add_edge(v1, v2)
            print(f'Aresta entre {v1} e {v2} criada')
        
        elif action == 3:
            new_graph.show_matrix()
        
        elif action == 4:
            v1 = int(input('Digite o vértice inicial: '))
            v2 = int(input('Digite o vértice que deseja comparar: '))
            print(new_graph.bfs(v1, v2))
            print('\n\n')
        
        elif action == 5:   
            v1 = int(input('Digite o vértice inicial: '))
            print(new_graph.dfs(v1))
            print('\n\n')
        
        elif action == 6: 
            break
        
        else:
            pass
            
else: 
  pass
