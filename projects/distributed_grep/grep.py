from pyspark import SparkContext
import sys

# Initialize Spark context
sc = SparkContext(appName="GrepLog")

# Input log file and keyword to grep
log_file = sys.argv[1]  # e.g., data/SSH/SSH.log
keyword = sys.argv[2]   # e.g., "Invalid user"

# Read the log file
lines = sc.textFile(log_file)

# Filter lines that contain the keyword
filtered = lines.filter(lambda line: keyword in line)

# Collect and print result
for line in filtered.collect():
    print(line)

sc.stop()
