import json

# Create function to verify integrity of json
def verify_json(json_file):
    data = json.load(json_file)
    id_dict = {}
    for dict in data:
        if dict["type"] in [0,1]:
            id_dict[dict["id"]]=dict["next"]
        elif dict["type"]==3:
            id_dict[dict["id"]]=-1
        else:
            id_dict[dict["id"]]=dict["next"][1]
            
    for key in id_dict.keys():
        if id_dict[key] not in id_dict:
            print(key,id_dict[key])


def main():
    # Open json file
    with open('plot.json','r',encoding='utf-8') as json_file:
        verify_json(json_file)

if __name__ == "__main__":
    main()