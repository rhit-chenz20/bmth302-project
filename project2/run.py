
import argparse
from model import FemaleMatingModel
import genome

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-fs', '--femaleSize', type=int, default=100, required=False)
parser.add_argument('-ml', '--matingLength', type=int)
parser.add_argument('-ms', '--maleSigma', type=float)
parser.add_argument('-fit', '--fitnessFunction', type=int, default=0, required=False)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-seed', '--seed', type = float, default=-1, required=False)
args = parser.parse_args()

for g in genome.generate_genome(args.matingLength):
    # print(g)
    model = FemaleMatingModel(
        args=args,
        genome = g
    )

    # model.start()

