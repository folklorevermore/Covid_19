
# coding: utf-8

# In[1]:


import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
import matplotlib.pyplot as plt
import numpy as np
import  warnings
from pyecharts.charts import Timeline, Line, Tree,Map
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
warnings.filterwarnings("ignore", module="matplotlib")    
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  


# In[ ]:


df = pd.read_csv('新冠.csv')
df.info()
df['date'] = df['date'].astype('str')


# In[ ]:


fig = plt.figure(figsize=(13,3), dpi=100)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
x= list(df['date'])
y= list(df['importedCase'])
ax.plot(x, y)
ax.legend()
plt.xlabel('时间')
plt.ylabel('时间数')
plt.xticks(rotation=45)
ax.set_title('热点事件数')
plt.savefig('8.svg')
plt.show()

