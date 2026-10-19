import pandas as pd

def solution(df): #we know it already contains 2 columns
    df = pd.DataFrame(df) #df is a dataframe
    group_avg =  df.groupby('group')['value'].transform('mean') #defining what group_avg is
    df['group_avg'] = group_avg #we are adding group_avg to the 2 column dataframe
    return df #I think it automatically preservers row order

df = pd.DataFrame({'group': ['a','a','b'],'value': [10, 20, 40]})
solution (df) #df is a dataframe with two columns, group and value that is already given, call the function
