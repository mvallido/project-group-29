# Michael's Project Function
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




# Raj's Project Function
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


load_and_process("../data/raw/Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days.csv")