
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
df['date'] = df['date'].astype('str')
labels = list(df['date'])
sizes = list(df['confirm'])
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
df1 = df.head()
labels = list(df1['date'])
sizes = list(df1['dead'])
c = (
    Pie(opts.InitOpts(renderer='svg'))
    .add("", [list(z) for z in zip(labels, sizes)])
    .set_global_opts(title_opts=opts.TitleOpts(title="死亡人数"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}个"))
)
make_snapshot(snapshot, c.render('2.html'), "2.svg")
c.render_notebook()

