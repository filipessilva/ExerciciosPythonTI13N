import this
import ExerciciosModel
this.opcao = -1

def Menu():
    print('\n\n Menu \n\n'+
          '\n01. Exercicio 01' +
          '\n02. Exercicio 02' +
          '\n03. Exercicio 03' +
          '\n04. Exercicio 04' +
          '\n05. Exercicio 05' +
          '\n06. Exercicio 06' +
          '\n07. Exercicio 07' +
          '\n08. Exercicio 08' +
          '\n09. Exercicio 09' +
          '\n10. Exercicio 10' +
          '\n11. Exercicio 11' +
          '\n12. Exercicio 12' +
          '\n13. Exercicio 13' +
          '\n14. Exercicio 14' +
          '\n15. Exercicio 15' +
          '\n16. Exercicio 16' +
          '\n17. Exercicio 17' +
          '\n18. Exercicio 18' +
          '\n19. Exercicio 19' +
          '\n20. Exercicio 20' +
          '\n00. Sair'+
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()

        if this.opcao == 0:
            print ("Obrigado!")
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            print(ExerciciosModel.exercicio02())
        elif this.opcao == 3:
            print(ExerciciosModel.exercicio03())
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio04())
        elif this.opcao == 5:
            print (ExerciciosModel.exercicio05())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio09())
        elif this.opcao == 10:
            print()
        elif this.opcao == 11:
            print()
        elif this.opcao == 12:
            print()
        elif this.opcao == 13:
            print()
        elif this.opcao == 14:
            print ()
        elif this.opcao == 15:
            print()
        elif this.opcao == 16:
            print()
        elif this.opcao == 17:
            print()
        elif this.opcao == 18:
            print()
        elif this.opcao == 19:
            print()
        elif this.opcao == 20:
            print()
        else:
            print ('Opção informada não é valida!')