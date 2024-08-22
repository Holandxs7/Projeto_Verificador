'''
1 - Entrar na planilha e extrair o cpf do cliente.
2 - Entro no Site https://consultcpf-.... e uso o cpf da planilha para pesquisar o status do pagamento daquele cliente.
3 - Verificar se está "em dia" ou "atrasado".
4 - Se estiver "em dia", pegar a data do pagamento e o método de pagamento.
5 - Caso contrário(se estiver atrasado), colocar o status como pendente.
6 - Iserir essas novas informações(nome, valor, cpf, vencimento e status. E caso esteja em dia mostrar data pagamento e método pagamento(cartão ou boleto)) em uma nova planilha.
7 - Repetir até chegar no último cliente.
'''
import openpyxl

#1 - Entrar na planilha e extrair o cpf do cliente.
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2,values_only=true):
    nome, valor, cpf, vencimento = linha
    print(nome)
    print(valor)
    print(cpf)
    print(vencimento)
