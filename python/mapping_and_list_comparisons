from collections import MutableMapping
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
        if isinstance(value, list):
            for item in value:
                delete_keys_from_dict(item, keys)
        if isinstance(value, MutableMapping):
            delete_keys_from_dict(value, keys)
