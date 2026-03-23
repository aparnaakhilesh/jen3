import sys
import pandas as pd
import os

def process(input_file, output_file):
    print(f"Reading {input_file}...")
    if not os.path.exists(input_file):
        print("Input file not found.")
        return

    df = pd.read_csv(input_file)

    if 'value' not in df.columns:
        print("CSV must contain a 'value' column.")
        return

    # Simple transformation: square the values
    df['squared'] = df['value'] ** 2

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)

    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pipe1.py <input_file> <output_file>")
    else:
        process(sys.argv[1], sys.argv[2])

