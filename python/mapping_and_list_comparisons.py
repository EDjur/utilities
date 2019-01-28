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
        {'SolutionDetail': {
            'SolutionDetails': {
                'OperationImageId': 'Shoulder_Variant01_V',
                'Cooling': {
                    'CoolingStyle': 'DRY',
                    'Coolant': 'DRY'
                    },
                'Features': [],
                'CuttingToolAssemblyId': 1784475,
                'CuttingToolItems': [
                    {
                        'OrderCodeAnsi': '',
                        'Warnings': []
                    }
                ],
                'ToolFamily': 'CoroMill Plura',
                'Params': [
                    {
                        'ShortName': 'DC',
                        'PreferredName': 'cutting diameter',
                        'ToolingName': 'DC',
                        'DescriptorName': 'DC',  # This is the dict we want
                        'DefaultValue': None,
                    }
                ]
            }
            'CuttingData': {
                '$type': 'TouchTime.Web.Models.Solution.Rm0001CuttingData, TouchTime.Web',
                'BendingTabData': {
                    'BendingParameters': [
                            {
                                '$type': 'TouchTime.Web.Models.Parameter.MultivalueDisplayableParameter, TouchTime.Web',
                                'Messages': [None],
                                'IsServerRelevant': False,
                                'RoundingPrecision': 0,
                                'DescriptorName': 'BENDL_X',  # This is the dict we want
                                'Value': [0.198],
                                'ValueTitle': 'System.Object[]',
                            }
                        ]
                    }
                }
            }
        }
    :param wanted:
        wanted = ['VC', 'FZ', 'AE', 'AP', 'NOPAE', 'NOPAP', 'QQ', 'PPC', 'BENDL_X', 'DC']
    :return: does not return, instead appends list in place
        list = [
                {
                '$type': 'TouchTime.Web.Models.Parameter.MultivalueDisplayableParameter, TouchTime.Web',
                'Messages': [None],
                'IsServerRelevant': False,
                'RoundingPrecision': 0,
                'DescriptorName': 'BENDL_X',
                'Value': [0.198],
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
