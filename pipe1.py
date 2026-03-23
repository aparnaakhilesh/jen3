import sys
import csv
import os

def process(input_file, output_file):
    print(f"Reading {input_file}...")
    if not os.path.exists(input_file):
        print("Input file not found.")
        return

    results = []
    with open(input_file, newline='') as f:
        reader = csv.DictReader(f)
        if 'value' not in reader.fieldnames:
            print("CSV must contain a 'value' column.")
            return
        for row in reader:
            val = int(row['value'])
            results.append({'value': val, 'squared': val ** 2})

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['value', 'squared'])
        writer.writeheader()
        writer.writerows(results)

    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pipe1.py <input_file> <output_file>")
    else:
        process(sys.argv[1], sys.argv[2])

