import pandas as pd
import numpy as np

def load_and_process(url):
    df = (
        pd
        .read_csv(url)
        .drop(columns=['Phase','Time Period','Subgroup','Group','Time Period Start Date','Time Period Start Date','Time Period End Date','Low CI','High CI','Quartile Range'])
        .dropna()
        .rename(columns={"Percentage":"Level"})
    )

    df.drop(df[df["Indicator"] != "Symptoms of Anxiety Disorder"].index, inplace=True)
    df.drop(df[df["State"] != "California"].index, inplace=True)
    
    return df.reset_index(drop=True)

