import numpy as np
import csv
import plotly.express as px

def getDataSource ():
    marks=[]
    days=[]
    with open ("marks.csv")as f:
        file=csv.DictReader(f)
        for row in file:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return{"x":marks,"y":days}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between marks in percentage and days preset",correlation[0,1])

def setup():
    datasource = getDataSource()
    findcorrelation(datasource)

setup()

with open ("marks.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()