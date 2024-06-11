from typing import Any

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

def recursive(dict_: dict) -> None:
    for key, value in dict_.items(): 
        if type(value) is dict:
            print_dict(key, value)
            continue
            
        if type(value) is list:
            print(f'{key} : ' + '[')
            for item in value:
                if type(item) is dict:
                    print("{")
                    recursive(item)
                    print("}")
                    continue
                print(item)
            print(']')
            continue
        print('{} : {}'.format(key, value))
    


def print_dict(key, value) -> None:
    print(f'{key} : ' + "{")
    recursive(value)
    print('}')

recursive(dict_)