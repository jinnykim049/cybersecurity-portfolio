import json

# Set file path
input_file = 'Sample_event4625.log' #original log file
output_file = 'Sample_event4625.json' #converted JSON file

# Read each line as JSON object and place it in an array
with open(input_file, 'r', encoding='utf-8') as infile:
    json_objects = [json.loads(line.strip()) for line in infile if line.strip()]

# Save as JSON file in array form
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(json_objects, outfile, indent=4, ensure_ascii=False)

print (f"Conversion completed: {output_file}") 

