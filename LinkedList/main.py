from linkedlist import LinkedList


while True:
    print('Lista Encadeada by Lucas Sprakel')
    print('1- Criar uma lista')
    print('2- Verificar se lista está vazia')
    print('3- Obter tamanho da lista')
    print('4- Inserir um novo elemento na lista')
    print('5- Obter elemento da lista')
    print('6- Modificar elemento da lista')
    print('7- Retirar um elemento da lista')
    print('8- Mostrar lista completa')
    print('9- Sair')

    action = int(input('Digite uma ação: '))
    if action == 1:
        new_list = LinkedList()
        print('\n\nLISTA CRIADA COM SUCESSO \n\n')
    if action == 2:
        if new_list.list_is_empty():
            print('\n\nA lista está vazia\n\n')
        else:
            print('\n\nA lista não está vazia\n\n')
    if action == 3:
        print('\n\n' + 'A lista possui ' + str(new_list.size) + ' elementos\n\n')
    if action == 4:
        index = int(input('Começando a lista na posição 1, diga em que posição(índice) deseja inserir o elemento: '))
        valor = int(input('Diga o valor do elemento que deseja inserir: '))
        new_list.insert(valor, index)
        print('\n\nNovo elemento adicionado\n\n')
    if action == 5:
        index = int(input('Diga qual o indice do elemento que deseja buscar: '))
        print('\n\n')
        new_list.show_element(index)
        print('\n\n')
    if action == 6:
        index = int(input('Diga qual o indice do elemento que deseja modificar: '))
        value = int(input('Diga qual o novo valor do emento: '))
        new_list.edit_element(index, value)
        print(f'\n\nO elemento de indice = {index} foi modificado para {value}\n\n')
    if action == 7:
        index = int(input('Diga qual o indice do elemento que deseja remover: '))
        new_list.remove(index)
        print(f'\n\nO elemento de indice = {index} foi removido \n\n')
    if action == 8:
        print('\n\nLISTA COMPLETA: \n')
        new_list.show_list()
    if action == 9:
        break