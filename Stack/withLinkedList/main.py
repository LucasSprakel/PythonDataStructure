from stack import Stack
    
    
while True:
    print('Pilha baseada em Lista Encadeada by Lucas Sprakel')
    print('1- Criar uma pilha')
    print('2- Verificar se pilha está vazia')
    print('3- Inserir(Push) novo elemento no topo da pilha')
    print('4- Remover(Pop) um elemento do topo da pilha')
    print('5- Mostrar topo da pilha')
    print('6- Tamanho da pilha')
    print('7- Sair')

    action = int(input('Digite uma ação: '))
    if action == 1:
        new_stack = Stack()
        print('\n\nPILHA CRIADA COM SUCESSO \n\n')
    try:
        if action == 2:
            if new_stack.stack_is_empty():
                print('\n\nA pilha está vazia\n\n')
            else:
                print('\n\nA pilha não está vazia\n\n')
        if action == 3:
            valor = int(input('Diga o valor do elemento que deseja empilhar: '))
            new_stack.push(valor)
            print('\n\nNovo elemento empilhado\n\n')
        if action == 4:
            v_p = new_stack.pop()
            print(f'\n\nElemento {v_p} foi desempilhado \n\n')
        if action == 5:
            print('\n\n' + str(new_stack.top.value) + '\n\n')
        if action == 6:
            print('\n\n' + 'A pilha possui ' + str(new_stack.size) + ' elementos\n\n')
        if action == 7:
            break
    except NameError:
        print("\n\nCrie a pilha antes\n\n")