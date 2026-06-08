#Etapa 1 - Calculo do imc
def calc_imc(peso , altura):
    imc = peso/(altura * altura)
    return imc
#Etapa 2 - Classificação do imc
def class_imc(resultado):
    if resultado >= 25:
        return "ACIMA DO PESO!"
    else:
        return "PESO NORMAL"
#Etapa 3 - Mensagem de retorno
def mensagem(status):
    if status -- "ACIMA DO PESO":
        return "⚠️Atenção! procure um Médico"
    else:
        return "⚠️Seu peso está Normal, continue assim"
#Etapa 4 - Integração do código
valor_peso = float(input("Digite o seu peso: "))
valor_altura = float(input("Digite a sua altura: "))
valor_imc = calc_imc(valor_peso, valor_altura)
resultado_imc = class_imc(valor_imc)
saida = mensagem(resultado_imc)
print("=" * "50")
print("resultado do seu imc: ")
print(f"\n seu imc é: {valor_imc}")
print(f"\n {saida}")
print(f"=" * 50)