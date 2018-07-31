import sys
import tushare as ts
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

res = ts.realtime_boxoffice(60, True)
res.to_csv('./temp_boxoffice_result')
