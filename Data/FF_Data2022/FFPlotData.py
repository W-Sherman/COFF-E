import matplotlib.pyplot as plt 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
from  plotly.subplots import make_subplots
from plotly.subplots import make_subplots
import pandas as pd
import seaborn as sns
import seaborn.objects as so


data = pd.read_csv('/Users/will/Desktop/EDUCATION/SSDL/2_Research/TopOpt/FF_Data2022/FF_MasterData_Subset_V1.2.csv')

useSats = data.loc[data[['# sats','Type']].notnull().all(axis=1)]
names = useSats['System']
nums = useSats['# sats']
lognums = np.log(nums)
field = useSats['Field']
archType = useSats['Type']
ForC = useSats['Sub-Class']

"""
plt.scatter(x=archType,
            y=field,
            c = ForC,
            alpha = 0.5
            )
plt.show()
"""
#print(type(field),type(nums))
#fig = make_subplots(rows=2, cols=2, column_widths=[0.7,0.3], row_heights=[0.7,0.3])
"""
fig.add_trace(go.Bar(
             x = nums,
             y = archType,
             orientation='h',
             hover_name = ), row=1, col=1)
"""
figMAIN = make_subplots(rows=2,cols=2)

fig = px.bar(useSats,x='# sats',
                y='Type',
                color='Sub-Class',
                labels={'# sats':'Number of Satellites (log scale)', 'Type':''},
                log_x=True,
                hover_name=names)


fig1 = px.scatter(useSats,
                    x='Field',
                    y='Type',
                    labels = {'Type':'Architecture Type', 'Field':''},
                    color='Sub-Class',
                    size = lognums,
                    opacity = 0.55,
                    title= 'Multi-Vehicle Mission Architectur Map')


fig2 = px.bar(useSats,x='Field',
                y=nums,
                color='Sub-Class',
                labels={'Field':'Mission Type', '# sats':'Number of Satellites (log scale)'},
                log_y = True,
                hover_name=names)

#figMAIN.append_trace(fig1,row=1,col=1)

fig.show()
fig1.show()
fig2.show()

#sns.displot(data = useSats, x='# sats', col='Sub-Class', log_scale=True)

"""
plt.subplot(2,2,1)
sns.scatterplot(data=useSats,
           x='Field',
            y='Type',
            hue='Sub-Class',
            alpha = 0.5
            )

plt.subplot(2,2,3)
plt.bar(data=useSats,
        x=field,
        height=nums,
        )

plt.show()"""

"""fig = px.bar(x=nums,
                y=field,
                color=ForC,
                title= 'Multi-Vehicle Mission Function Distribution',
                log_x=True,
                hover_name=names)

fig.show()"""

#fig = go.scatter(useSats,x='Field',y='Type',color='Sub-Class')
#fig.update_traces(marker=)
#fig.show()

