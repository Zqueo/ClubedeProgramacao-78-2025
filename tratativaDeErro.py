try:
    result = 1 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
finally:
    print("Finalizando o programa.")
    input("Pressione enter para sair...")