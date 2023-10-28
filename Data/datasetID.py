import json
import uuid

def add_unique_id(json_data):
    for key in json_data:
        for item in json_data[key]:
            if 'id' not in item:
                item['id'] = str(uuid.uuid4())
        
        return json_data
    
def main():
    imput_file = 'Data/dataset.json'
    output_file = 'updated_dataset.json'

    with open(imput_file, 'r') as f:
        json_data = json.load(f)

    update_data = add_unique_id(json_data)
    
    with open(output_file, 'w') as f:
        json.dump(update_data, f, indent=4)

if __name__ == "__main__":
    main()