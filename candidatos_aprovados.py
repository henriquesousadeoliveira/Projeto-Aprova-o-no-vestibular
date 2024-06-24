def filtra_candidatos(candidatos, cats_regra, limite, ja_selecionados):
    selecionados = []
    for ordem, inscricao, cats_cand in candidatos:
        if len(selecionados) >= limite:
            break
        if inscricao not in ja_selecionados and len(cats_cand.intersection(cats_regra)) >= 1:
            selecionados.append(inscricao)
    return selecionados 

# Leitura dos dados
vagas = dict()
regras = []
while True:
    regra = input()
    if regra == '0 0':
        break
    npasso, nregra, cat_regra, prioridades = regra.split()
    prioridades = [ set(prior.split(',')) for prior in prioridades.split(';') ]
    regra = [int(npasso), int(nregra), cat_regra, prioridades ]
    regras.append(regra)
    vagas[cat_regra] = 0

for _ in range(len(vagas)):
    cat, qtd_vagas = input().split()
    vagas[cat] = int(qtd_vagas)

candidatos = []
num_cand = int(input())
for _ in range(num_cand):
    ordem, inscricao, cats_regra = input().split()
    cand = [int(ordem), int(inscricao), set(cats_regra.split(','))]
    candidatos.append(cand)
    
# Seleção dos candidatos
selecionados = set()
for npasso, nregra, cat_regra, prioridades in regras:
    for prior in prioridades:
        inscricoes = filtra_candidatos(candidatos, prior, vagas[cat_regra], selecionados)
        selecionados.update(inscricoes)
        vagas[cat_regra] -= len(inscricoes)
for inscricao in sorted(selecionados):
    print(inscricao)