#!/usr/bin/env python3
#

import datetime
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
axes = figure().add_subplot(111)

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from backend.models import Webpage, Pageview, Resource


OUTPUT_BASEDIR = sys.argv[1]  #/static/img/ directory

y = []
x = []
total_so_far = 0
start_t = end_t = datetime.datetime(2015, 4, 1)
while True:
    start_t = end_t
    end_t += datetime.timedelta(days=2)
    
    if end_t > datetime.datetime.now(): 
        print(end_t)
        break

    views = Pageview.query.filter(start_t <= Pageview.date).filter(Pageview.date < end_t).all()
    total_so_far += len(views)
    y.append(total_so_far / 1000000)
    x.append(start_t)
    
plt.plot(range(len(y)), y, 'r-')
plt.title("Total Pageview Observations Recorded")
plt.ylabel("Millions of pageviews")

xmin, xmax, ymin, ymax = plt.axis()
plt.axis([xmin, len(x), 0, ymax])

n_entries = len(x)
n_labels = len(axes.get_xticklabels()) - 2
time_labels = []
for i in range(n_entries):
    if i % (n_entries // n_labels) == 0:
        time_labels.insert(0, x[-1 - i].strftime('%m/%d'))
time_labels[0] = ""
axes.set_xticklabels(time_labels)

os.system("rm {0}/entries-over-time.png".format(OUTPUT_BASEDIR))
plt.savefig(OUTPUT_BASEDIR + "/entries-over-time.png")

