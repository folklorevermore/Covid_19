
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


import pyecharts.options as opts
from pyecharts.charts import Radar
v1 = [[8923, 64, 3151, 17581, 2666]]
c = (
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC",renderer='svg'))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="confirm", max_=10000),
            opts.RadarIndicatorItem(name="dead", max_=100),
            opts.RadarIndicatorItem(name="heal", max_=20000),
            opts.RadarIndicatorItem(name="infect", max_=20000),
            opts.RadarIndicatorItem(name="localinfectionadd", max_=10000),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    .add(
        series_name="4.24",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="雷达图"), legend_opts=opts.LegendOpts()
    )
)
make_snapshot(snapshot, c.render('4.html'), "4.svg")
c.render_notebook()

