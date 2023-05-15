import os
import re
import json

sensitive_data = []

# Scan files for sensitive data
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.txt', '.md')):
            path = os.path.join(root, file)
            with open(path) as f:
                for line_num, line in enumerate(f):
                    if re.search('sensitive_data_regex', line):
                        sensitive_data.append({
                            'file_path': path,
                            'line_number': line_num,
                            'line_text': line.strip()
                        })

# Save results to file
with open('sensitive-data.json', 'w') as f:
    json.dump(sensitive_data, f)

