from sys import argv

P_h1 = [0.1,1.0,0.0]
P_h2 = [0.2,0.75,0.25]
P_h3 = [0.4,0.5,0.5]
P_h4 = [0.2,0.25,0.75]
P_h5 = [0.1,0.0,1.0]
P_C = 0.5
P_L = 0.5

try:
    Q = argv[1]
except:
    Q = None

f = open('result.txt','w')
f.write("Observation sequence Q: {}\n".format(Q))

def output():

    f.write('P(h1 | Q) = {}\n'.format(round(P_h1[0],5)))
    f.write('P(h2 | Q) = {}\n'.format(round(P_h2[0],5)))
    f.write('P(h3 | Q) = {}\n'.format(round(P_h3[0],5)))
    f.write('P(h4 | Q) = {}\n'.format(round(P_h4[0],5)))
    f.write('P(h5 | Q) = {}\n'.format(round(P_h5[0],5)))

    f.write('Probability that the next candy we pick will be C, given Q: {}\n'.format(round(P_C,5)))
    f.write('Probability that the next candy we pick will be L, given Q: {}\n'.format(round(P_L,5)))

if Q is None:
    output()
else:
    f.write("Length of Q: {}\n".format(len(Q)))
    for i in range(len(Q)):
        
        if Q[i]=='C':
            P_h1[0] = (P_h1[1]*P_h1[0])/P_C
            P_h2[0] = (P_h2[1]*P_h2[0])/P_C
            P_h3[0] = (P_h3[1]*P_h3[0])/P_C
            P_h4[0] = (P_h4[1]*P_h4[0])/P_C
            P_h5[0] = (P_h5[1]*P_h5[0])/P_C
            P_C = P_h1[0]*P_h1[1]+P_h2[0]*P_h2[1]+P_h3[0]*P_h3[1]+P_h4[0]*P_h4[1]+P_h5[0]*P_h5[1]
            P_L = P_h1[0]*P_h1[2]+P_h2[0]*P_h2[2]+P_h3[0]*P_h3[2]+P_h4[0]*P_h4[2]+P_h5[0]*P_h5[2]
            f.write('After Observation {} = C:\n'.format(i+1))
        
        elif Q[i]=='L':
            P_h1[0] = (P_h1[2]*P_h1[0])/P_L
            P_h2[0] = (P_h2[2]*P_h2[0])/P_L
            P_h3[0] = (P_h3[2]*P_h3[0])/P_L
            P_h4[0] = (P_h4[2]*P_h4[0])/P_L
            P_h5[0] = (P_h5[2]*P_h5[0])/P_L
            P_C = P_h1[0]*P_h1[1]+P_h2[0]*P_h2[1]+P_h3[0]*P_h3[1]+P_h4[0]*P_h4[1]+P_h5[0]*P_h5[1]
            P_L = P_h1[0]*P_h1[2]+P_h2[0]*P_h2[2]+P_h3[0]*P_h3[2]+P_h4[0]*P_h4[2]+P_h5[0]*P_h5[2]
            f.write('After Observation {} = L:\n'.format(i+1))
            
        else:
            f.write('Only C and L are considered as observations, please provide either one of those')
        output()