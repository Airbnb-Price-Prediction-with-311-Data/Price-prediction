import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

def clean_data(airbnb):
    airbnb["reviews_per_month"].fillna(0, inplace = True) 
    airbnb.drop(['host_name','last_review'], axis=1, inplace=True)
    airbnb.drop(['name'], axis=1, inplace=True)


def corr_kendall(airbnb):
    corr = airbnb.corr(method='kendall')
    plt.figure(figsize=(15,8))
    heat_map = sns.heatmap(corr, annot=True)
    fig1 = heat_map.get_figure()
    fig1.savefig("images/correlation-heatmap-kendall.png")
    heat_map.get_figure().clf()


def corr_pearson(airbnb):
    corr = airbnb.corr(method='pearson')
    plt.figure(figsize=(15,8))
    heat_map = sns.heatmap(corr, annot=True)
    fig2 = heat_map.get_figure()
    fig2.savefig("images/correlation-heatmap-pearson.png")
    heat_map.get_figure().clf()



def corr_spearman(airbnb):
    corr = airbnb.corr(method='spearman')
    plt.figure(figsize=(15,8))
    heat_map = sns.heatmap(corr, annot=True)
    fig3 = heat_map.get_figure()
    fig3.savefig("images/correlation-heatmap-spearman.png")
    heat_map.get_figure().clf()



def neighbourhood_group_vs_count(airbnb):
    countplot = sns.countplot(airbnb['neighbourhood_group'], palette="plasma")
    fig4 = plt.gcf()
    fig4.set_size_inches(10,10)
    plt.title('Neighbourhood Group')
    fig4.savefig("images/neighbourhood-group-vs-count.png")
    countplot.get_figure().clf()


def room_type_vs_count(airbnb):
    countplot = sns.countplot(airbnb['room_type'], palette="plasma")
    fig5 = plt.gcf()
    fig5.set_size_inches(10,10)
    plt.title('Room Type')
    fig5.savefig("images/room-type-vs-count.png")
    countplot.get_figure().clf()


def neighbourhood_vs_count(airbnb):
    ax = sns.countplot(airbnb['neighbourhood'], palette="plasma")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
    fig6 = plt.gcf()
    fig6.set_size_inches(60,15)
    plt.title('Neighbourhood')
    fig6.savefig("images/neighbourhood-vs-count.png")
    ax.get_figure().clf()


def calculated_host_listings_vs_count(airbnb):
    countplot = sns.countplot(airbnb['calculated_host_listings_count'], palette="plasma")
    fig7 = plt.gcf()
    fig7.set_size_inches(10,5)
    plt.title('Calculated Host Listings Count')
    fig7.savefig("images/calculated-host-listings-vs-count.png")
    countplot.get_figure().clf()


airbnb = pd.read_csv('../../dataset/AB_NYC_2019.csv')
clean_data(airbnb)
corr_kendall(airbnb)
corr_pearson(airbnb)
corr_spearman(airbnb)
neighbourhood_group_vs_count(airbnb)
room_type_vs_count(airbnb)
neighbourhood_vs_count(airbnb)
calculated_host_listings_vs_count(airbnb)