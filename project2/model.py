import random
from fitness_function import FitnessFunction
from dataProcess import DataProcessor
from agent import Female
from copy import deepcopy

class FemaleMatingModel():
    """
    args: femaleSize, matingLength, maleSigma,fitnessFunction, filename, seed
    """
    def __init__(
        self,
        args,
        genome
    ):
        if args.seed!=-1:
            seed = args.seed
        else:
            seed = random.randint(0,100000)
        self.ran = random.seed(args.seed) 
        # self.dataPro = DataProcessor(seed, args.filename, args.matingLength)
        self.matingLength = args.matingLength
        self.maleSigma = args.maleSigma
        self.females = self.generateFemale(args.femaleSize, genome)
        self.fitness_function = FitnessFunction.get_fitness_function(args.fitnessFunction)
        
    def generateFemale(self, size, genome):
        """
        Generate females
        """
        pop = []
        for x in range(size):
            pop.append(Female(genome = deepcopy(genome)))
        return pop
