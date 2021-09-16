import plotly.express as px
import pandas as pd 
import statistics
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff 

df = pd.read_csv("savings_data_final.csv")
with open('savings_data_final.csv') as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)


totalentries = len(savings_data)
rich = 0
for data in savings_data: 
  if int(data[4]) == 1:
    rich += 1
  

fig = go.Figure(go.Bar(x=["rich","poor"], y=[rich,(totalentries-rich)]))
fig.show()
#fig = ff.create_distplot([df["quant_saved "].tolist()], ["Savings"], show_hist=False) 
#fig.show()