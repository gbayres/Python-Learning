print("Insira os valores. Se não houver, apenas dê ENTER")

var = {
    ' q ' : int(input("q - Quantidade de vendas por unidade para o PEO\n")),
    ' p ' : float(input("p - Preço de venda unitário\n")),
    ' CVu ' : float(input("CVu - Custo operacional variável por unidade\n")),
    ' CF ' : float(input("CF - Custo operacional fixo no período\n")),
    ' MC ' : float(input("MC - Margem de contribuição (p - CVu)\n")),
    ' RVatual ' : float(input("RV(atual)\n")),
    ' RVpeo ' : float(input("RV(PEO)\n")),
    ' lcmin ' : float(input("Lucro mínimo\n")),
}

if var[' CVu '] != '' and var[' p '] != '':
    var[' MC '] = var[' p '] - var[' CVu ']

formulas = {' q = CF / MC ' : "Ponto de equilíbrio contábil",
            ' RVpeo = CF * RVatual / MC ' : "Receita de vendas no ponto de equilíbrio",
            ' q = ( CF + lcmin ) / MC ' : "Ponto de equilíbrio econômico",
            ' q = RVpeo / p ': "Unidades produzidas no PEO",
            }
            
