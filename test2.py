from typing import Any
import mypy

dict_: dict[str, Any] = \
{
    "Key1" : "Value1",
    "Key2" : "Value2",
    "Key3" : "Value3",
    "Key4" : 
    {
        "SubKey1" : "SubValue1", 
        "SubKey2" : 
        {
            "SubSubKey1" : "SubSubValue1"
        }
    },
    "Key5" : 
    [
        "ListKey1", 
        "ListKey2", 
        "ListKey3"
    ],
    "Key6" : 
    {
        "SubKey1" : "SubValue1", 
        "SubKey2" : 
        {
            "SubSubKey1" : "SubSubValue2", 
            "SubSubKey2" : 
            [
                "ListItem1", 
                "ListItem2"
            ]
        }
    },
    "Key7" : 
    [
        "ListItem1", 
        {
            "ListDictKey1" : "ListDictValue1", 
            "ListDictKey2" : "ListDictValue2", 
            "ListDictKey3" : 
            [
                "ListDictListValue1", 
                "ListDictListValue2", 
                {
                    "ListDictListDictKey1" : "ListDictListDictValue1"
                }
            ]
        }
    ]
}

value_type: type = None

## recursive function that will print the contents of the dictionary
def recursive(dict_: dict) -> None:

    ## iterate through each key/value pair in the dictionary
    for key, value in dict_.items():
        value_type = type(value)

        ## if the value is a dictionary
        ## recurse through the function
        if value_type is dict:
            print_dict(key, value)
            
        ## if the value is a list, print the list. Recurse
        ## if the list contains a dictionary
        elif value_type is list:
            print(f'{key} : ' + '[')

            for item in value:
                if type(item) is dict:
                    print("{")
                    recursive(item)
                    print("}")
                
                else:
                    print(item)

            print(']')

        ## if the value is neither list not dictionary, simply
        ## print the key/value pair
        else:
            print('{} : {}'.format(key, value))
    


def print_dict(key, value) -> None:
    print(f'{key} : ' + "{")
    recursive(value)
    print('}')


recursive(dict_)