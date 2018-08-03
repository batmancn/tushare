# -*- coding:utf-8 -*-

import sys
import tushare as ts
import pandas as pd

# 获得大盘数据

reload(sys)
sys.setdefaultencoding('utf-8')

res = ts.get_index()
res.to_csv('./result_index')
