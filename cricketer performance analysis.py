#!/usr/bin/env python
# coding: utf-8

# # Virat Kohli Performance Analysis

# This project is about classifying whether or not patient has he

# In[3]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[4]:


df=pd.read_csv('Virat_Kohli_ODI.csv')


# In[5]:


print(df)


# In[6]:


data=pd.read_csv('Virat_Kohli_ODI.csv')


# In[7]:


print(data)


# In[8]:


data["Runs"] = data["Runs"].str.replace("*", "")
data["Runs"]


# In[9]:


data["Runs"] = data["Runs"].astype(int)
data.info()


# In[10]:


total_runs = data["Runs"].sum()
total_runs


# normally in ODI's 35-37 is considered a good average 

# In[11]:


data['Runs'].mean()


# Now let us look at the trend of runs scored by him

# In[12]:


matches=data.index
figure=px.line(data,x=matches,y='Runs',title='Runs scored by virat kohli between 18-Aug-08 - 22-Jan-17',template='plotly_dark')
figure.show()


# In some matches kohli has scored more than hundred or near to century so based on his batting positions analysing his performance
# ![virat%20kohli.jpeg](attachment:virat%20kohli.jpeg)
# 

# In[13]:


data['Pos']=data['Pos'].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
                               1.0: "Batting At 1", 7.0:"Batting At 7", 5.0:"Batting At 5", 
                               6.0: "batting At 6"})
Pos=data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ["gold","lightgreen", "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# 68.9% of all innings played by virat kohli he batted in third position.
# now lets calculate total runs scored by virat kohli in different positions

# In[14]:


label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# 72.4% of his runs are scored at batting position 3. From this we can 3rd position is best for him

# Now let us look at the centuries scored by virat kohli in second and first innings

# In[15]:


centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()


# centuries are scored while batting in the second innings. 

# Dismissals virat kohli faced

# In[16]:


dismissal = data["Dismissal"].value_counts()
label = dismissal.index
counts = dismissal.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Dismissals of Virat Kohli')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# Kohli wicket is mostly because of the fielder or the keeper.
# Let us understand against which team kohli scored most of his runs

# In[17]:


figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
            title="Most Runs Against Teams")
figure.show()


#  Virat Kohli likes batting against Sri Lanka, Australia, New Zealand, West Indies, and England.But he scored most of his runs while batting against Sri Lanka

# Now let’s have a look at against which team Virat Kohli scored most of his centuries

# In[18]:


figure=px.bar(centuries,x=centuries['Opposition'],y=centuries['Runs'],color = centuries["Runs"],
                title="Most Centuries Against Teams")
figure.show()


# Most of the centuries were scored against Australia.

# Taking strike rate into consideration we need to create a new dataset of all the matches played by virat kohli where his strike rate is more than 120.

# In[19]:


data["SR"] = data["SR"].str.replace("-", " ")
print(data)


# In[24]:


figure = px.bar(data, x = data["Inns"], 
                y = data["SR"], 
                color = data["SR"],
            title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
figure.show()


# In[27]:


figure = px.scatter(data_frame = data, x="Runs",
                    y="4s",
                    title="Relationship Between Runs Scored and Fours")
figure.show()


# In[28]:


figure = px.scatter(data_frame = data, x="Runs",
                    y="6s",  
                    title= "Relationship Between Runs Scored and Sixes")
figure.show()


# In[ ]:





# In[ ]:




