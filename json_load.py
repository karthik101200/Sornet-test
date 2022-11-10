import json 

def reflection():
    print(1)
def rotation():
    print(2)
def scaling():
    print(3)
def mirroring():
    print(4)
with open("augmentations.json") as jsonfile:
    # `json.loads` parses a string in json format
    parent_dict = json.load(jsonfile)
    # print(list(parent_dict['report'].values()))
    auggie = []
    for c,report in enumerate(parent_dict['report'].values()):
        if report == 'True':
            auggie.append(list(parent_dict['report'].keys())[c])
        
    globals()[auggie[0]]()

        # Will print the dictionary keys
        # '/report1', '/report2'
        # print(report['rotation'])
# def func1(): return 1
# def func2(): return 2
# def func3(): return 3

# funcs = [func1, func2, func3]
# funcs_dict = {f.__name__: f for f in funcs}

# funcname = "func2"

# print(funcs_dict[funcname]())