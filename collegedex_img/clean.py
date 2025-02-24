def clean_and_deduplicate_emoji_ids(input_file, output_file):
    """Function to clean emoji IDs that start with '13' and save only unique IDs."""
    seen_ids = set()

    with open(input_file, 'r', encoding='latin-1') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Find all parts that start with "13"
            parts = line.split()
            for part in parts:
                if part.startswith('13') and part.isdigit():
                    # Add to set if not already seen
                    if part not in seen_ids:
                        outfile.write(part + '\n')
                        seen_ids.add(part)

if __name__ == "__main__":
    input_path = 'cleaned_emoji_ids.txt'
    output_path = 'emojids.txt'
    clean_and_deduplicate_emoji_ids(input_path, output_path)
    print(f"Cleaned and deduplicated emoji IDs have been written to {output_path}")