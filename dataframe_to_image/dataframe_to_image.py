import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def convert(df,visualisation_library):
    """
    Returns a downloadable image version of a dataframe
    Input: Pandas DataFrame
    Output: Downloadable Image
    """
    if visualisation_library=='matplotlib':
        #defaults
        col_width=2.0
        row_height=0.625
        font_size=14
        header_color='#110a1f' 
        row_colors=['#f1f1f2', 'w']
        edge_color='w'
        bbox=[0, 0, 1, 1] 
        header_columns=0
        ax=None
        if ax is None:
            size = (np.array(df.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
            fig, ax = plt.subplots(figsize=size)
            ax.axis('off')
        mpl_table = ax.table(cellText=df.values, bbox=bbox, colLabels=df.columns)
        mpl_table.auto_set_font_size(False)
        mpl_table.set_fontsize(font_size)
        for k, cell in mpl_table._cells.items():
            cell.set_edgecolor(edge_color)
            if k[0] == 0 or k[1] < header_columns:
                cell.set_text_props(weight='bold', color='w')
                cell.set_facecolor(header_color)
            else:
                cell.set_facecolor(row_colors[k[0]%len(row_colors) ])

    elif visualisation_library=='plotly':
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        align='left'),
            cells=dict(values=df.transpose().values.tolist(),
                       align='left'))])
        fig.show()