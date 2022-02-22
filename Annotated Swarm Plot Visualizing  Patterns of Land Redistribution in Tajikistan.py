#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce
pd.options.mode.chained_assignment = None
get_ipython().run_line_magic('matplotlib', 'notebook')

def land():
    df=pd.read_csv("C:\\Users\\14024\\Desktop\\Land Data\\jamoat_2021.csv")
    #return df["landref_2019"].median()
    # #ax = sns.scapplot(x="croparea", y="landref_2012", data=df)
    
    #sns.catplot(x="croparea", y="landref_2012", kind="swarm", data=df)
    #ax = sns.violinplot(x="croparea", y="landref_2012", data=df,
     #  color=".8")
    a = df['landref_2012'].eq(1).groupby(df['croparea']).mean().reset_index()
    #a = df.groupby(df["croparea"]).mean().reset_index()
    #return a
    fig, axes = plt.subplots(2,2,figsize=(9,9),sharey=True)
    #sns.set(style="whitegrid")
    fig.subplots_adjust(hspace=0.3)
    ttl = axes[0,0].title 
    ttl.set_position([.5, 1.05])
    
    ttl = axes[0,1].title
    ttl.set_position([.5, 1.05])
    
    ttl = axes[1,0].title
    ttl.set_position([.5, 1.05])
    
    ttl = axes[1,1].title
    ttl.set_position([.5, 1.05])
    
    
    #fig.subplots_adjust(hspace=8)
    #plt.subplots_adjust(hspace = 20)
    fig.suptitle("Extent of Farm Individualizaiton in Tajikistan in 2012 and 2019",fontsize=12)


    #plt.figure(linewidth=5)
    ax=sns.swarmplot(y=df["landref_2012"],ax=axes[0,0], color="yellow", linewidth=0.5, alpha = 1)
    median_width = 0.65
    for tick, text in zip(ax.get_xticks(), ax.get_xticklabels()):
        median_val = df["landref_2012"].median()
        ax.plot([tick-median_width/2, tick+median_width/2], [median_val, median_val], lw=2, color='red')
    axes[0,0].set(ylabel="Proportion of Arable Land in Family Farms in Jamoat")
    axes[0,0].set_title('Amount of Arable Land in Family Farms(ha)\n in 329 Jamoats of Tajikistan in 2012', size=10)
    axes[0,0].legend(loc=4,frameon=False,bbox_to_anchor=(0.5,0.029,0.7,0.8), fontsize="8")
    axes[0,0].spines["top"].set_visible(False)
    axes[0,0].spines["right"].set_visible(False)
    axes[0,0].spines["left"].set_visible(False)
    axes[0,0].spines["bottom"].set_visible(False)
    axes[0,0].tick_params(bottom=False)
    
    axes[0,0].annotate('median', xy=(0.3, 0.28),xytext=(0.5,0.5),arrowprops=dict(arrowstyle='->', color='black'))
    
    # Plot 2
    ax=sns.swarmplot(y=df["landref_2019"],ax=axes[0,1], color="yellow", linewidth=0.5, alpha = 1)
    median_width = 0.7
    for tick, text in zip(ax.get_xticks(), ax.get_xticklabels()):
        median_val = df["landref_2019"].median()
        ax.plot([tick-median_width/2, tick+median_width/2], [median_val, median_val], lw=2, color='red')
    axes[0,1].set_title('Amount of Arable Land in Family Farms(ha)\n in 329 Jamoats of Tajikistan in 2019', size=10)
    axes[0,1].set(xlabel="", ylabel = "")
    axes[0,1].legend(loc=4,frameon=False,bbox_to_anchor=(0.5,0.029,0.7,0.8), fontsize="8")
    axes[0,1].spines["left"].set_visible(False)
    axes[0,1].spines["top"].set_visible(False)
    axes[0,1].spines["right"].set_visible(False)
    axes[0,1].spines["bottom"].set_visible(False)
    axes[0,1].tick_params(left=False, bottom=False)
    
    #axes[0,1].set_yticks([])
    # Plot 3
    ax=sns.swarmplot(x="croparea", y="landref_2012",ax=axes[1,0], data=df,color="yellow", linewidth=0.5, alpha = 1 )#, data=df, #color="lightgreen", linewidth=1, alpha = 1)
    median_width = 0.8
    for tick, text in zip(ax.get_xticks(), ax.get_xticklabels()):
        sample_name = text.get_text()  # "X" or "Y"
        median_val = df[df['croparea']==sample_name].landref_2012.median()
        ax.plot([tick-median_width/2, tick+median_width/2], [median_val, median_val], lw=2, color='red')
    axes[1,0].set_title('Amount of Arable Land in Family Farms(ha)\n in 329 Jamoats of Tajikistan in 2012 by Crop Type', size=10)
    axes[1,0].set(xlabel="", ylabel = "Proportion of Arable Land in Family Farms in Jamoat")
    axes[1,0].legend(loc=4,frameon=False,bbox_to_anchor=(0.5,0.029,0.7,0.8), fontsize="8")
    axes[1,0].spines["left"].set_visible(False)
    axes[1,0].spines["top"].set_visible(False)
    axes[1,0].spines["right"].set_visible(False)
    axes[1,0].set_xticklabels( ('Cotton-growing', 'Noncotton-growing') )
    axes[1,0].set(xlabel='Type of Jamoat')
    axes[1,0].spines["bottom"].set_visible(False)
    axes[1,0].tick_params(bottom=False)
    
    # Plot 4
    ax=sns.swarmplot(x="croparea", y="landref_2019",ax=axes[1,1],data=df,color="yellow", linewidth=0.5, alpha = 1)
    median_width = 0.7
    for tick, text in zip(ax.get_xticks(), ax.get_xticklabels()):
        sample_name = text.get_text()  # "X" or "Y"
        median_val = df[df['croparea']==sample_name].landref_2019.median()
        ax.plot([tick-median_width/2, tick+median_width/2], [median_val, median_val], lw=2, color='red')
    axes[1,1].set_title('Amount of Arable Land in Family Farms(ha)\n in 329 Jamoats of Tajikistan in 2019 by Crop Type', size=10)
    #axes[1,1].set(xlabel="Type of Jamoat", ylabel = "")
    axes[1,1].set(xlabel=" ", ylabel = " ")
    axes[1,1].legend(loc=4,frameon=False,bbox_to_anchor=(0.5,0.029,0.7,0.8), fontsize="8")
    axes[1,1].spines["left"].set_visible(False)
    axes[1,1].spines["top"].set_visible(False)
    axes[1,1].spines["right"].set_visible(False)
    axes[1,1].set_xticklabels( ('Cotton-growing', 'Noncotton-growing') )
    axes[1,1].set(xlabel='Type of Jamoat')
    axes[1,1].spines["bottom"].set_visible(False)
    axes[1,1].tick_params(left=False, bottom=False)
    plt.show();
    
    
    #sns.stripplot(y=df["landref_2012"],picker=5, color="green")
    #def onpick(event):
        #origin = df.iloc[event.ind[0]]['Country']
        #plt.gca().set_title('Selected item came from {}'.format(origin))

    #plt.gcf().canvas.mpl_connect('pick_event', onpick)
   
    
land()


# In[ ]:




