# plotting
import seaborn as sns
from zmq import EVENT_CLOSE_FAILED
sns.set(font_scale=1)
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke
import numpy as np

# ML
from sklearn.linear_model import LinearRegression

# others
import life_quality_and_government.utils.paths as path


# colors for bars, argentina is different color
BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#aaaaaa"
GREEN = "#07521f"
ORANGE = "#FF8B00ff"

def barh_plot(countries, variable, title, sources, save_name, is_gdp=False):
    """
    giving list of countries and a variable to plot, plot a horizontal bar plot with a fixed format.
    If is_gdp=True, a format of NNk will be used instead of the std range 0 to 1
    """
    matplotlib.rc_file_defaults()

   
    colors = list()
    for country in countries:
        if country=='Argentina':
            colors.append(GREEN)
        elif country in ['Mean','Median']:
            colors.append(ORANGE)
        else:
            colors.append(BLUE)

    fig, ax = plt.subplots(figsize=(10, 10*0.625))
    ax.barh( countries,variable, height=0.7, align="center", color=colors);
    ax.invert_yaxis();

    # tick params
    ax.xaxis.set_tick_params(labelbottom=True, length=0)
    ax.yaxis.set_tick_params( length=0)

    # Set whether axis ticks and gridlines are above or below most artists.
    ax.set_axisbelow(True)
    ax.grid(axis = "x", color="#A8BAC4", lw=1.2)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_lw(1.5)

    # Hide y labels
    ax.yaxis.set_visible(False)

    # adding labels
    bar_range = max(variable) - min(variable)
    bar_max = max(variable)


    if is_gdp:
        for i, (country, variable) in enumerate(zip(countries, variable)):
            if variable > bar_max*0.3:
                plt.text(s=country, x=bar_max*0.025, y=i, color="w", verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                plt.text(s= str(round(variable/1000,1))+'k', x=variable*0.975, y=i, color="w",
                        verticalalignment="center", horizontalalignment="right", size=14, fontdict={'fontweight':'600'})
            else:
                if country=='Argentina':
                    plt.text(s=country, x=variable*1.05, y=i, color=GREEN, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= str(round(variable/1000,1))+'k', x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                elif country in ['Mean','Median']:
                    plt.text(s=country, x=variable*1.05, y=i, color=ORANGE, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= str(round(variable/1000,1))+'k', x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                else:
                    plt.text(s=country, x=variable*1.05, y=i, color=BLUE, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= str(round(variable/1000,1))+'k', x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})

    else:
        for i, (country, value) in enumerate(zip(countries, variable)):
            if value > bar_max*0.3:
                plt.text(s=country, x=bar_max*0.025, y=i, color="w", verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                plt.text(s= round(value,2), x=value*0.975, y=i, color="w",
                        verticalalignment="center", horizontalalignment="right", size=14, fontdict={'fontweight':'600'})
            else:
                if country=='Argentina':
                    plt.text(s=country, x=value*1.025, y=i, color=GREEN, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= round(value,2), x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                elif country in ['Mean','Median']:
                    plt.text(s=country, x=value*1.025, y=i, color=ORANGE, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= round(value,2), x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                else:
                    plt.text(s=country, x=value*1.025, y=i, color=BLUE, verticalalignment="center", size=14,fontdict={'fontweight':'600'})
                    plt.text(s= round(value,2), x=bar_max*0.025, y=i, color="w",
                            verticalalignment="center", size=14,fontdict={'fontweight':'600'})


    # margins

    fig.subplots_adjust(left=0.01, right=1, top=0.95, bottom=0.1)

    # Title

    ax.set_title(title, fontdict={'fontsize':16, 'fontweight':'bold'})

    # Add caption
    source = sources
    fig.text(
        0.01, 0.04, source, color=GREY, 
        fontsize=10
    )

    # Add authorship
    fig.text(
        0.01, 0.01, "Author: Gonzalo Giampaolo", color=GREY,
        fontsize=12
    )
    plt.savefig(path.reports_figures_dir(save_name+'.png'))


def scatter_regression_plot(df, x, y, hue, x_label, y_label, title, sources, save_name, regression='linear'):
    """
    Print a scatter plot with a regression line (linear or log)
    """

    # df for linear regression
    df_lr = df.copy( deep=True)
    # drop columns with GQ = 0 and NaNs
    df_lr.dropna(subset=[x, y], inplace=True)
    df_lr = df_lr.drop(index=df_lr.loc[(df_lr[x]==0)].index);

    if regression=='log':
        # drop some outliers for the LR
        df_lr = df_lr.drop(
            index=df_lr.loc[(df_lr[x]<0.2) & (df_lr[y]>0.5)].index)
            
        df_lr = df_lr.drop(
            index=df_lr.loc[(df_lr[x]>0.3) & (df_lr[y]<0.5)].index)
        df_lr = df_lr.drop(
            index=df_lr.loc[(df_lr[x]>0.4) & (df_lr[y]<0.6)].index)

        # transform series into arrays

        X = np.array(df_lr[x]).reshape(-1, 1)
        Y = np.array(df_lr[y])

        # Initialize linear regression object
        linear_regressor = LinearRegression()

        # Fit linear regression model of HDI on the log of CPI
        linear_regressor.fit(np.log(X), Y)


        # Make predictions
        # * Construct a sequence of values ranging from 0.05 to 0.95  and
        #   apply logarithmic transform to them.
        x_pred = np.array([np.log(x/100) for x in range(10,105,1)]).reshape(-1, 1)

        # * Use .predict() method with the created sequence
        y_pred = linear_regressor.predict(x_pred)
    else:
        # transform series into arrays

        X = np.array(df_lr[x]).reshape(-1, 1)
        Y = np.array(df_lr[y])

        # Initialize linear regression object
        linear_regressor = LinearRegression()

        # Fit linear regression model of LQI on the log of CPI
        linear_regressor.fit(X, Y)


        # Make predictions
        # * Construct a sequence of values ranging from 0.05 to 0.95  and
        #   apply logarithmic transform to them.
        x_pred = np.array([x/100 for x in range(25,105,1)]).reshape(-1, 1)

        # * Use .predict() method with the created sequence
        # This is used for plotting
        y_pred = linear_regressor.predict(x_pred)
        y_pred_x = linear_regressor.predict(X)
    
    #### PLOTING
    fig = plt.figure(figsize=(10,7));
    sns.set_style('darkgrid')
    ## scatter plot
    ax = sns.scatterplot(data=df, x = x,
        y = y, zorder=10, hue=hue,size=hue, palette="inferno",
        legend='brief', sizes=(15,100));

    ## regression line
    if regression == 'log':     
        plt.plot(np.exp(x_pred),y_pred, color='grey', lw=4)
    else:
        plt.plot(x_pred,y_pred, color='grey', lw=4)



    ## annotations
    if y == 'HDI':     
        text_relative_pos={'Argentina':(-0.1,0.05),'Chile':(0.1,-0.3),'China':(0.2,-0.4),'Germany':(-0.05,0.05),'Ghana':(0.2,-0.4),
        'Libya':(0,0.05),'Norway':(0.05,-0.2),'United States':(-0.1,0.05),'Uruguay':(0.1,-0.3),'Niger':(0.1,-0.2)}
    elif y == 'LQI':
        text_relative_pos={'Argentina':(-0.2,0.2),'Chile':(0.05,-0.1),'China':(0.075,-0.1),'Germany':(-0.125,0.075),
        'Peru':(0.025,-0.05),'Norway':(0.025,-0.15),'United States':(-0.15,0.075),'Uruguay':(0.1,-0.3),
        'Nigeria':(0.025,0.1),'Denmark':(-0.1,0.0125),'Italy':(-0.2,0.175)}
    
    to_annotate = df[['Country Name',x,y]].values


    for i,info in enumerate(to_annotate):
        if info[0] in list(text_relative_pos.keys()):
            ax.annotate(info[0], xy=(info[1], info[2]),  xycoords='data',
                xytext=(info[1]+text_relative_pos[info[0]][0], info[2]+text_relative_pos[info[0]][1]),
                textcoords='axes fraction', horizontalalignment='right', verticalalignment='top',
                arrowprops=dict(width=2,facecolor='grey', shrink=0.0, headlength=0.01),
                )

    # margins

    fig.subplots_adjust(left=0.005, right=1, top=0.95, bottom=0.125)

    ## seteos plot
    ax.set_xlabel(x_label, fontsize=16)
    ax.set_ylabel(y_label, fontsize=16)
    ax.set_title(title, fontdict={'fontsize':18, 'fontweight':'700'})

    ## limits

    if y == 'HDI':     
        ax.set_xlim(0.1, 1.05)
        ax.set_ylim(0.375, 1)
    elif y == 'LQI':
        ax.set_xlim(0.225, 1.05)
        #ax.set_ylim(0.375, 1)

    
    # Add caption
    source = "Sources: " + sources
    fig.text(
        -0.05, 0.005, source, color=GREY, 
        fontsize=10
    )

    # Add authorship
    fig.text(
        -0.05, 0.03, "Author: Gonzalo Giampaolo", color=GREY,
        fontsize=12
    )

    plt.savefig(path.reports_figures_dir(save_name+'.png'), bbox_inches = 'tight')
    plt.show();
                    

