from abc import abstractmethod

class FitnessFunction():
    def get_fitness_function(num):
        if(num == 0):
            return AverageFitness()
        elif (num == 1):
            return LowestFitness()

    @abstractmethod
    def cal_fitness(self, female):
        pass

class AverageFitness(FitnessFunction):
    def cal_fitness(self, female):
        if(len(female.mates) != 0):
            female.fitness = sum(female.mates) / len(female.mates)
        else:
            female.fitness = 0

class LowestFitness(FitnessFunction):
    def cal_fitness(self, female):
        if(len(female.mates) == 0):
            female.fitness = 0
        else: 
            female.fitness = min(female.mates)

