import math# arredondar vaolores


def decimal_para_binario(decimal): # input para função
    convertido = ''
    while decimal != 1:# enquanto for diferente de 1
        convertido += str(decimal %2) # divide o valor e adiciona o resto da divisão na linha  5
        decimal = math.floor(decimal / 2)# divide o valor para a proxima divisão do loop (atualiza o valor decimal)
    else:
        convertido += "1"#  adicionanco o 1 do final da conversão
    return convertido[::-1]# invertendo a ordem 

def decimal_para_octal(decimal): # input para função
    convertido = ''
    while decimal > 8:# enquanto for maior que 8
        convertido += str(decimal %8) # divide o valor e adiciona o resto da divisão na linha  14
        decimal = math.floor(decimal / 8)# divide o valor para a proxima divisão do loop (atualiza o valor decimal)
    else:    
        convertido += str(decimal) #adiciona o decimal menor que 8
    return convertido[::-1]# invertendo a ordem 


def decimal_para_hexadecimal(decimal): # input para função
    convertido = ''
    hex_codes = { 
        0: "0", 
        1: "1",
        2: "2", 
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "c",
        13: "D",
        14: "E",
        15: "F"
    }

    while decimal > 16:# enquanto for maior que 16
        convertido += hex_codes[decimal %16] # pega o resto da divisão e traduz com o dicionario e armazena na linha 23
        decimal = math.floor(decimal / 16)# divide o valor para a proxima divisão do loop (atualiza o valor decimal)
    else: 
        convertido += hex_codes[decimal]# ira pegar o numero menor que 16 e vai traduzir no dicionario e adicionar no convertido 
    return convertido[::-1]# invertendo a ordem 


nDecimal = int(input('Digite um Nº decimal: ')) # input para o usuario informar o decimal para conversão 




binario = decimal_para_binario(nDecimal) # definindo o nome pelo qual será chamado a função 

octal = decimal_para_octal(nDecimal) # definindo o nome pelo qual será chamado a função 

hexadecimal = decimal_para_hexadecimal(nDecimal) # definindo o nome pelo qual será chamado a função 

opção = 0
while opção != 4:
    print('''    [1] converter para binario
    [2] converter para octal
    [3] converter para hexadecimal 
    [4] sair do programa''')
    opção = int(input("Qual é a sua opção? "))
    if opção == 1 :
        print ("o valor convertido para binario é ", binario) # exibindo o resultado para o usuario
    elif opção == 2 :
        print ("o valor convertido para octal é ", octal) # exibindo o resultado para o usuario
    elif opção == 3 :
        print ("o valor convertido para hexadecimal é ", hexadecimal) # exibindo o resultado para o usuario 
    elif opção == 4 :
        print ("Finalizando...")
    else:
        print("opção inválida, tente novamente")