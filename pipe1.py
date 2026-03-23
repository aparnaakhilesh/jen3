# pipe_lower.py

def to_lowercase(input_file, output_file):
    print(f"Reading {input_file}...")

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Input file not found.")
        return

    lower_text = text.lower()

    with open(output_file, 'w') as f:
        f.write(lower_text)

    print(f"Conversion complete. Results saved to {output_file}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python pipe_lower.py <input_file> <output_file>")
    else:
        to_lowercase(sys.argv[1], sys.argv[2])


