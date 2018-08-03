import sys
import tushare as ts
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

res = ts.get_today_all()
res.to_csv('./result_today_all')
