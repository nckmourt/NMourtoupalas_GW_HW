# Dependencies
import csv

# Files to Load
file_to_load = "../Resources/budget_data.csv"
file_to_output = "../Resources/budget_analysis.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

entries = {} # date -> amount
revenue_changes = []
totals = {}
total_num_months = 0
net_profit = 0
inc_month = ""
dec_month = ""
ovr_min = 0
ovr_max = 0
rev_avg = 0

# Read Files
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    prev_change = 8089807
    min = 9999999999999999999999 # this variable will hold the value of the greatest Decrease
    decrease_month = ""
    max = -9999999999999999999999
    increase_month = ""
    # Loop through all the rows of data we collect

    # total Months included
    # net total amount of profit / loss
    # average of the changes in profit / loss
    # greatest increase
    # greatest decrease
    for row in reader:

        # Calculate the totals
        entries[row[0]] = int(row[1])

        # add to total number of Months
        total_num_months += 1
        net_profit += int(row[1])

        # calculate rev changes
        rev_change = None
        if prev_change is not None:
            rev_change = int(row[1]) - prev_revenue

        if rev_change is not None and prev_change is not None and rev_change < min:
            min = rev_change
            decrease_month = row[0]

        if rev_change is not None and prev_change is not None and rev_change > max:
            max = rev_change
            increase_month = row[0]

        if rev_change is not None:
            prev_change = rev_change
        else:
            prev_change = int(row[1])

    # calculate the Revenue average
    revenue_avg = net_profit/total_num_months
    rev_avg = revenue_avg

    inc_month = increase_month
    dec_month = decrease_month
    ovr_max = max
    ovr_min = min

    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_num_months))
    print("Total Revenue: " + "$" + str(net_profit))
    print("Average Change: " + "$" + str(revenue_avg))
    print("Greatest Increase: " + str(increase_month) + " ($" +  str(max) + ")")
    print("Greatest Decrease: " + str(decrease_month) + " ($" +  str(min) + ")")

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_num_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(net_profit))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(rev_avg))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(inc_month) + " ($" + str(ovr_max) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(dec_month) + " ($" + str(ovr_min) + ")")