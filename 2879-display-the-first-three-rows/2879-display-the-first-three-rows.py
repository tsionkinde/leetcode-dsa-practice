import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employees)
    df1=df.head(3)
    return df1
    