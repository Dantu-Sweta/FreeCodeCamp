import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axis = plt.subplots(figsize=(10, 6))

    axis = plt.plot(df.index, df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    # sns.lineplot(data = df)
  

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index().sort_values(by = ['year', 'month'])
    df_bar = df_bar.set_index('year')
    df_bar = df_bar.pivot_table(values = 'value', index = df_bar.index, columns = 'month', aggfunc = 'first').reset_index()
    df_bar = df_bar.set_index('year')
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar= df_bar.fillna(0)

    #plotting 
    fig, axis = plt.subplots()
    plot = df_bar.plot.bar(rot = 0, ax = axis)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title = 'months')
    




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [date.year for date in df_box.date]
    df_box['month'] = [date.strftime('%b') for date in df_box.date]
    fig, (axis1, axis2) = plt.subplots(1, 2)
    fig.set_figheight(15)
    fig.set_figwidth(60)

    sns.boxplot(ax = axis1, x="year", y= "value", data = df_box) 
    axis1.set_title("Year-wise Box Plot (Trend)")
    axis1.set_xlabel("Year")
    axis1.set_ylabel("Page Views")

    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    sns.boxplot(ax = axis2, x="month", y= "value", data=df_box, order = month_order) 
    axis2.set_title('Month-wise Box Plot (Seasonality)')
    axis2.set_xlabel('Month')
    axis2.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
