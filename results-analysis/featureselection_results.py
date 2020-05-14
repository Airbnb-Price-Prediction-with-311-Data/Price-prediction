import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_graph():
    errors_file = pd.read_csv('../data-modeling/results/errors.csv')
    print (errors_file.columns)
    sns.set(style="whitegrid")
    g = sns.catplot(x="Method", y="RMSE", hue="model_name",kind="bar",data=errors_file, palette="bright",height=7, aspect=3)
    g.despine(left=True)
    g.set_ylabels("Error",color='black',size=15)
    g.set_xlabels("Feature Selection Method",color='black',size=15)
    plt.savefig("featureselectioncomparison.png")

plot_graph()