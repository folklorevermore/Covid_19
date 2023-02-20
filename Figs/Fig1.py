
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
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
c = (
    Bar(opts.InitOpts(renderer='svg'))
    .add_xaxis(labels)
    .add_yaxis("人数", sizes, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="新冠确诊人数"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                yaxis_opts=opts.AxisOpts(name="人数"),
        xaxis_opts=opts.AxisOpts(name="时间")
    )
    
)
make_snapshot(snapshot, c.render('1.html'), "1.svg")
c.render_notebook()

