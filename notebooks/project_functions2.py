def load_and_process(url):
    df = (
        pd
        .read_csv(url)
        .drop(columns=['Phase','Time Period','Subgroup','Time Period Start Date','Time Period Start Date','Time Period End Date','Low  CI','High CI','Quartile Range'])
        .dropna()
        .rename(columns={"Value":"Percentage"})
    )

    df.drop(df[df["Indicator"] != "Symptoms of Depressive Disorder"].index, inplace=True)
    df.drop(df[df["Group"] != "By State"].index, inplace=True)
    df.drop(df[df["Time Period Label"] != "Sep 15 - Sep 27, 2021"].index, inplace=True)
    
    return df.reset_index(drop=True)


