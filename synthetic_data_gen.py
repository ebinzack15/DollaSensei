import json
from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI()

# Function to generate response using GPT-4o model
def generate_response(about_me, context):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert financial advisor with deep knowledge in wealth management, investment strategies, estate planning, and tax optimization. Provide curated and personalized advice tailored to individual client needs."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"# ABOUT ME \\n{about_me} \\n# CONTEXT \\n{context} \\nPlease provide concrete advice in less than 100 tokens, and justify your answer based on the news provided in the context."
                    }
                ]
            }
        ],
        temperature=0,
        max_tokens=1039,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
    return response.choices[0].message.content

# Load input data from JSON file
input_file = 'shuffled_input.json'
output_file = '161_output.json'

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Check if the output file exists
if not os.path.exists(output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump([], file)

# Process each entry and append responses progressively
for i, entry in enumerate(data, start=1):
    about_me = entry['about_me']
    context = entry['context']

    print(f"Processing entry {i}...")  # Log progress

    response = generate_response(about_me, context)
    entry['response'] = response

    print(f"Generated response for entry {i}: {response[:100]}...")  # Log the first 100 characters of the response

    # Append the updated entry to the output file
    with open(output_file, 'r+', encoding='utf-8') as file:
        # Load current content
        current_data = json.load(file)

        # Append new entry
        current_data.append(entry)

        # Move to the beginning and rewrite the file
        file.seek(0)
        json.dump(current_data, file, indent=4)

    print(f"Entry {i} has been written to {output_file}")

print("All responses have been generated and saved to output.json")
