import glob

gox_files = '/Volumes/public/public_downloads/mtgox-data/trades/*_mtgox_japan.csv'

cc = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
"""Country codes."""

trades_by_date = dict()

for f in glob.glob(gox_files):
    with open(f, 'r') as fh:
        read_data = fh.readlines()
    for line1, line2 in zip(read_data[1::2], read_data[2::2]):
        values1 = line1.split(',')
        values2 = line2.split(',')

        # ignore same country
        try:
            country1 = values1[17]
        except IndexError:
            continue
        try:
            country2 = values2[17]
        except IndexError:
            continue

        if country1 == country2:
            continue

        if country1 not in cc:
            country1 = 'XX'
        if country2 not in cc:
            country2 = 'XX'

        year, month = values1[1][1:].split('-')[:2]

        # separate by year, month
        if year not in trades_by_date:
            trades_by_date[year] = dict()
        if month not in trades_by_date[year]:
            trades_by_date[year][month] = dict()

        # add countries
        if country1 not in trades_by_date[year][month]:
            trades_by_date[year][month][country1] = 0
        if country2 not in trades_by_date[year][month]:
            trades_by_date[year][month][country2] = 0

        type1 = values1[6]
        bitcoins = float(values1[8])

        # reduntant?
        if type1 == 'sell':
            bitcoins = -bitcoins

        trades_by_date[year][month][country1] += bitcoins
        trades_by_date[year][month][country2] -= bitcoins

years = trades_by_date.keys()
years.sort()
for year in years:
    months = trades_by_date[year].keys()
    months.sort()
    for month in months:
        countries = trades_by_date[year][month].keys()
        countries.sort()
        for country in countries:
            # print year, month, country, trades_by_date[year][month][country]
            print "%s\t%s\t%s\t%s" % (year, month, country, trades_by_date[year][month][country])
