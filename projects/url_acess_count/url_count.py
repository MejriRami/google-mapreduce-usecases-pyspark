from pyspark import SparkContext
import re
import sys

sc = SparkContext(appName="URLCount")

log_file = sys.argv[1]  # e.g., data/SSH/SSH.log

# Regex to extract IPs
ip_regex = r'(\d{1,3}(?:\.\d{1,3}){3})'

def extract_ips(line):
    return re.findall(ip_regex, line)

lines = sc.textFile(log_file)

# Extract and count IPs
ip_counts = (lines.flatMap(extract_ips)
                  .map(lambda ip: (ip, 1))
                  .reduceByKey(lambda a, b: a + b))

# Print results
for ip, count in ip_counts.collect():
    print(f"{ip}\t{count}")

sc.stop()
