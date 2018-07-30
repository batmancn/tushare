import sys
import tushare.stock.newsevent as fd
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

res = fd.get_latest_news(60, True)
res.to_csv('./temp_news_result')