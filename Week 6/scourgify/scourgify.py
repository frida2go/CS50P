import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        table = []
        with open(sys.argv[1],newline = "") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                table.append({"first": first, "last": last, "house": row ["house"]})

        with open(sys.argv[2], "w", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for i in table:
                writer.writerow(i)
        sys.exit()

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")