import json
from hashlib import sha256

# Load the JSON data from input.json
input_file = 'input.json'
output_file = 'cleaned_input.json'

def load_data(file_path):
    """Load data from JSON file with utf-8 encoding."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(file_path, data):
    """Save data to JSON file with utf-8 encoding."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def hash_first_50_chars(about_me, context):
    """Create a hash from the first 50 characters of about_me and context."""
    combined = (about_me[:50] + context[:50]).encode('utf-8')
    return sha256(combined).hexdigest()

def remove_duplicates(entries):
    """Remove duplicates based on the first 50 characters of about_me and context."""
    seen_hashes = set()
    unique_entries = []
    duplicate_count = 0
    
    for entry in entries:
        entry_hash = hash_first_50_chars(entry['about_me'], entry['context'])
        
        if entry_hash not in seen_hashes:
            seen_hashes.add(entry_hash)
            unique_entries.append(entry)
        else:
            duplicate_count += 1
    
    return unique_entries, duplicate_count

def main():
    # Load data from the file
    entries = load_data(input_file)
    
    print(f"Initial number of entries: {len(entries)}")
    
    # Remove duplicates
    cleaned_entries, duplicates_removed = remove_duplicates(entries)
    
    print(f"Number of duplicates removed: {duplicates_removed}")
    print(f"Number of unique entries remaining: {len(cleaned_entries)}")
    
    # Save the cleaned data to a new file
    save_data(output_file, cleaned_entries)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    main()
