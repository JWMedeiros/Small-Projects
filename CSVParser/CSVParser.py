import csv
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-v","--version",help="show program version",action="store_true")
parser.add_argument("-f","--file",help="export file to JSON format")

#Read arguments sent from cmd line
args=parser.parse_args()

if args.version:
	print("Program version 1.0")

elif args.file:
	ctr=0
	files = args.file.split(',')
	data = {"SCUnit": []}
	for string in files:
		with open (files[ctr]) as csv_file:
			csvReader = csv.reader(csv_file, delimiter=';')
			next(csvReader) #ignore first row (column titles) if needed
			for row in csvReader:
				data["SCUnit"].append({"Name":row[0],"Race":row[1],"Cost":row[2]})
			ctr+=1
	with open ("Starcraft.json","w") as csv_file:
		csv_file.write(json.dumps(data, indent=4))
