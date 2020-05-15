import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_graph():
    errors_file = pd.read_csv('data_modeling/results/errors.csv')
    #errors_file['RMSE'] = pd.to_numeric(errors_file['RMSE'],errors='coerce')
    print (errors_file.dtypes)
    sns.set(style="whitegrid")
    g = sns.catplot(x="Method", y="RMSE", hue="model_name",kind="bar",data=errors_file, palette="bright",height=7, aspect=3)
    g.despine(left=True)
    g.set_ylabels("Error",color='black',size=15)
    g.set_xlabels("Feature Selection Method",color='black',size=15)
    plt.savefig("results_analysis/images/featureselectioncomparison.png")

#plot_graph()