# usage: python parse-volume.py > ../data/gox_volume.tsv

import datetime
import json

"""
Bars in the background represent volume 
(that is, how many coins were traded during that time) 
enumerated in [mBTC]. The Value for this is shown on the left axis.
"""

volume = []

f = '../data/mtgox-volume_parsed.csv'

with open(f, 'r') as fh:
    data = fh.read()

data = json.loads(data[9:-1])

same_date = []
prev_month = 10

for epoch, v in data[22:-9]:
    # 1396456917.98835 # epoch from file
    # 1333152000.000   # python time.time()
    d = datetime.datetime.utcfromtimestamp(epoch / 1000)
    # if prev_month == d.month:
    #     same_date.append(v);
    # else:
    #     if len(same_date) > 0:
    #         avg = sum(same_date) / float(len(same_date))
    #         volume.append(avg)
    #     same_date = [v]
    # prev_month = d.month
    print "%s\t%s" % (d.month, v)

# avg = sum(same_date) / float(len(same_date))
# volume.append(avg);

# the output is how many BITCOINS (not mBTC) were traded per month
# MM = 12 # number of months
# for i, v in enumerate(volume):
#     print "%s\t%s" % ((i + MM + 10) % MM + 1, str(int(round(v))))
