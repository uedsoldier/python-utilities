import json

def json_to_dict(json_file, encoding='utf-8'):
    with open(json_file,'r', encoding=encoding) as file:
        return json.load(file)


def dict_to_json(dict,json_file, ensure_ascii=False):
    with open(json_file,'w') as file:
        json.dump(dict,file,ensure_ascii=ensure_ascii)
