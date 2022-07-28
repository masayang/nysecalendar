from nysecalendar.nysecalendar import NYSE_tradingdays
import datetime

def test_tradingdays_202207():
    trading_days = sorted(list(NYSE_tradingdays(datetime.date(2022, 7, 1), datetime.date(2022, 7, 31))))
    assert trading_days == [
            datetime.datetime(2022, 7, 1, 0, 0),
            datetime.datetime(2022, 7, 5, 0, 0),
            datetime.datetime(2022, 7, 6, 0, 0),
            datetime.datetime(2022, 7, 7, 0, 0),
            datetime.datetime(2022, 7, 8, 0, 0),
            datetime.datetime(2022, 7, 11, 0, 0),
            datetime.datetime(2022, 7, 12, 0, 0),
            datetime.datetime(2022, 7, 13, 0, 0),
            datetime.datetime(2022, 7, 14, 0, 0),
            datetime.datetime(2022, 7, 15, 0, 0),
            datetime.datetime(2022, 7, 18, 0, 0),
            datetime.datetime(2022, 7, 19, 0, 0),
            datetime.datetime(2022, 7, 20, 0, 0),
            datetime.datetime(2022, 7, 21, 0, 0),
            datetime.datetime(2022, 7, 22, 0, 0),
            datetime.datetime(2022, 7, 25, 0, 0),
            datetime.datetime(2022, 7, 26, 0, 0),
            datetime.datetime(2022, 7, 27, 0, 0),
            datetime.datetime(2022, 7, 28, 0, 0),
            datetime.datetime(2022, 7, 29, 0, 0),        
    ]

