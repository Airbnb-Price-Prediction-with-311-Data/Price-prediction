import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_graph():
    errors_file = pd.read_csv('../data-modeling/results/errors.csv')
    x = ['LinearReg', 'EnsembleBoost', 'XgBoost', 'Random Forest']
    y_errors = []
    y_errors = errors_file.loc[errors_file['Method'] == 'None', 'RMSE']
    y_errors_feature = []
    y_errors_feature = errors_file.loc[errors_file['Method'] == 'Forward Selection(15)', 'RMSE']
    y = y_errors
    y_features = y_errors_feature
    color = 'tab:green'
    fig, ax = plt.subplots()
    plot = sns.barplot(x=x, y=y,palette='summer',ax=ax,alpha=0.3 )
    plot = sns.scatterplot(x=x, y=y_features,color=color,s=100,ax=ax)
    plot = sns.lineplot(x=x, y=y_features,sort=False, color=color,ax=ax)
    fig1 = plot.get_figure()
    fig1.savefig("modeling_baselinevsforward.png")
    plot.get_figure().clf()
    
get_graph()

