# pocentagem
#primeiros passos pra conseguir fazer uma porcentagem .
# com muita pesquisas

SP = 6783643   # não usei flout pois assim a conta fica mais facil
RJ = 667866
MG = 2922988
ES = 2716548
Out = 1984953
Faturamento = SP + RJ + MG + ES + Out

PSP = SP/Faturamento # pra acha o percentual 
PRJ = RJ/Faturamento
PMG = MG/Faturamento
PES = ES/Faturamento
POUT = Out/Faturamento

print(f'O porcentual de SP {PSP:.0%}')
print(f'O porcentual de RJ {PRJ:.0%}')
print(f'O porcentual de MG {PMG:.0%}')
print(f'O porcentual de ES {PES:.0%}')
print(f'O porcentual de Out {POUT:.0%}')

texto_Faturamento = f'R${Faturamento:_.2f}'
texto_Faturamento = texto_Faturamento.replace(".",",").replace("_",".")
print("Valor total Mensal foi de R$ ",(texto_Faturamento))
print ()
