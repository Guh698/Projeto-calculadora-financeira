# Juros e Descontos da administração


import tkinter as tk
import math


def calcular():
    Formula_a_ser_seguida = int(entry_formula.get())

    if Formula_a_ser_seguida == 1:
        x = int(entry_incongnita.get())
        if x == 1:
            # Lógica para calcular Juros Simples com incógnita Capital
            pass  # Aqui você implementará a lógica de cálculo

# Função para mostrar o resultado no campo de texto


def mostrar_resultado(resultado):
    output_resultado.delete(1.0, tk.END)  # Limpa o campo de texto
    # Insere o resultado no campo de texto
    output_resultado.insert(tk.END, resultado)


# Cria a janela principal
root = tk.Tk()
root.title("Cálculos Financeiros")

# Cria os widgets
label_formula = tk.Label(root, text="Insira o número da fórmula a ser usada:")
entry_formula = tk.Entry(root)
label_incongnita = tk.Label(
    root, text="Insira o número da incógnita especial:")
entry_incongnita = tk.Entry(root)
button_calcular = tk.Button(root, text="Calcular", command=calcular)
output_resultado = tk.Text(root, height=10, width=50)

# Posiciona os widgets na janela
label_formula.pack()
entry_formula.pack()
label_incongnita.pack()
entry_incongnita.pack()
button_calcular.pack()
output_resultado.pack()

# Inicia o loop principal da interface
root.mainloop()


print(
    "\nObserve as fórmulas para ajudar em sua escolha:"
    "\n1 - Juros simples                :  J = C.i.t"
    "\n2 - Juros simples (montante)     :  M = C.(1+ i.t)"
    "\n3 - Juros compostos              :  M = C * (1 + i)^t"
    "\n4 - Desconto simples (comercial) :  A = N*(1 - i*n)"
    "\n4 - Desconto simples (racional)  :  A = N / (1 + i*n)"
    "\n5 - Desconto composto (comercial):  A = N*(1 - i)^n"
    "\n5 - Desconto composto (racional) :  A = N / (1 + i)^n")

print(
    "\nEm juros:"
    "\n1 - C = capital"
    "\n2 - i = taxa"
    "\n3 - T = tempo"
    "\nM = montante"
    "\nJ = juros")

print(
    "\nEm Descontos:"
    "\nA = atual"
    "\ni = taxa"
    "\nn = tempo"
    "\nD = desconto"
    "\nN = nominal")

Formula_a_ser_seguida = int(input("\nInsira o número da fórmula a ser usada:"))

# Descobrir juros simples
if Formula_a_ser_seguida == 1:
    x = int(input(
        "Se ouver alguma incógnita especial, insira o número (consulte na tabela):"))
    if x == 1:
        J = float(input("Insira seu juros:"))
        I = float(input("Insira sua taxa ao mês:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            C = round(J / (i*Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            C = round(J / (i*Tm), 4)
        print(f"O capital é: {C}")
    elif x == 2:
        J = float(input("Insira seu juros:"))
        C = float(input("Insira seu capital:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            i = round(J / (C*Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            i = round(J / (C*Tm), 4)
        ia = i*100
        print(f"A taxa ao mês é: {ia}%")
    elif x == 3:
        J = float(input("Insira seu juros:"))
        C = float(input("Insira seu capital:"))
        I = float(input("Insira sua taxa ao mês:"))
        i = round(I / 100, 4)
        T = round(J / (C*i), 4)
        if T % 1 == 0:
            print(f"Seu tempo em mês é: {T}")
        else:
            td = T*30
            print(f"Seu tempo em dias é: {td}")
    else:
        C = float(input("Insira seu capital:"))
        I = float(input("Insira sua taxa ao mês:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            J = round((C*i*Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            J = round((C*i*Tm), 4)
        print(f"Juros igual a: {J}")
elif Formula_a_ser_seguida == 2:
    x = int(input(
        "Se ouver alguma incógnita especial, insira o número (consulte na tabela):"))
    if x == 1:
        M = float(input("Insira seu montante obtido:"))
        I = float(input("Insira sua taxa:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            C = round(M / (1 + i * Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            C = round(M / (1 + i * Tm), 4)
        print(f"Seu capital é de: {C}")
    elif x == 2:
        C = float(input("Insira o capital:"))
        M = float(input("Insira o montante obtido:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            I = round((M - C) / (C*Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            I = round((M - C) / (C*Tm), 4)
        i = I*100
        print(f"A sua taxa mensal é de: {i}%")
    elif x == 3:
        M = float(input("Insira o montante obtido:"))
        C = float(input("Insira o capital:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        T = round((M - C) / (C * i), 4)
        print(f"O seu tempo é: {T}")
    else:
        C = float(input("Insira o capital:"))
        I = float(input("Insira a taxa mensal:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            M = round(C * (1+i * Td), 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            M = round(C * (1+i * Tm), 4)
        print(f"O seu montante é: {M}")
elif Formula_a_ser_seguida == 3:
    x = int(input(
        "Se ouver alguma incógnita especial, insira o número (consulte na tabela):"))
    if x == 1:
        M = float(input("Insira o montante:"))
        I = float(input("Insira a taxa:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            C = round(M / (1 + i) ** Td, 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            C = round(M / (1 + i) ** Tm, 4)
        print(f"O seu capital é de:{C}")
    elif x == 2:
        M = float(input("Insira o montante:"))
        C = float(input("Insira o capital:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            i = round(((M / C) ** (1 / Td)) - 1, 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            i = round(((M / C) ** (1 / Tm)) - 1, 4)
        I = i*100
        print(f"A taxa é: {I}%")
    elif x == 3:
        import math
        M = float(input("Insira o montante:"))
        C = float(input("Insira o capital:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        T = round(math.log(M / C) / math.log(1 + i), 4)
        print(f"O seu tempo é: {T} meses")
    else:
        C = float(input("Insira o capital:"))
        I = float(input("Insira a taxa mensal:"))
        T = str(input(
            "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
        i = round(I / 100, 4)
        if T == "dias":
            Td = float(input("Insira seu tempo em dias:"))
            while Td >= 30:
                Td = round(Td / 30, 4)
            M = round(C * (1 + i) ** Td, 4)
        elif T == "meses":
            Tm = float(input("Insira seu tempo em meses:"))
            M = round(C * (1 + i) ** Tm, 4)
        print(f"O seu montante é de: {M}")
elif Formula_a_ser_seguida == 4:
    Td = str(input("\nInsira o tipo de desconto (Racional) ou (Comercial):"))
    n = str(input(
        "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
    if n == "dias":
        Tempo = float(input("Insira seu tempo em dias:"))
        while Tempo >= 30:
            Tempo = round(Tempo / 30, 4)
    elif n == "meses":
        Tempo = float(input("Insira seu tempo em meses:"))
    if Td == "Comercial" and n == "dias":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N*(1 - i*Tempo), 4)
        D = (N - A)
        print(f"O seu valor atual é: R${A} e seu desconto é de R${D}")
    elif Td == "Racional" and n == "dias":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N / (1 + i*Tempo), 4)
        D = (N - A)
        print(f"O seu valor atual é: R${A} e seu desconto é de R${D}")
    elif Td == "Comercial" and n == "meses":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N*(1 - i*Tempo), 4)
        D = (N - A)
        print(f"O seu valor atual é: R${A} e seu desconto é de R${D}")
    elif Td == "Racional" and n == "meses":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N / (1 + i*Tempo), 4)
        D = (N - A)
        print(f"O seu valor atual é: R${A} e seu desconto é de R${D}")
elif Formula_a_ser_seguida == 5:
    Td = str(input("\nInsira o tipo de desconto (Racional) ou (Comercial):"))
    n = str(input(
        "Se o tempo for em dias escreva -dias-, mas se o tempo for em mês, escreva -meses-:"))
    if n == "dias":
        Tempo = float(input("Insira seu tempo em dias:"))
        while Tempo >= 30:
            Tempo = round(Tempo / 30, 4)
    elif n == "meses":
        Tempo = float(input("Insira seu tempo em meses:"))
    if Td == "Comercial":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N*(1 - i)**Tempo, 4)
        D = (N - A)
    elif Td == "Racional":
        N = float(input("Insira o valor nominal:"))
        I = float(input("Insira a taxa:"))
        i = round(I / 100, 4)
        A = round(N / (1 + i)**Tempo, 4)
        D = (N - A)
    print(f"O seu valor atual é: R${A} e seu desconto é de R${D}")
