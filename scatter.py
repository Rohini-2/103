import pandas as pd
import plotly.express as px
df=pd.read_csv("Copy+of+data+-+data.csv")
figure=px.scatter(df,x="date",y="cases")
figure.show()