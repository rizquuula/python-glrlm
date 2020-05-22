def SRE(mat0, mat45, mat90, mat135):
    inputMatrix = (mat0, mat45, mat90, mat135)
    matSRE = []
    for inputMatrix in inputMatrix:
        S = 0
        SRE = 0
        for x in range(inputMatrix.shape[1]):
            for y in range(inputMatrix.shape[0]):
                S += inputMatrix[y][x]

        for x in range(inputMatrix.shape[1]):
            Rj = 0
            for y in range(inputMatrix.shape[0]):
                Rj += inputMatrix[y][x]

            SRE += (Rj/S)/((x+1)**2)
            # print('( ',Rj,'/',S,' ) / ',(x+1)**2)
        SRE = round(SRE, 3)
        matSRE.append(SRE)

    # print('Perhitungan SRE')
    return round(sum(matSRE),3)

def LRE(mat0, mat45, mat90, mat135):
    inputMatrix = (mat0, mat45, mat90, mat135)
    matLRE = []
    for inputMatrix in inputMatrix:
        S = 0
        LRE = 0
        for x in range(inputMatrix.shape[1]):
            for y in range(inputMatrix.shape[0]):
                S += inputMatrix[y][x]

        for x in range(inputMatrix.shape[1]):
            Rj = 0
            for y in range(inputMatrix.shape[0]):
                Rj += inputMatrix[y][x]

            LRE += (Rj * ((x + 1) ** 2)) / S
            # print('( ', Rj ,' * ',((x + 1) ** 2), ' ) /', S)
        LRE = round(LRE, 3)
        matLRE.append(LRE)
    # print('Perhitungan LRE')
    return round(sum(matLRE),3)

def GLU(mat0, mat45, mat90, mat135):
    inputMatrix = (mat0, mat45, mat90, mat135)
    matGLU = []
    for inputMatrix in inputMatrix:
        S = 0
        GLU = 0
        for x in range(inputMatrix.shape[1]):
            for y in range(inputMatrix.shape[0]):
                S += inputMatrix[y][x]

        for x in range(inputMatrix.shape[1]):
            Rj = 0
            for y in range(inputMatrix.shape[0]):
                Rj += inputMatrix[y][x]

            GLU += ((x + 1) ** 2) / S
            # print('( ',((x + 1) ** 2), ' ) /', S)
        GLU = round(GLU, 3)
        matGLU.append(GLU)
    # print('Perhitungan GLU')
    return round(sum(matGLU),3)

def RLU(mat0, mat45, mat90, mat135):
    inputMatrix = (mat0, mat45, mat90, mat135)
    matRLU = []
    for inputMatrix in inputMatrix:
        S = 0
        RLU = 0
        for x in range(inputMatrix.shape[1]):
            for y in range(inputMatrix.shape[0]):
                S += inputMatrix[y][x]

        for x in range(inputMatrix.shape[1]):
            Rj = 0
            for y in range(inputMatrix.shape[0]):
                Rj += inputMatrix[y][x]

            RLU += (Rj ** 2) / S
            # print('( ', (Rj ** 2), ' ) /', S)
        RLU = round(RLU, 3)
        matRLU.append(RLU)
    # print('Perhitungan RLU')
    return round(sum(matRLU),3)

def RPC(mat0, mat45, mat90, mat135):
    inputMatrix = (mat0, mat45, mat90, mat135)
    matRPC = []
    for inputMatrix in inputMatrix:
        S = 0
        RPC = 0
        for x in range(inputMatrix.shape[1]):
            for y in range(inputMatrix.shape[0]):
                S += inputMatrix[y][x]

        for x in range(inputMatrix.shape[1]):
            Rj = 0
            for y in range(inputMatrix.shape[0]):
                Rj += inputMatrix[y][x]

            RPC += (Rj) / (inputMatrix.shape[0]*inputMatrix.shape[1])
            # print('( ', (Rj), ' ) /', inputMatrix.shape[0]*inputMatrix.shape[1])
        RPC = round(RPC, 3)
        matRPC.append(RPC)
    # print('Perhitungan RPC')
    return round(sum(matRPC),3)