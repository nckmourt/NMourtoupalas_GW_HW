import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title=str(udemy_csv[1])

        # Add price
        price=int(udemy_csv[4])

        # Add number of subscribers
        subscribers=int(udemy_csv[5])

        # Add amount of reviews
        reviews=int(udemy_csv[6])

        # Determine percent of review left to 2 decimal places
        review_percent=((reviews/subscribers)*100)
        print(reviewpercent)

        # Get length of the course to just a number
        length = float(udemy_csv[10])

# Zip lists together
list_combined = zip(title, numPrice, numSubscribers, numReviews, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
for list_combined print (review_percent in [11])
