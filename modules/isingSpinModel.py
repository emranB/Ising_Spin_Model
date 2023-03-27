import itertools, sys


class IsingSpingModel:
    def __init__(self, fileDataPointer: any, debug: bool=False) -> None:
        self.inputData = self.readFile(fileDataPointer)
        self.debug = debug

    """ 
    Read from input file and split data into 2d array
    -   u,    v,  weight
    [ [ 0,    1,    1 ]
      [ 1,    2,    1 ]
      [ 1,    3,    1 ]
      [ 0,    0,   -1 ]
      [ 1,    1,   -1 ]
      [ 2,    2,   -1 ] ]
    """
    def readFile(self, fileDataPointer: any) -> list | bool:
        try:
            inputData: list = []
            for line in fileDataPointer:
                inputData.append([ int(i) for i in line.rstrip().split() ])
            return inputData
        except Exception as e:
            print('Invalid file data provided.')
            return False


    # Find the number of unique nodes
    def numNodes(self, inputData: int) -> int:
        nodes: list = []
        for u, v, weight in inputData:
            if u not in nodes: nodes.append(u)
            if v not in nodes: nodes.append(v)
        return len(nodes)


    # Find all possible permutations for n-bits
    def permutations(self, n: int) -> list[list[int]]:
        return [ list(i) for i in itertools.product([1, -1], repeat=n) ]


    # Calculate min state energy and spin state associated with it
    # eg. eqn = w1(x0 * x1) + w2(x1 * x2) + w3(x1 * x3) + w4(x0) + w5(x1) + w6(x2)    
    def stateEnergy(self, inputData: list[list[int]], spinConfig: list) -> int:
        energy: int = 0
        for u, v, weight in inputData: 
            if (u != v):
                energy += (spinConfig[u] * spinConfig[v] * weight)
            else:
                energy += (spinConfig[u] * weight)
        return energy 


    # Calculate min state energy and spin state associated with it
    # eg. eqn = w1(x0 * x1) + w2(x1 * x2) + w3(x1 * x3) + w4(x0) + w5(x1) + w6(x2)
    def groundStateEnergy(self) -> tuple | bool:
        if not self.inputData: return False
        
        nodes: int = self.numNodes(self.inputData)
        perms: list = self.permutations(nodes)

        minEnergy: int = sys.maxsize
        minEnergySpinConfig: list = []
        for perm in perms:
            currEnergy = self.stateEnergy(self.inputData, perm)
            if (currEnergy < minEnergy):
                minEnergy = currEnergy
                minEnergySpinConfig = perm

        minEnergySpinConfig = ''.join([ '+' if i == 1 else '-' for i in minEnergySpinConfig ])
        return tuple((minEnergy, minEnergySpinConfig))





