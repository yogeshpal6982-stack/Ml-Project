#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

import plotly.express as px

import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default="plotly_white"


# In[20]:


data = pd.read_csv("Superstore.csv",encoding='latin-1')


# In[21]:


data


# In[22]:


data.head()


# In[23]:


data.describe()


# In[24]:


data.info()


# # Converting Date Columns

# In[25]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])


# In[26]:


data.info()


# In[27]:


data['Order month'] = data['Order Date'].dt.month
data['Order year'] = data['Order Date'].dt.year
data['Order day of week'] = data['Order Date'].dt.dayofweek


# In[28]:


data.head()


# # Monthly Sales Analysis

# In[30]:


sales_by_month = data.groupby('Order month')['Sales'].sum().reset_index()
fig = px.line(sales_by_month,
              x = 'Order month',
              y = 'Sales',
              title = 'monthly Sales Analysis')
fig.show()


# In[32]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()

fig = px.pie(
    sales_by_category,
    values='Sales',
    names='Category',
    hole=0.5,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(
    textposition='inside',
    textinfo='percent+label'
)

fig.update_layout(
    title_text='Sales Analysis by Category',
    title_font=dict(size=24)
)

fig.show()


# # Sales Analysis by Sub Category

# In[33]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[34]:


sales_by_subcategory


# In[35]:


fig = px.bar(sales_by_subcategory,x='Sub-Category',y='Sales',title='Sales Analysis by subcategory')
fig.show()


# # Monthly Profit Analysis

# In[36]:


data.head()


# In[37]:


profit_by_month =data.groupby('Order month')['Profit'].sum().reset_index()


# In[38]:


profit_by_month


# In[39]:


fig = px.line(profit_by_month,x='Order month',y='Profit',title='Monthly analysis profit')
fig.show()


# # Profit by category

# In[40]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[41]:


profit_by_category


# In[43]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()

fig = px.pie(
    profit_by_category,
    values='Profit',
    names='Category',
    hole=0.5,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(
    textposition='inside',
    textinfo='percent+label'
)

fig.update_layout(
    title_text='profit Analysis by Category',
    title_font=dict(size=24)
)

fig.show()


# # Profit by Sub Categorey

# In[48]:


profit_by_subcategory=data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[46]:


profit_by_subcategory


# In[51]:


fig = px.bar(profit_by_subcategory,x='Sub-Category',y='Profit',title='Profit Analysis by Sub-Category')
fig.show()


# # Sales & Profit -Customer Segment

# In[52]:


data.head()


# In[56]:


import plotly.graph_objects as go
import plotly.express as px

sales_profit_by_segment = data.groupby('Segment').agg({
    'Sales': 'sum',
    'Profit': 'sum'
}).reset_index()

color_palette = px.colors.qualitative.Pastel

fig = go.Figure()

fig.add_trace(go.Bar(
    x=sales_profit_by_segment['Segment'],
    y=sales_profit_by_segment['Sales'],
    name='Sales',
    marker_color=color_palette[0]
))

fig.add_trace(go.Bar(
    x=sales_profit_by_segment['Segment'],
    y=sales_profit_by_segment['Profit'],
    name='Profit',
    marker_color=color_palette[1]
))

fig.update_layout(
    title='Sales and Profit Analysis by Customer Segment',
    xaxis_title='Customer Segment',
    yaxis_title='Amount',
    barmode='group'
)

fig.show()

