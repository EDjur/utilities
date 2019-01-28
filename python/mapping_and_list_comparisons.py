from collections.abc import MutableMapping, MutableSequence
from contextlib import suppress
        
def delete_keys_from_dict(dictionary, keys):
    """
    Recursively deletes keys contained in {keys} from {dictionary}

    EXAMPLE USAGE:
    :param dictionary: 
        dictionary = {
            "responses": [
                {
                    "foo": "abcdef",
                    "test_result": "test_1",
                    "success": true
                },
                {
                    "foo": "abcdef",
                    "bar": "12345",
                    "test_result": "test_2",
                    "success": true
                }
            ]
        }
    :param keys: 
        keys = ["foo", "bar", "baz"]
    :return: does not return, instead modifies dictionary in place
        dictionary = {
            "responses": [
                {
                    "test_result": "test_1",
                    "success": true
                },
                {
                    "test_result": "test_2",
                    "success": true
                }
            ]
        }
    """
    for key in keys:
        with suppress(KeyError):
            del dictionary[key]
    for value in dictionary.values():
        if isinstance(value, MutableSequence):
            for item in value:
                if isinstance(item, MutableMapping):
                        delete_keys_from_dict(item, keys)
        if isinstance(value, MutableMapping):
            delete_keys_from_dict(value, keys)

        
def find_and_save_dicts(dictionary, wanted, key):
    """
    Recursively finds and saves dictionaries in a list (defined before function call)
    whose {key} has the value of {wanted}

    EXAMPLE USAGE:
    :param dictionary:
        {'Detail': {
            'Details': {
                'Styles': {
                    'Style': 'X',
                    },
                'Features': [],
                'Items': [
                    {
                        'Ansi': '',
                        'Warnings': []
                    }
                ],
                'Params': [
                    {
                        'ShortName': 'UNWANTED_VALUE_1',
                        'TName': 'UNWANTED_VALUE_1',
                        'DescriptorName': 'UNWANTED_VALUE_1',
                        'DefaultValue': None,
                    }
                ]
            }
            'Data': {
                'TabData': {
                    'Parameters': [
                            {
                                'Messages': [None],
                                'RoundingPrecision': 0,
                                'DescriptorName': 'WANTED_VALUE_1',  # This is the dict we want
                                'ValueTitle': 'System.Object[]',
                            }
                        ]
                    }
                }
            }
        }
    :param wanted:
        wanted = ['WANTED_VALUE_1']
    :return: does not return, instead appends list in place
        list = [
                {
                'Messages': [None],
                'RoundingPrecision': 0,
                'DescriptorName': 'WANTED_VALUE_1',
                'ValueTitle': 'System.Object[]',
                }
            ]
    """
    with suppress(KeyError):
        for item in wanted:
            if dictionary[key] == item:
                resulting_list.append(dictionary)
    for value in dictionary.values():
        if isinstance(value, MutableSequence):
            for item in value:
                if isinstance(item, MutableMapping):
                    find_and_save_dicts(item, wanted, key)
        if isinstance(value, MutableMapping):
            find_and_save_dicts(value, wanted, key)
