#aluno1: formato do nome do filme
def formatar(nome):
    return nome.upper()
#aluno2: verificação de acesso
def  verificador(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não Autorizado"
#Aluno3: Mensagem de Retorno
def gerar_mensagem(status):
    if status == "Autorizado":
        return "Tenha uma ótima sessão"
    else:
        return "Sinto muito, idade não autorizada"
#Aluno4: Integrador do projeto
nome_filme = input("Digite o nome do filme: ")
idade_filme = int(input("Digite sua idade: "))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\n Filme:{filme}")
print(f"status:{status_final}")
print(f"Aviso:{mensagem}")