# Multiplica 2 mintérminos
def mul(x,y): 
    res = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res

# Multiplica 2 expresiones
def multiplica(x,y): 
    res = []
    for i in x:
        for j in y:
            implprimos = multiplica(i,j)
            res.append(implprimos) if len(implprimos) != 0 else None
    return res

# crea la lista reacomodada
def reacomoda(my_list): 
    res = []
    for i in my_list:
        res.append(i)
    return res

# Encuentra implicantes primos esenciales
def BuscarIPE(x): 
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res

 # Encontrar variables
def BuscarVariables(x):
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+65)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+65))
    return var_list

# Recorta la lista
def recorta(x):
    elem_recortados = []
    for i in x:
        elem_recortados.extend(x[i])
    return elem_recortados

# Encontrar mintérminos repetidos
def buscaMinterminos(a): 
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

# Comparar un bit
def compara(a,b): 
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True,mismatch_index)


# Remueve mintérminos repetidos
def remueveTerminos(_chart,terms): 
    for i in terms:
        for j in buscaMinterminos(i):
            try:
                del _chart[j]
            except KeyError:
                pass
print('Por favor ingrese los términos separados por un espacio')
mint = [int(i) for i in input("Ingrese los mintérminos ").strip().split()]
mint.sort()
minterminos = mint
minterminos.sort()
size = len(bin(minterminos[-1]))-2
grupos,all_pi = {},set()

# Comenzamos la primera agrupación
for minterm in minterminos:
    try:
        grupos[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
    except KeyError:
        grupos[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]


#Imprime la primera agrupación
def mostrar(self):
    print("\n\n\n\nNúmero de Gpo.\tMintérminos\t\tExpresión en BCD\n%s"%('='*60))
for i in sorted(grupos.keys()):
    print("%5d:"%i) 
    for j in grupos[i]:
        print("\t\t    %-20d%s"%(int(j,2),j))
    print('-'*60)
    print("\n\n\n\nNúmero de Gpo.\tMintérminos\t\tExpresión en BCD\n%s"%('='*60))
for i in sorted(grupos.keys()):
    print("%5d:"%i)
    for j in grupos[i]:
        print("\t\t    %-20d%s"%(int(j,2),j)) 
    print('-'*60)


# Crear tablas y encontrar los implicantes primos 
while True:
    implprimos = grupos.copy()
    grupos,m,marcados,debo_parar = {},0,set(),True
    l = sorted(list(implprimos.keys()))
    for i in range(len(l)-1):
        for j in implprimos[l[i]]: 
            for k in implprimos[l[i+1]]:
                res = compara(j,k)
                if res[0]: 
                    try:
                        grupos[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in grupos[m] else None
                    except KeyError:
                        grupos[m] = [j[:res[1]]+'-'+j[res[1]+1:]]
                    debo_parar = False
                    marcados.add(j) 
                    marcados.add(k) 
        m += 1
    desmarcados_local = set(recorta(implprimos)).difference(marcados) 
    all_pi = all_pi.union(desmarcados_local)
    print("Elementos desmarcados(Implicantes Primos) de la tabla:",None if len(desmarcados_local)==0 else ', '.join(desmarcados_local)) 
    if debo_parar:
        print("\n\nAll Implicantes Primos: ",None if len(all_pi)==0 else ', '.join(all_pi))
        break
    print("\n\n\n\nNúmero de Gpo\tMintérminos\t\tExpresión en BCD\n%s"%('='*60))
    for i in sorted(grupos.keys()):
        print("%5d:"%i) 
        for j in grupos[i]:
            print("\t\t%-24s%s"%(','.join(buscaMinterminos(j)),j)) 
        print('-'*60)

# Impresión de implicantes primos 
sim = len(str(mint[-1])) 
chart = {}
print('\n\n\nImpresión de los implicantes primos escenciales:\n\n  Mintérminos  |%s\n%s'%(' '.join((' '*(sim-len(str(i))))+str(i) for i in mint),'='*(len(mint)*(sim+1)+16)))
for i in all_pi:
    minterminos_mezclados,y = buscaMinterminos(i),0
    print("%-16s|"%','.join(minterminos_mezclados),end='')
    for j in reacomoda(minterminos_mezclados):
        x = mint.index(int(j))*(sim+1) 
        print(' '*abs(x-y)+' '*(sim-1)+'X',end='')
        y = x+sim
        try:
            chart[j].append(i) if i not in chart[j] else None 
        except KeyError:
            chart[j] = [i]
    print('\n'+'-'*(len(mint)*(sim+1)+16))

IPE = BuscarIPE(chart) 
print("\nImplicantes Primos Escenciales: "+', '.join(str(i) for i in IPE))
remueveTerminos(chart,IPE) 

if(len(chart) == 0): 
    resultado_final = [BuscarVariables(i) for i in IPE] 
else: 
    P = [[BuscarVariables(j) for j in chart[i]] for i in chart]
    while len(P)>1: 
        P[1] = multiplica(P[0],P[1])
        P.pop(0)
    resultado_final = [min(P[0],key=len)] 
    resultado_final.extend(BuscarVariables(i) for i in IPE) 
print('\nSolución: Y = '+' + '.join(''.join(i) for i in resultado_final))

input("\nPresione enter para salir ")
