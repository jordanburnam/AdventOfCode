import os
import logging 


logging.basicConfig(
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to console
    ]
)

# Created a class to encapsulate this problem
class ReactorReport:
    def __init__(self, line_number, numbers):
        self.line_number = line_number
        self.raw = numbers
        self.deltas = self._calculate_delta()

    def _calculate_delta(self):
        #Sanity check
        if len(self.raw) < 2:
            raise Exception(f"at line {self.line_number} row had less than 2 columns {self.raw}")
        
        #Calculate deltas
        deltas = []
        for i in range(len(self.raw) - 1):
            deltas.append(self.raw[i + 1] - self.raw[i])
       
        return deltas

    def check_safety(self):
        if not self.deltas:
            raise Exception(f"at line {self.line_number} there were no deltas so I died")

        # Check if all deltas are positive or all deltas are negative
        is_monotonic = all(d > 0 for d in self.deltas) or all(d < 0 for d in self.deltas)
        
        # Check if all deltas are within the range [-3, 3]
        is_within_delta_range = all(abs(d) <= 3 for d in self.deltas)
        
        return is_monotonic and is_within_delta_range



reactor_reports=[]

input_file_path='2024/2/input/data.ssv'
# input_file_path='2024/2/input/example.ssv'

logging.info(f"Reading file at '{input_file_path}'")

# Count the lines to check our work later
line_count=0

#opening file and reading line by line
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        line_count+=1
        line = line.strip()

        # Split line on space
        report = line.split()

        # if len(report) % 2 == 0:
        #     print(report)
        #     raise Exception(f"at line {line_count}: Expected columns in line to be even but got {len(report)} columns, line was '{line}'")

        # Convert to float and fail with details if not able to convert
        try:
            report = [float(value) for value in report]
        except Exception as e:
             raise Exception(f"Failed to convert values to float, {report[0]} and {report[1]}")

        reactor_report = ReactorReport(line_count, report)
        reactor_reports.append(reactor_report)

if len(reactor_reports) != line_count:
    raise Exception(f"File had {line_count} and only created {len(reactor_reports)} reports, expected the total to match")

logging.info(f"total_lines_in_file:{line_count}|reactor_report_count:{len(reactor_reports)}")

safe_reactors = []
for reactor_report in reactor_reports:
    logging.debug(f"Safe:{reactor_report.check_safety()}|Raw:{reactor_report.raw}")
    if reactor_report.check_safety():
        safe_reactors.append(reactor_report)

print(f"Total safe reactors are {len(safe_reactors)}")