# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, closing_prices, volumes = np.loadtxt(
    '../../data/bhp.csv', delimiter=',',
    usecols=(1, 6, 7), unpack=True,
    dtype='M8[D], f8, f8', converters={1: dmy2ymd})
diff_closing_prices = np.diff(closing_prices)
#sign_closing_prices = np.sign(diff_closing_prices)
sign_closing_prices = np.piecewise(
    diff_closing_prices, [
        diff_closing_prices < 0,
        diff_closing_prices == 0,
        diff_closing_prices > 0], [-1, 0, 1])
obvs = volumes[1:] * sign_closing_prices
mp.figure('On-Balance Volume', facecolor='lightgray')
mp.title('On-Balance Volume', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('OBV', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(
    byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
dates = dates[1:].astype(md.datetime.datetime)
mp.bar(dates, obvs, 1.0, color='dodgerblue',
       edgecolor='white', label='OBV')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
