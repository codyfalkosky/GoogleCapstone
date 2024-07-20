import matplotlib.pyplot as plt
import seaborn as sns

def plot_column(df, col, rotation=None, **kwargs):
    plt.figure(figsize=(10, 5))
    sns.set_theme()

    hist_params = {
        'hue'      : df['left'].map({0:'stay', 1:'left'}).to_numpy(),
        'hue_order': ['stay', 'left'],
        'multiple' : 'stack',
        'stat'     : 'probability',}

    plt.subplot(1,2,1)
    sns.histplot(data=df, x=col, **hist_params, **kwargs)
    if rotation:
        plt.xticks(rotation=rotation)

    plt.subplot(1, 2, 2)
    plt.axis('off')
    plt.text(0, .05,   f'{"Missing Data Count:":<20}{df[col].isna().sum()}')
    plt.text(0, .0,   f'{"Data Type:":<26}{df[col].dtype}')

        

    plt.suptitle(col)
    plt.show()
