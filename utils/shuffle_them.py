import json
import random

# Input and output file paths
input_file = 'cleaned_input.json'
output_file = 'shuffled_input.json'

def load_data(file_path):
    """Load data from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(file_path, data):
    """Save data to JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def shuffle_data(entries):
    """Shuffle the list of entries."""
    random.shuffle(entries)
    return entries

def main():
    # Load data from the file
    entries = load_data(input_file)
    
    print(f"Number of entries before shuffling: {len(entries)}")
    
    # Shuffle the data
    shuffled_entries = shuffle_data(entries)
    
    print("Data shuffled successfully.")
    
    # Save the shuffled data to a new file
    save_data(output_file, shuffled_entries)
    print(f"Shuffled data saved to {output_file}")

if __name__ == "__main__":
    main()
