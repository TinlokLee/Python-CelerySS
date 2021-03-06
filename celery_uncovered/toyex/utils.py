import os
import csv
import datetime


def make_csv(filename, lines):
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, 'wb') as csvfile:
        trending_csv = csv.writer(csvfile)
        for line in lines:
            trending_csv.writerow(line)
    return filename



def strf_date(mixed_date, ref_date=None):
    dt_str = None
    if ref_date is None:
        ref_date = datetime.date.today()
    if mixed_date in ('day', 'week', 'month'):
        delta = None
        if mixed_date is 'day':
            delta = datetime.timedelta(days=1)
        elif mixed_date is 'week':
            delta = datetime.timedelta(weeks=1)
        else:
            delta = datetime.timedelta(days=30)
        dt_str = (ref_date - delta).isoformat()

    elif type(ref_date) in (str, unicode):
        dt_str = ref_date

    elif type(ref_date) in (datetime.date, datetime.datetime):
        dt_str = ref_date.isoformat()
    return dt_str
