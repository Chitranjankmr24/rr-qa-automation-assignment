import json

data_path = None
dic_data = None
modify_data = dict()


# set the path of test data and update the dictionary
def set_data_path(file_path):
    global data_path
    data_path = file_path
    global dic_data
    dic_data = get_json_object(data_path)
    if type(modify_data) == dict and len(modify_data.items()):
        modify_main_dict_value_param()


# read json file
def get_json_object(file_path):
    with open(file_path, 'r') as f:
        distros_dict = json.load(f)
    return distros_dict


def modify_parameter(param):
    global modify_data
    modify_data = param


def modify_main_dict_value_param():
    for modify_key, modify_value in modify_data.items():
        key_found = search_dict_key(dic_data, modify_key)
        if key_found:
            dic_data[modify_key] = modify_value


def fetch_data(target_key, nested_dictionary):
    for key, dic_value in nested_dictionary.items():
        if type(dic_value) is dict and dic_value:
            if key == target_key:
                return dic_value
        if type(dic_value) is dict and dic_value:
            for x in dic_value:
                if x == target_key:
                    return dic_value[x]
        elif type(dic_value) is str and dic_value:
            for key_string, value_string in nested_dictionary.items():
                if key_string == target_key:
                    return value_string
            return None
    return dic_value


def get_data(target_key, nested_dictionary=None):
    global dic_data
    if dic_data is None and nested_dictionary is None:
        dic_data = get_json_object(data_path)
    if nested_dictionary:
        test_data = fetch_data(target_key, nested_dictionary)
        return test_data
    if dic_data:
        test_data = fetch_data(target_key, dic_data)

        return test_data


# Search a given key inside dictionary recursively
def search_dict_key(target_dict, search_key):
    for key, value in target_dict.items():
        if key == search_key and type(value) == dict:
            return target_dict[key]
        elif key == search_key:
            return True
        elif type(value) == dict:
            key_found = search_dict_key(target_dict[key], search_key)
            if key_found:
                return key_found
    return None
