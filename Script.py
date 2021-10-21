print('Bem vindo(a) ao "Devo pagar IRPF?"')
print('Para saber se você deve ou não declarar imposto de renda responda algumas perguntas.')
print('OBSERVAÇÕES: Caso não tenha recebido algum valor questionado digite 0')
condição1 = float(input('Qual o valor obtido com venda de veículos ou imóveis? '))
if condição1 > 0:
	print('Você deve declarar o IRPF, você também precisará preencher o programa que calcula ganho de capital (GCAP)!')
	exit('Você obteve uma condição obrigatória para a declaração do IRPF, o programa irá encerrar')
condição2 = float(input('Qual o valor obtido por meio de ação trabalhista? '))
if condição2 > 40000:
	print('Você deve declarar o IRPF!')
	exit('Você obteve uma condição obrigatória para a declaração do IRPF, o programa irá encerrar') 
salário= float(input('Qual o valor recebido de salário? '))
aposentadoria = float(input('Qual o valor recebido de aposentadoria? '))
inss = float(input('Qual o valor da sua pensão recebida pelo INSS? '))
pensão_alimentícia =  float(input('Qual o valor recebido de pensão alimentícia? '))
renda_alugel = float(input('Qual o valor recebido com alugueis? '))
rendimento_autônomo = float(input('Qual o valor recebido como autônomo? '))
auxílio = float(input('Qual o valor recebido pelo FGTS? '))
valor_total = (salário + aposentadoria + inss + pensão_alimentícia + renda_alugel + rendimento_autônomo)
if auxílio > 0 and((valor_total + auxílio) * 12) > 22847.76:
        print('Você deve declarar o IRPF!')

if auxílio <= 0 and(valor_total* 12) > 28559.70:
        print('Você precisa declarar o IRPF!')
	
elif auxílio <= 0 and(valor_total* 12) < 28559.70:
        print('Você não precisa declarar o IRPF')
