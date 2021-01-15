##print("Insira os valores. Se não houver, apenas dê ENTER")
##
##var = {
##    ' q ' : int(input("q - Quantidade de vendas por unidade para o PEO\n")),
##    ' p ' : float(input("p - Preço de venda unitário\n")),
##    ' CVu ' : float(input("CVu - Custo operacional variável por unidade\n")),
##    ' CF ' : float(input("CF - Custo operacional fixo no período\n")),
##    ' MC ' : float(input("MC - Margem de contribuição (p - CVu)\n")),
##    ' RVatual ' : float(input("RV(atual)\n")),
##    ' RVpeo ' : float(input("RV(PEO)\n")),
##    ' lcmin ' : float(input("Lucro mínimo\n")),
##}
##
##if var[' CVu '] != '' and var[' p '] != '':
##    var[' MC '] = var[' p '] - var[' CVu ']
##
##formulas = {' q = CF / MC ' : "Ponto de equilíbrio contábil",
##            ' RVpeo = CF * RVatual / MC ' : "Receita de vendas no ponto de equilíbrio",
##            ' q = ( CF + lcmin ) / MC ' : "Ponto de equilíbrio econômico",
##            ' q = RVpeo / p ': "Unidades produzidas no PEO",
##            }
##            
##

def q(CF, p, CVu, lmin=0):
    return  round((CF + lmin) / ( p - CVu ), 2)

def q2(RV, p):
    return round(RV / p, 2)

def RV(p, q):
    return round(p * q, 2)

def CVu(n, custo_prod_vendidos=0, desp_variaveis=0):
    return round((custo_prod_vendidos + desp_variaveis) / n, 2)    

def p (RV, n):
    return round(RV / n, 2)

##def PE(CF, p, CVu, lmin = 0):
##    
##    q = _q(CF, p, CVu)
##    RV = _RV(p, q)
##
##    print(f'''PEC em quantidade: q = CF/(p - CVu) = {CF}/({p} - {CVu}) = {q} unidades
##PEC em valores monetários: RV = p * q = R${RV}''')
##
##    if lmin != 0:
##        q = _q(CF, p, CVu, lmin)
##        RV = _RV(p, q)
##
##        print(f'''PEE em quantidade: q = (CF + lucro mínimo)/(p - CVu) = {q} unidades
##PEE em valores monetários: RV = p * q = R${RV}''')    
##
##def PE2(RV, n, custo_prod_vendidos, desp_variaveis, CF, lmin=0):
##    p = _p(RV, n)
##    CVu = _CVu(n, custo_prod_vendidos, desp_variaveis)
##
##    print(f'p = RV / q = {RV} / {n} = {p}')
##    print(f'CVu = custos dos produtos vendidos + despesas variaveis / q = {CVu}')
##
##    PE(CF, p, CVu, lmin)

