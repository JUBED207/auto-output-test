from datetime import datetime
import csv

# Create a simple CSV file with a timestamp
filename = "output.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Message", "Timestamp"])
    writer.writerow(["Hello from workflow", datetime.utcnow().isoformat()])

print(f"Created {filename}")
