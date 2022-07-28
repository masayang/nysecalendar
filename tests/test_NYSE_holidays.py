from nysecalendar.nysecalendar import NYSE_holidays
import datetime

'''
For the actual NYSE Holidays, please refer following resources:
- http://www.market-holidays.com/
- https://www.nasdaq.com/articles/stock-market-news-for-october-29-2012-market-news-2012-10-29
- https://www.nasdaq.com/articles/stock-market-news-for-october-30-2012-market-news-2012-10-30
- https://www.cnn.com/2018/12/01/business/markets-closed-george-h-w-bush/index.html
- https://economictimes.indiatimes.com/news/international/us/its-juneteenth-is-the-stock-market-operating-today-in-the-u-s-/articleshow/92342880.cms
'''


def test_NYSE_holidays_1900():
    holidays = list(NYSE_holidays(datetime.date(
        1990, 1, 1), datetime.date(1990, 12, 31)))
    assert holidays == [
        datetime.datetime(1990, 1, 1, 0, 0),
        datetime.datetime(1990, 1, 15, 0, 0),
        datetime.datetime(1990, 2, 19, 0, 0),
        datetime.datetime(1990, 4, 13, 0, 0),
        datetime.datetime(1990, 5, 28, 0, 0),
        datetime.datetime(1990, 7, 4, 0, 0),
        datetime.datetime(1990, 9, 3, 0, 0),
        datetime.datetime(1990, 11, 22, 0, 0),
        datetime.datetime(1990, 12, 25, 0, 0)
    ]


def test_NYSE_holidays_1991():
    holidays = list(NYSE_holidays(datetime.date(
        1991, 1, 1), datetime.date(1991, 12, 31)))
    assert holidays == [
        datetime.datetime(1991, 1, 1, 0, 0),
        datetime.datetime(1991, 1, 21, 0, 0),
        datetime.datetime(1991, 2, 18, 0, 0),
        datetime.datetime(1991, 3, 29, 0, 0),
        datetime.datetime(1991, 5, 27, 0, 0),
        datetime.datetime(1991, 7, 4, 0, 0),
        datetime.datetime(1991, 9, 2, 0, 0),
        datetime.datetime(1991, 11, 28, 0, 0),
        datetime.datetime(1991, 12, 25, 0, 0)
    ]


def test_NYSE_holidays_1992():
    holidays = list(NYSE_holidays(datetime.date(
        1992, 1, 1), datetime.date(1992, 12, 31)))
    assert holidays == [
        datetime.datetime(1992, 1, 1, 0, 0),
        datetime.datetime(1992, 1, 20, 0, 0),
        datetime.datetime(1992, 2, 17, 0, 0),
        datetime.datetime(1992, 4, 17, 0, 0),
        datetime.datetime(1992, 5, 25, 0, 0),
        datetime.datetime(1992, 7, 3, 0, 0),
        datetime.datetime(1992, 9, 7, 0, 0),
        datetime.datetime(1992, 11, 26, 0, 0),
        datetime.datetime(1992, 12, 25, 0, 0)
    ]


def test_NYSE_holidays_1993():
    holidays = list(NYSE_holidays(datetime.date(
        1993, 1, 1), datetime.date(1993, 12, 31)))
    assert holidays == [
        datetime.datetime(1993, 1, 1, 0, 0),
        datetime.datetime(1993, 1, 18, 0, 0),
        datetime.datetime(1993, 2, 15, 0, 0),
        datetime.datetime(1993, 4, 9, 0, 0),
        datetime.datetime(1993, 5, 31, 0, 0),
        datetime.datetime(1993, 7, 5, 0, 0),
        datetime.datetime(1993, 9, 6, 0, 0),
        datetime.datetime(1993, 11, 25, 0, 0),
        datetime.datetime(1993, 12, 24, 0, 0),
    ]


def test_NYSE_holidays_1994():
    holidays = list(NYSE_holidays(datetime.date(
        1994, 1, 1), datetime.date(1994, 12, 31)))
    assert holidays == [
            datetime.datetime(1994, 1, 17, 0, 0),
            datetime.datetime(1994, 2, 21, 0, 0),
            datetime.datetime(1994, 4, 1, 0, 0),
            datetime.datetime(1994, 5, 30, 0, 0),
            datetime.datetime(1994, 7, 4, 0, 0),
            datetime.datetime(1994, 9, 5, 0, 0),
            datetime.datetime(1994, 11, 24, 0, 0),
            datetime.datetime(1994, 12, 26, 0, 0),
    ]


def test_NYSE_holidays_1995():
    holidays = list(NYSE_holidays(datetime.date(
        1995, 1, 1), datetime.date(1995, 12, 31)))
    assert holidays == [
            datetime.datetime(1995, 1, 2, 0, 0),
            datetime.datetime(1995, 1, 16, 0, 0),
            datetime.datetime(1995, 2, 20, 0, 0),
            datetime.datetime(1995, 4, 14, 0, 0),
            datetime.datetime(1995, 5, 29, 0, 0),
            datetime.datetime(1995, 7, 4, 0, 0),
            datetime.datetime(1995, 9, 4, 0, 0),
            datetime.datetime(1995, 11, 23, 0, 0),
            datetime.datetime(1995, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_1996():
    holidays = list(NYSE_holidays(datetime.date(
        1996, 1, 1), datetime.date(1996, 12, 31)))
    assert holidays == [
            datetime.datetime(1996, 1, 1, 0, 0),
            datetime.datetime(1996, 1, 15, 0, 0),
            datetime.datetime(1996, 2, 19, 0, 0),
            datetime.datetime(1996, 4, 5, 0, 0),
            datetime.datetime(1996, 5, 27, 0, 0),
            datetime.datetime(1996, 7, 4, 0, 0),
            datetime.datetime(1996, 9, 2, 0, 0),
            datetime.datetime(1996, 11, 28, 0, 0),
            datetime.datetime(1996, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_1997():
    holidays = list(NYSE_holidays(datetime.date(
        1997, 1, 1), datetime.date(1997, 12, 31)))
    assert holidays == [
            datetime.datetime(1997, 1, 1, 0, 0),
            datetime.datetime(1997, 1, 20, 0, 0),
            datetime.datetime(1997, 2, 17, 0, 0),
            datetime.datetime(1997, 3, 28, 0, 0),
            datetime.datetime(1997, 5, 26, 0, 0),
            datetime.datetime(1997, 7, 4, 0, 0),
            datetime.datetime(1997, 9, 1, 0, 0),
            datetime.datetime(1997, 11, 27, 0, 0),
            datetime.datetime(1997, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_1998():
    holidays = list(NYSE_holidays(datetime.date(
        1998, 1, 1), datetime.date(1998, 12, 31)))
    assert holidays == [
            datetime.datetime(1998, 1, 1, 0, 0),
            datetime.datetime(1998, 1, 19, 0, 0),
            datetime.datetime(1998, 2, 16, 0, 0),
            datetime.datetime(1998, 4, 10, 0, 0),
            datetime.datetime(1998, 5, 25, 0, 0),
            datetime.datetime(1998, 7, 3, 0, 0),
            datetime.datetime(1998, 9, 7, 0, 0),
            datetime.datetime(1998, 11, 26, 0, 0),
            datetime.datetime(1998, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_1999():
    holidays = list(NYSE_holidays(datetime.date(
        1999, 1, 1), datetime.date(1999, 12, 31)))
    assert holidays == [
            datetime.datetime(1999, 1, 1, 0, 0),
            datetime.datetime(1999, 1, 18, 0, 0),
            datetime.datetime(1999, 2, 15, 0, 0),
            datetime.datetime(1999, 4, 2, 0, 0),
            datetime.datetime(1999, 5, 31, 0, 0),
            datetime.datetime(1999, 7, 5, 0, 0),
            datetime.datetime(1999, 9, 6, 0, 0),
            datetime.datetime(1999, 11, 25, 0, 0),
            datetime.datetime(1999, 12, 24, 0, 0),
    ]


def test_NYSE_holidays_2000():
    holidays = list(NYSE_holidays(datetime.date(
        2000, 1, 1), datetime.date(2000, 12, 31)))
    assert holidays == [
        datetime.datetime(2000, 1, 17, 0, 0),
        datetime.datetime(2000, 2, 21, 0, 0),
        datetime.datetime(2000, 4, 21, 0, 0),
        datetime.datetime(2000, 5, 29, 0, 0),
        datetime.datetime(2000, 7, 4, 0, 0),
        datetime.datetime(2000, 9, 4, 0, 0),
        datetime.datetime(2000, 11, 23, 0, 0),
        datetime.datetime(2000, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2001():
    holidays = list(NYSE_holidays(datetime.date(
        2001, 1, 1), datetime.date(2001, 12, 31)))
    assert holidays == [
        datetime.datetime(2001, 1, 1, 0, 0),
        datetime.datetime(2001, 1, 15, 0, 0),
        datetime.datetime(2001, 2, 19, 0, 0),
        datetime.datetime(2001, 4, 13, 0, 0),
        datetime.datetime(2001, 5, 28, 0, 0),
        datetime.datetime(2001, 7, 4, 0, 0),
        datetime.datetime(2001, 9, 3, 0, 0),
        datetime.datetime(2001, 11, 22, 0, 0),
        datetime.datetime(2001, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2002():
    holidays = list(NYSE_holidays(datetime.date(
        2002, 1, 1), datetime.date(2002, 12, 31)))
    assert holidays == [
        datetime.datetime(2002, 1, 1, 0, 0),
        datetime.datetime(2002, 1, 21, 0, 0),
        datetime.datetime(2002, 2, 18, 0, 0),
        datetime.datetime(2002, 3, 29, 0, 0),
        datetime.datetime(2002, 5, 27, 0, 0),
        datetime.datetime(2002, 7, 4, 0, 0),
        datetime.datetime(2002, 9, 2, 0, 0),
        datetime.datetime(2002, 11, 28, 0, 0),
        datetime.datetime(2002, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2003():
    holidays = list(NYSE_holidays(datetime.date(
        2003, 1, 1), datetime.date(2003, 12, 31)))
    assert holidays == [
        datetime.datetime(2003, 1, 1, 0, 0),
        datetime.datetime(2003, 1, 20, 0, 0),
        datetime.datetime(2003, 2, 17, 0, 0),
        datetime.datetime(2003, 4, 18, 0, 0),
        datetime.datetime(2003, 5, 26, 0, 0),
        datetime.datetime(2003, 7, 4, 0, 0),
        datetime.datetime(2003, 9, 1, 0, 0),
        datetime.datetime(2003, 11, 27, 0, 0),
        datetime.datetime(2003, 12, 25, 0, 0)
    ]


def test_NYSE_holidays_2004():
    holidays = list(NYSE_holidays(datetime.date(
        2004, 1, 1), datetime.date(2004, 12, 31)))
    assert holidays == [
            datetime.datetime(2004, 1, 1, 0, 0),
            datetime.datetime(2004, 1, 19, 0, 0),
            datetime.datetime(2004, 2, 16, 0, 0),
            datetime.datetime(2004, 4, 9, 0, 0),
            datetime.datetime(2004, 5, 31, 0, 0),
            datetime.datetime(2004, 7, 5, 0, 0),
            datetime.datetime(2004, 9, 6, 0, 0),
            datetime.datetime(2004, 11, 25, 0, 0),
            datetime.datetime(2004, 12, 24, 0, 0),
    ]


def test_NYSE_holidays_2005():
    holidays = list(NYSE_holidays(datetime.date(
        2005, 1, 1), datetime.date(2005, 12, 31)))
    assert holidays == [
            datetime.datetime(2005, 1, 17, 0, 0),
            datetime.datetime(2005, 2, 21, 0, 0),
            datetime.datetime(2005, 3, 25, 0, 0),
            datetime.datetime(2005, 5, 30, 0, 0),
            datetime.datetime(2005, 7, 4, 0, 0),
            datetime.datetime(2005, 9, 5, 0, 0),
            datetime.datetime(2005, 11, 24, 0, 0),
            datetime.datetime(2005, 12, 26, 0, 0),
    ]


def test_NYSE_holidays_2006():
    holidays = list(NYSE_holidays(datetime.date(
        2006, 1, 1), datetime.date(2006, 12, 31)))
    assert holidays == [
            datetime.datetime(2006, 1, 2, 0, 0),
            datetime.datetime(2006, 1, 16, 0, 0),
            datetime.datetime(2006, 2, 20, 0, 0),
            datetime.datetime(2006, 4, 14, 0, 0),
            datetime.datetime(2006, 5, 29, 0, 0),
            datetime.datetime(2006, 7, 4, 0, 0),
            datetime.datetime(2006, 9, 4, 0, 0),
            datetime.datetime(2006, 11, 23, 0, 0),
            datetime.datetime(2006, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2007():
    holidays = list(NYSE_holidays(datetime.date(
        2007, 1, 1), datetime.date(2007, 12, 31)))
    assert holidays == [
            datetime.datetime(2007, 1, 1, 0, 0),
            datetime.datetime(2007, 1, 15, 0, 0),
            datetime.datetime(2007, 2, 19, 0, 0),
            datetime.datetime(2007, 4, 6, 0, 0),
            datetime.datetime(2007, 5, 28, 0, 0),
            datetime.datetime(2007, 7, 4, 0, 0),
            datetime.datetime(2007, 9, 3, 0, 0),
            datetime.datetime(2007, 11, 22, 0, 0),
            datetime.datetime(2007, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2008():
    holidays = list(NYSE_holidays(datetime.date(
        2008, 1, 1), datetime.date(2008, 12, 31)))
    assert holidays == [
            datetime.datetime(2008, 1, 1, 0, 0),
            datetime.datetime(2008, 1, 21, 0, 0),
            datetime.datetime(2008, 2, 18, 0, 0),
            datetime.datetime(2008, 3, 21, 0, 0),
            datetime.datetime(2008, 5, 26, 0, 0),
            datetime.datetime(2008, 7, 4, 0, 0),
            datetime.datetime(2008, 9, 1, 0, 0),
            datetime.datetime(2008, 11, 27, 0, 0),
            datetime.datetime(2008, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2009():
    holidays = list(NYSE_holidays(datetime.date(
        2009, 1, 1), datetime.date(2009, 12, 31)))
    assert holidays == [
            datetime.datetime(2009, 1, 1, 0, 0),
            datetime.datetime(2009, 1, 19, 0, 0),
            datetime.datetime(2009, 2, 16, 0, 0),
            datetime.datetime(2009, 4, 10, 0, 0),
            datetime.datetime(2009, 5, 25, 0, 0),
            datetime.datetime(2009, 7, 3, 0, 0),
            datetime.datetime(2009, 9, 7, 0, 0),
            datetime.datetime(2009, 11, 26, 0, 0),
            datetime.datetime(2009, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2010():
    holidays = list(NYSE_holidays(datetime.date(
        2010, 1, 1), datetime.date(2010, 12, 31)))
    assert holidays == [
            datetime.datetime(2010, 1, 1, 0, 0),
            datetime.datetime(2010, 1, 18, 0, 0),
            datetime.datetime(2010, 2, 15, 0, 0),
            datetime.datetime(2010, 4, 2, 0, 0),
            datetime.datetime(2010, 5, 31, 0, 0),
            datetime.datetime(2010, 7, 5, 0, 0),
            datetime.datetime(2010, 9, 6, 0, 0),
            datetime.datetime(2010, 11, 25, 0, 0),
            datetime.datetime(2010, 12, 24, 0, 0),
    ]


def test_NYSE_holidays_2011():
    holidays = list(NYSE_holidays(datetime.date(
        2011, 1, 1), datetime.date(2011, 12, 31)))
    assert holidays == [
            datetime.datetime(2011, 1, 17, 0, 0),
            datetime.datetime(2011, 2, 21, 0, 0),
            datetime.datetime(2011, 4, 22, 0, 0),
            datetime.datetime(2011, 5, 30, 0, 0),
            datetime.datetime(2011, 7, 4, 0, 0),
            datetime.datetime(2011, 9, 5, 0, 0),
            datetime.datetime(2011, 11, 24, 0, 0),
            datetime.datetime(2011, 12, 26, 0, 0),
    ]


def test_NYSE_holidays_2012():
    holidays = list(NYSE_holidays(datetime.date(
        2012, 1, 1), datetime.date(2012, 12, 31)))
    assert holidays == [
            datetime.datetime(2012, 1, 2, 0, 0),
            datetime.datetime(2012, 1, 16, 0, 0),
            datetime.datetime(2012, 2, 20, 0, 0),
            datetime.datetime(2012, 4, 6, 0, 0),
            datetime.datetime(2012, 5, 28, 0, 0),
            datetime.datetime(2012, 7, 4, 0, 0),
            datetime.datetime(2012, 9, 3, 0, 0),
            datetime.datetime(2012, 10, 29, 0, 0),
            datetime.datetime(2012, 10, 30, 0, 0),
            datetime.datetime(2012, 11, 22, 0, 0),
            datetime.datetime(2012, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2013():
    holidays = list(NYSE_holidays(datetime.date(
        2013, 1, 1), datetime.date(2013, 12, 31)))
    assert holidays == [
            datetime.datetime(2013, 1, 1, 0, 0),
            datetime.datetime(2013, 1, 21, 0, 0),
            datetime.datetime(2013, 2, 18, 0, 0),
            datetime.datetime(2013, 3, 29, 0, 0),
            datetime.datetime(2013, 5, 27, 0, 0),
            datetime.datetime(2013, 7, 4, 0, 0),
            datetime.datetime(2013, 9, 2, 0, 0),
            datetime.datetime(2013, 11, 28, 0, 0),
            datetime.datetime(2013, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2014():
    holidays = list(NYSE_holidays(datetime.date(
        2014, 1, 1), datetime.date(2014, 12, 31)))
    assert holidays == [
            datetime.datetime(2014, 1, 1, 0, 0),
            datetime.datetime(2014, 1, 20, 0, 0),
            datetime.datetime(2014, 2, 17, 0, 0),
            datetime.datetime(2014, 4, 18, 0, 0),
            datetime.datetime(2014, 5, 26, 0, 0),
            datetime.datetime(2014, 7, 4, 0, 0),
            datetime.datetime(2014, 9, 1, 0, 0),
            datetime.datetime(2014, 11, 27, 0, 0),
            datetime.datetime(2014, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2015():
    holidays = list(NYSE_holidays(datetime.date(
        2015, 1, 1), datetime.date(2015, 12, 31)))
    assert holidays == [
            datetime.datetime(2015, 1, 1, 0, 0),
            datetime.datetime(2015, 1, 19, 0, 0),
            datetime.datetime(2015, 2, 16, 0, 0),
            datetime.datetime(2015, 4, 3, 0, 0),
            datetime.datetime(2015, 5, 25, 0, 0),
            datetime.datetime(2015, 7, 3, 0, 0),
            datetime.datetime(2015, 9, 7, 0, 0),
            datetime.datetime(2015, 11, 26, 0, 0),
            datetime.datetime(2015, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2016():
    holidays = list(NYSE_holidays(datetime.date(
        2016, 1, 1), datetime.date(2016, 12, 31)))
    assert holidays == [
            datetime.datetime(2016, 1, 1, 0, 0),
            datetime.datetime(2016, 1, 18, 0, 0),
            datetime.datetime(2016, 2, 15, 0, 0),
            datetime.datetime(2016, 3, 25, 0, 0),
            datetime.datetime(2016, 5, 30, 0, 0),
            datetime.datetime(2016, 7, 4, 0, 0),
            datetime.datetime(2016, 9, 5, 0, 0),
            datetime.datetime(2016, 11, 24, 0, 0),
            datetime.datetime(2016, 12, 26, 0, 0),
    ]


def test_NYSE_holidays_2017():
    holidays = list(NYSE_holidays(datetime.date(
        2017, 1, 1), datetime.date(2017, 12, 31)))
    assert holidays == [
            datetime.datetime(2017, 1, 2, 0, 0),
            datetime.datetime(2017, 1, 16, 0, 0),
            datetime.datetime(2017, 2, 20, 0, 0),
            datetime.datetime(2017, 4, 14, 0, 0),
            datetime.datetime(2017, 5, 29, 0, 0),
            datetime.datetime(2017, 7, 4, 0, 0),
            datetime.datetime(2017, 9, 4, 0, 0),
            datetime.datetime(2017, 11, 23, 0, 0),
            datetime.datetime(2017, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2018():
    holidays = list(NYSE_holidays(datetime.date(
        2018, 1, 1), datetime.date(2018, 12, 31)))
    assert holidays == [
            datetime.datetime(2018, 1, 1, 0, 0),
            datetime.datetime(2018, 1, 15, 0, 0),
            datetime.datetime(2018, 2, 19, 0, 0),
            datetime.datetime(2018, 3, 30, 0, 0),
            datetime.datetime(2018, 5, 28, 0, 0),
            datetime.datetime(2018, 7, 4, 0, 0),
            datetime.datetime(2018, 9, 3, 0, 0),
            datetime.datetime(2018, 11, 22, 0, 0),
            datetime.datetime(2018, 12, 5, 0, 0),
            datetime.datetime(2018, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2019():
    holidays = list(NYSE_holidays(datetime.date(
        2019, 1, 1), datetime.date(2019, 12, 31)))
    assert holidays == [
            datetime.datetime(2019, 1, 1, 0, 0),
            datetime.datetime(2019, 1, 21, 0, 0),
            datetime.datetime(2019, 2, 18, 0, 0),
            datetime.datetime(2019, 4, 19, 0, 0),
            datetime.datetime(2019, 5, 27, 0, 0),
            datetime.datetime(2019, 7, 4, 0, 0),
            datetime.datetime(2019, 9, 2, 0, 0),
            datetime.datetime(2019, 11, 28, 0, 0),
            datetime.datetime(2019, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2020():
    holidays = list(NYSE_holidays(datetime.date(
        2020, 1, 1), datetime.date(2020, 12, 31)))
    assert holidays == [
            datetime.datetime(2020, 1, 1, 0, 0),
            datetime.datetime(2020, 1, 20, 0, 0),
            datetime.datetime(2020, 2, 17, 0, 0),
            datetime.datetime(2020, 4, 10, 0, 0),
            datetime.datetime(2020, 5, 25, 0, 0),
            datetime.datetime(2020, 7, 3, 0, 0),
            datetime.datetime(2020, 9, 7, 0, 0),
            datetime.datetime(2020, 11, 26, 0, 0),
            datetime.datetime(2020, 12, 25, 0, 0),
    ]


def test_NYSE_holidays_2021():
    holidays = list(NYSE_holidays(datetime.date(
        2021, 1, 1), datetime.date(2021, 12, 31)))
    assert holidays == [
            datetime.datetime(2021, 1, 1, 0, 0),
            datetime.datetime(2021, 1, 18, 0, 0),
            datetime.datetime(2021, 2, 15, 0, 0),
            datetime.datetime(2021, 4, 2, 0, 0),
            datetime.datetime(2021, 5, 31, 0, 0),
            datetime.datetime(2021, 7, 5, 0, 0),
            datetime.datetime(2021, 9, 6, 0, 0),
            datetime.datetime(2021, 11, 25, 0, 0),
            datetime.datetime(2021, 12, 24, 0, 0),
    ]


def test_NYSE_holidays_2022():
    holidays = list(NYSE_holidays(datetime.date(
        2022, 1, 1), datetime.date(2022, 12, 31)))
    assert holidays == [
            datetime.datetime(2022, 1, 17, 0, 0),
            datetime.datetime(2022, 2, 21, 0, 0),
            datetime.datetime(2022, 4, 15, 0, 0),
            datetime.datetime(2022, 5, 30, 0, 0),
            datetime.datetime(2022, 6, 20, 0, 0),
            datetime.datetime(2022, 7, 4, 0, 0),
            datetime.datetime(2022, 9, 5, 0, 0),
            datetime.datetime(2022, 11, 24, 0, 0),
            datetime.datetime(2022, 12, 26, 0, 0),
    ]


def test_NYSE_holidays_2023():
    holidays = list(NYSE_holidays(datetime.date(
        2023, 1, 1), datetime.date(2023, 12, 31)))
    assert holidays == [
            datetime.datetime(2023, 1, 2, 0, 0),
            datetime.datetime(2023, 1, 16, 0, 0),
            datetime.datetime(2023, 2, 20, 0, 0),
            datetime.datetime(2023, 4, 7, 0, 0),
            datetime.datetime(2023, 5, 29, 0, 0),
            datetime.datetime(2023, 6, 19, 0, 0),
            datetime.datetime(2023, 7, 4, 0, 0),
            datetime.datetime(2023, 9, 4, 0, 0),
            datetime.datetime(2023, 11, 23, 0, 0),
            datetime.datetime(2023, 12, 25, 0, 0),
    ]
