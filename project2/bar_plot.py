import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-fn', '--filenames', type=str, nargs="*")
parser.add_argument('-o', '--outputFile', type=str)
parser.add_argument('-t', '--topPercent', type=float)
parser.add_argument('-c', '--column', type=str)
args = parser.parse_args()

op = [0.1, 0.4, 0.4]
col_name = ["Genome", "Ave_fit", "Std_fit", "Sum_fit", "Ave_thr", "Std_thr", "Seed", "Num_Learning", "Num_Mating"]

fig = plt.figure(figsize = (10, 5))
op_i=0
for filename in args.filenames:
    df = pd.read_csv(filename)
    # df_sorted = df.sort_values("Ave_fit", ascending = False).head(n = int(len(df.index)*args.topPercent))
    # df_sorted = df.sort_values("Sum_fit", ascending = False).head(n = int(len(df.index)*args.topPercent))
    df_sorted = df.sort_values(args.column, ascending = False).head(n = int(len(df.index)*args.topPercent))

    su = [0] * len(df["Genome"][0].split(","))
    x_label = range(len(df["Genome"][0].split(",")))
    for g in df_sorted["Genome"]:
        genome = [int(x) for x in g.split("[", 1)[1].split("]", 1)[0].split(",")]
        for i in range(len(genome)):
            su[i] += genome[i]
    
    su = list(map(lambda x: 100*x/int(len(df.index)*args.topPercent),su))
    # creating the bar plot
    plt.bar(x_label, su, alpha=0.2,label = "Length = "+str(len(df["Genome"][0].split(","))), edgecolor = "black")
    op_i+=1
 

plt.xlabel("Loci position")
plt.ylabel("% chooses to Learn")
# plt.legend((p[0][0], p[1][0], p[2][0]), ('10', '3', '5'))
# plt.show()
plt.legend()
plt.savefig(args.outputFile)

