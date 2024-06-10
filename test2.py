dict_ = {
            "Key1" : "Value1",
            "Key2" : "Value2",
            "Key3" : "Value3",
            "Key4" : {"SubKey1" : "SubValue1", "SubKey2" : {"SubSubKey1" : "SubSubValue1"}},
            "Key5" : ["ListKey1", "ListKey2", "ListKey3"],
            "Key6" : {"SubKey1" : "SubValue1", "SubKey2" : {"SubSubKey1" : "SubSubValue2", "SubSubKey2" : ["ListItem1", "ListItem2"]}}
        }

def recursive(dict_: dict):
    for key, value in dict_.items(): 
        if type(value) is dict:
            print(key + ': {')
            recursive(value)
            print("}")
            continue
            
        if type(value) is list:
            print(key + ' [')
            for num, item in enumerate(value, 1):
                print(f'list item {num}: {item}')
            print(']')
            continue
        print('key: {}, value: {}'.format(key, value))
    


recursive(dict_)