import scipy.optimize as spo 

class IsingSpinModel_SciPy:
    def __init__(self, fileDataPointer: any, debug: bool=False) -> None:
        self.inputData = self.readFile(fileDataPointer)
        self.debug = debug


    def readFile(self, fileDataPointer: any) -> list:
        inputData: list = []
        try:
            for line in fileDataPointer:
                inputData.append([ int(i) for i in line.rstrip().split() ])
        except Exception as e:
            print('Invalid file data provided.')
        return inputData
    

    # Find the number of unique nodes
    def numNodes(self, inputData: int) -> int:
        nodes: list = []
        for u, v, weight in inputData:
            if u not in nodes: nodes.append(u)
            if v not in nodes: nodes.append(v)
        return len(nodes)


    # Calculate min state energy and spin state associated with it
    # eg. eqn = w1(x0 * x1) + w2(x1 * x2) + w3(x1 * x3) + w4(x0) + w5(x1) + w6(x2)    
    def groundStateEnergy(self) -> tuple | bool:
        if not len(self.inputData): return False

        # Calculate total energy for given spin config by summing J components
        def stateEnergy(permutation: list[int]):
            energy = 0
            for u, v, weight in self.inputData:
                if (u != v):
                    energy += (permutation[u] * permutation[v] * weight)
                else:
                    energy += (permutation[u] * weight)
            return energy 
            
        # Setting up params needed for scipy minimize API
        nodes: int = self.numNodes(inputData=self.inputData)
        permStart: list[int] = [ 1 ] * nodes
        bnds: tuple[tuple] = tuple([ tuple((-1, 1)) for _ in range(nodes) ])

        # Scipy minimize API to find min state energy and spin config
        result: any = spo.minimize(stateEnergy, permStart, options={'disp': self.debug}, bounds=bnds)
        if result.success:
            minEnergySpinConfig = ''.join([ '+' if int(i) == 1 else '-' for i in result.x ])
            return tuple((int(result.fun), minEnergySpinConfig))
        else:
            print('Error with spo optimize model.')
            return False


        
        





        
