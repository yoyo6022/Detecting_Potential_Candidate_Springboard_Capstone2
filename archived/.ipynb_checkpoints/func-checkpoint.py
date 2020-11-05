import os
import pandas as pd
import numpy as np


def unique_var_pct(data):
    num = data.nunique()
    pct = round((data.nunique()/(data.shape[0]))*100,4)
    frame = pd.DataFrame(zip(num,pct), index = num.index,columns=['number','percentage'])
    return frame.sort_values('percentage',ascending=False)


def var_pct(data):
    num = data.value_counts(dropna=False)
    pct = round(data.value_counts(dropna=False)/(data.shape[0])*100,2)
    frame = pd.DataFrame(zip(num,pct),index=num.index,columns=['number','percentage'])
    return frame.sort_values('percentage',ascending=False)