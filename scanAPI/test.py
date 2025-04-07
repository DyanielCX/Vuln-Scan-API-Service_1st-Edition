import json

# JSONL file directory
jsonl_file = "C:/Users/dyani/Desktop/Intern/API_Practice/Osmedeus/example.com/vuln/nuclei/example.com-nuclei-json.txt"

# Read and parse JSONL
with open(jsonl_file, 'r') as f:
    # Load all entries into a list of dictionaries
    scan_results = [json.loads(line.strip()) for line in f]

print(f"Loaded {len(scan_results)} scan results")
print("First entry:", scan_results[0]['template'])