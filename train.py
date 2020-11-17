from flask import Flask
import pandas as pd
import joblib
import json
import time
import datetime
from datetime import timedelta
import statsmodels.api as sm
import scipy.stats as stats


def train():
    train = pd.read_csv(
        'https://api.covid19india.org/csv/latest/state_wise_daily.csv')
    train.drop('Date_YMD', axis=1, inplace=True)
    train.set_index("Status", inplace=True)
    train.drop(['Recovered', 'Deceased'], inplace=True)
    train.reset_index(level=0, inplace=True)
    train.drop('Status', axis=1, inplace=True)
    train_df = train[['Date', 'TT', 'UN']]
    train_df.reset_index(drop=True, inplace=True)
    train_df.set_index('Date', inplace=True)
    train_df['TT'] = train_df['TT'].astype(float)
    sarimax_mod = sm.tsa.statespace.SARIMAX(
        train_df.TT, trend='n', order=(14, 1, 0)).fit()
    yesterday = datetime.date.today() - timedelta(days=1)
    start_index = '14-Mar-20'
    end_index = yesterday.strftime('%Y-%m-%d')
    train_df['forecast'] = sarimax_mod.predict(
        start=start_index, end=end_index, dynamic=False)
    today = datetime.date.today()
    future_predict = sarimax_mod.predict(
        start=str(today), end=str(today+timedelta(days=7)), dynamic=True)
    f_temp = pd.DataFrame()
    f_temp['date'] = future_predict.index.strftime("%d-%b-%y")
    f_temp['values'] = future_predict.values
    f_temp.loc[-1] = [train_df.index[-1], train_df['TT'][-1]]
    f_temp.index = f_temp.index+1
    f_temp = f_temp.sort_index()
    f_temp['date'] = pd.to_datetime(f_temp['date'], format="%d-%b-%y")
    f_temp['date'] = f_temp['date'].dt.strftime('%Y-%m-%d')
    f_temp.to_json('preds.json')
    return f_temp.to_json()


if __name__ == "__main__":
    train()
