import csv

# Open the tab-delimited file and read its contents
with open("injurydat.txt", 'r') as infile, open("injurydat.csv", 'w', newline='') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    
    # Read each line from the tab-delimited file
    for line in infile:
        # Split each line into columns based on the tab delimiter
        row = line.strip().split('\t')
        # Write the row to the CSV file
        writer.writerow(row)
        
# Open the tab-delimited file and read its contents
with open("locdat2.txt", 'r') as infile, open("locdat2.csv", 'w', newline='') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    
    # Read each line from the tab-delimited file
    for line in infile:
        # Split each line into columns based on the tab delimiter
        row = line.strip().split('\t')
        # Write the row to the CSV file
        writer.writerow(row)
        
# Open the tab-delimited file and read its contents
with open("timedb2.txt", 'r') as infile, open("timedb2.csv", 'w', newline='') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    
    # Read each line from the tab-delimited file
    for line in infile:
        # Split each line into columns based on the tab delimiter
        row = line.strip().split('\t')
        # Write the row to the CSV file
        writer.writerow(row)