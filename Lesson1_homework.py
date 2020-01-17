#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[10]:


x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.cos(x))


# In[11]:


x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.cos(x*1.5))


# In[ ]:




