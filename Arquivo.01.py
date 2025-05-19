
with open("Nomes.txt","w") as arquivo:

    arquivo.write()

    def menu():
        print("___Lista___")
        print("1.Adicionar")
        print("2.Sair")
    def repetidor():
        add=[]
        while True:
            menu()
            escolha=input("digite sua escolha: ")
            if escolha == '1':
                tarefas=input("digite sua tarefa:")
                add.append(tarefas)
                print("tarefa adicionada.")
            elif escolha == '2':
                print("você esta saindo da lista")
                break
            else:
                print("opição invalida")
    repetidor()


