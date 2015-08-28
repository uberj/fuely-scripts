import csv
import sys
from datetime import datetime

with open(sys.argv[1]) as fd:
	reader = csv.DictReader(fd)
	total_cost = 0
	for row in reader:
		date_added = row[' date_added']
		price = float(row[' price'])
		gallons = float(row[' gallons'])
		total_cost += price * gallons
		date = datetime.strptime(date_added, '%Y-%m-%d %H:%M:%S')
		min_date = min(min_date or date, date)
		max_date = max(max_date or date, date)

	diff = (max_date - min_date)
	total_days = abs(diff.days)
	cost_per_day = total_cost/total_days
	print "Total cost: $" + str(total_cost)
	print "Average cost per day: $" + str(cost_per_day)
	print "Average cost per month (31 days): $" + str(cost_per_day * 31)
