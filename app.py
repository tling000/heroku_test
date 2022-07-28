import datetime as dt
import pandas as pd

def test():
    print('hello world!!')
    print(dt.datetime.utcnow().strftime('%Y/%m/%d %H:%M'))
    print(pd.DataFrame(columns=['A', 'B', 'C'], index=[i for i in range(2)]))