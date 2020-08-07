
# ======================================================================
# FUNÇÕES Principais
# ======================================================================

def polinomioComRaiz(p, b) :
    """Devolve True se b é raiz do polinômio representado pela lista p,
       ou False no caso contrário.

       p -- a lista dos coeficientes do polinômio
       b -- o número a ser testado como raiz
    """

    # Escreva aqui o corpo da função
    a = len(p)
    valor = 0
    for i in range (a):
        valor += p[i]*(b**i)
        a += 1

    teste = ""
    if valor == 0:
        teste = True
    else:
        teste = False
    return teste  # Ajuste o valor de retorno


# ======================================================================

def polinomioQuociente(p, b) :
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(x-b), onde p(x) é o polinômio cujos coeficientes estão na
       lista p e b é uma raiz de p(x).

       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- a raiz a ser usada como divisor
    """

    # Escreva aqui o corpo da função

    copia = p[:]
    a = len(p)

    copia.reverse()
    v = []
    v.append(copia[0])
    i=1
    while i <= a-2:
        v.append(v[i-1]*b + copia[i])
        i += 1

    v.reverse()
    return v  # Ajuste o valor de retorno

# ======================================================================
def listaCanonicaDeRaizes(p) :
    """Devolve a lista canônica de raízes inteiras do polinômio
       representado pela lista p.

       p -- a lista dos coeficientes do polinômios
    """

    # Escreva aqui o corpo da função

    div1 = []
    raiz = []
    recebido = False
    while recebido == False :
        if p[0] == 0 :
            raiz.append(p[0])
            del p[0]
        else :
            if p[0] > 0 :
                indep = p[0]
            else :
                indep = -p[0]
            recebido = True

    i = 1
    tamanho = len(p)

    #pega divisores do independente
    while i <= indep :
        if p[0] % i == 0 :
            div1.append(int(p[0] / i))
            div1.append(int(-(p[0] / i)))
        i += 1


    totaldiv = len(div1)
    u = valor = 0
    div1.reverse()
    while u < totaldiv :
        valor = polinomioComRaiz(p, div1[u])
        if valor :
            p = polinomioQuociente(p, div1[u])
            raiz.append(div1[u])
        else:
            u += 1

    return raiz  # Ajuste o valor de retorno


# ======================================================================
def polinomioQuocienteRacional(p, b, a) :
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(ax-b) e o resto dessa divisão, onde p(x) é o polinômio
       cujos coeficientes estão na lista p e b/a é uma raiz de p(x).

       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- numerador da raiz a ser usada como divisor
       a -- denominador da raiz a ser usada como divisor
    """
    # Escreva aqui o corpo da função
    r = 0
    tam = len(p)
    x = []
    q = []
    if tam > 1:
        v = []
        copia = p[:]
        copia.reverse()
        v.append(copia[0])
        i = 1
        while i <= tam - 2 :
            v.append(v[i - 1] * b/a + copia[i])
            i += 1

        v.reverse()

        r = p[0] - v[0]*(-b/a)

        l = 0
        while l < len(p) - 1:
            q.append(v[l]/a)
            l += 1


    else:
        q = None
        r = -1

    return q, r # Ajuste o valor de retorno


# ======================================================================
def listaRaizesRacionais(p) :
    # Escreva aqui o corpo da função
    div1 = []
    raiz = []
    a = b = 1
    tam = len(p)
    dominante = p[tam - 1]
    div2 = []

    # verifica se o primeiro termo e zero e elimina
    while p[0] == 0 :
        raiz.append(0)
        p = polinomioQuociente(p, 0)

    indep = p[0]

    # calcula os divisores do termo independente
    if indep < 0 :
        indep = -indep
    while b <= indep :
        if p[0] % b == 0 :
            div1.append(-(b))
            div1.append(b)
        b += 1

    # calcula os divisores do termo dominante
    if dominante < 0 :
        dominante = -dominante
    while a <= dominante :
        if dominante % a == 0 :
            div2.append(a)
        a += 1

    # numero de vetores dos divisores do termo independente
    totaldiv1 = len(div1)

    # numero de vetores dos divisores do termo dominante
    totaldiv2 = len(div2)

    c = 0

    # calcula as raizes racionais do polinomio

    while c < totaldiv2 :
        u = 0
        while u < totaldiv1 :
            q, r = polinomioQuocienteRacional(p, div1[u], div2[c])
            if r == 0 :
                raiz.append(div1[u] / div2[c])
                p = q
            else :
                u += 1
        c += 1
    print(raiz)
    return raiz

# ======================================================================
def racionalToString(pn, r) :
    """Devolve uma string que apresenta a raiz r do polinômio do qual pn
       é o coeficiente de maior grau como:
        - um inteiro, caso r seja inteiro
        - na forma b/a, com b e a primos entre si e a > 0, caso contrário

       pn -- coeficiente de maior grau do polinômio
       r -- uma raiz do polinômio
    """

    # Escreva aqui o corpo da função
    neg =False
    v1 = pn*r
    if r == round(r):
        res = "%d" %(r)
    else:
        if v1 < 0 :
            v1 = -v1
            neg = True

        mdc = v1

        #Calcula o MDC
        while v1 % mdc != 0 or pn % mdc != 0 :
            mdc = mdc - 1

        num = v1/mdc
        den = pn/mdc
        if neg:
            num = -num
        res = "%d/%d" %(num,den)

    return res  # Ajuste o valor de retorno


# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# FUNÇÕES ADICIONAIS
# ======================================================================
def polinomioToString(p) :
    """Devolve uma string que representa o polinômio em um formato
       legível para humanos.

       p -- a lista dos coeficientes do polinômio
    """
    n = len(p) - 1
    s = ""
    for m in range(n - 1) :
        if p[n - m] != 0 :
            s = "%s%s%dx^%d " % (s, sig(m, p[n - m]), p[n - m], n - m)
    if p[1] != 0 :
        s = "%s%s%dx " % (s, sig(n - 1, p[1]), p[1])
    if p[0] != 0 :
        s = "%s%s%d" % (s, sig(n, p[0]), p[0])
    return s


# ======================================================================
def sig(nTermAnte, coef) :
    """Devolve '+' se coef não é negativo e existe termo anterior ao
       termo dele no polinômio. Devolve '' (string vazia) no caso
       contrário. Usado para determinar se o '+' deve aparecer antes
       de coef na string que representa o polinômio.

       nTermAnte -- expoente de x no termo anterior ao termo do coef
       coef -- coeficiente de um termo do polinômio
    """
    if nTermAnte > 0 and coef >= 0 :
        return "+"
    else :
        return ""


# ======================================================================
# FIM DO BLOCO DE FUNÇÕES ADICIONAIS
# ======================================================================


# ======================================================================
# FUNÇÃO MAIN
# Escreva dentro da função main() o código que quiser para testar suas
# demais funções.
# Somente dentro da função main() você pode usar as funções print e
# input.
# O código da função main() NÃO será avaliado.
# ======================================================================
def main() :
    listaRaizesRacionais([1, -34, 404, -1934, 3003])


    n = int(input("Digite o grau: "))

    # Lê os coeficientes do polinômio
    p = []
    for i in range(n + 1) :
        p.append(float(input("Digite p[" + str(i) + "]: ")))
        i += 1

    # Obtém a lista de raízes
    if p[n] == 1 :
        raizes = listaCanonicaDeRaizes(p)
        print('A lista canonica das raizes inteiras de p(x) =',
              polinomioToString(p), 'eh:')
    else :
        raizes = listaRaizesRacionais(p)
        print('A lista canonica das raizes racionais de p(x) =',
              polinomioToString(p), 'eh:')

    # Imprime a lista canônica de raízes
    for raiz in raizes :
        s = racionalToString(p[n], raiz)
        print(s, end=" ")


    print()


# ======================================================================
# FIM DA FUNÇÃO MAIN
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__" :
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN
# ======================================================================