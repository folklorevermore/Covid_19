
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
from pyecharts.charts import Scatter
importedCase = list(df['localConfirmadd'])
confirm = list(df['confirm'])
data = [
]
for i in range(len(confirm)):
    data.append([importedCase[i],confirm[i]])
data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]

c = (
    Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px",renderer='svg'))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            name="本土确诊人数",
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            name="确诊人数",
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
)
make_snapshot(snapshot, c.render('6.html'), "6.svg")
c.render_notebook()

