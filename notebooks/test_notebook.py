#!/usr/bin/env python
# coding: utf-8

# # Test Notebook

# In[4]:
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# In[17]:


n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, s=20)
st.pyplot()


# In[ ]:




