mat = float(input())
fis = float(input())
qui = float(input())
por = float(input())

cond = 0

if mat>=65 and fis >=55 and qui >=50: cond+=1

if mat+fis+qui+por >= 240: cond+=1

if (mat+fis >=130) or (mat+qui>=120) or (fis+qui >=110): cond+=1

if por >=70: cond+=1
else:
    if mat>=70 or fis >=70 or qui>=70: cond+=1
    
if cond == 4:
    print("Candidato aprovado!!!")
    
else:
    print("Candidato reprovado!!!")