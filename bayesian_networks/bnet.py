from sys import argv

P_B = 0.001
P_E = 0.002
P_A_B_E = 0.95
P_A_B_nE = 0.94
P_A_nB_E = 0.29
P_A_nB_nE = 0.001
P_J_A = 0.90
P_J_nA = 0.05
P_M_A = 0.70
P_M_nA = 0.01

parents = {'A':['B','E'],'J':['A'],'M':['A']}

conditions = []

def Probability(attri):
    res = 1
    att = attri.split()
    for i in att:
        if i == 'Bt':
            res *= P_B
        elif i == 'Bf':
            res *= 1 - P_B
        elif i == 'Et':
            res *= P_E
        elif i == 'Ef':
            res *= 1 - P_E
        elif i == 'At':
            if 'Bt' in att and 'Et' in att:
                res *= P_A_B_E
            elif 'Bt' in att and 'Ef' in att:
                res *= P_A_B_nE
            elif 'Bf' in att and 'Et' in att:
                res *= P_A_nB_E
            elif 'Bf' in att and 'Ef' in att:
                res *= P_A_nB_nE
        elif i == 'Af':
            if 'Bt' in att and 'Et' in att:
                res *= 1 - P_A_B_E
            elif 'Bt' in att and 'Ef' in att:
                res *= 1 - P_A_B_nE
            elif 'Bf' in att and 'Et' in att:
                res *= 1 - P_A_nB_E
            elif 'Bf' in att and 'Ef' in att:
                res *= 1 - P_A_nB_nE
        elif i == 'Jt':
            if 'At' in att:
                res *= P_J_A
            elif 'Af' in att:
                res *= P_J_nA
        elif i == 'Jf':
            if 'At' in att:
                res *= 1 - P_J_A
            elif 'Af' in att:
                res *= 1 - P_J_nA
        elif i == 'Mt':
            if 'At' in att:
                res *= P_M_A
            elif 'Af' in att:
                res *= P_M_nA
        elif i == 'Mf':
            if 'At' in att:
                res *= 1 - P_M_A
            elif 'Af' in att:
                res *= 1- P_M_nA
    return res

def enumeration(attr):
    sum = 0
    comb = []
    prob = ''
    Required = attr
    known = []
    for i in attr:
        known.append(i[0])
    for i in attr:
        if i[0] in parents:
            lst = parents[i[0]]
            for j in lst:
                if j not in known:
                    known.append(j)
                    Required.append(j)
    for i in Required:
        if len(i)==2:
            prob += i+' '
    comb.append(prob)

    for i in Required:
        if len(i)==1:
            comb *= 2
            temp = len(comb)//2
            for j in range(temp):
                comb[j]+=i+'t '
            for j in range(temp,temp*2):
                comb[j]+=i+'f '
    for i in comb:
        sum = sum + Probability(i)
    return sum

if len(argv) <2 or len(argv)>7:
    print("Arguments should be between 1 and 6")
else:
    attributes = argv[1:]
    if 'given' in attributes:
        conditions = attributes[attributes.index('given')+1:]
        attributes.remove('given')
        numerator = enumeration(attributes)
        denominator = enumeration(conditions)
        final_probability = numerator/denominator
        print('Probability = {}\n'.format(final_probability))
    else:
        final_probability = enumeration(attributes)
        print('Probability = {}\n'.format(final_probability))
