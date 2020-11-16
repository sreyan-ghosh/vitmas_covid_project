# vitmas_covid_project

Contains the SARIMAX Time Series Forecasting model that predicts the number of COVID cases that may happen in the next 7 days.

<b><i>train.py</i></b> needs to run once daily to create the latest model after the data is fetched from this [API][1]

<b><i>app.py</i></b> conatins the Flask file that will be published to Heroku or AWS after the frontend work is finished.

[1]: "https://api.covid19india.org/csv/latest/state_wise_daily.csv"
