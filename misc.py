
def addToDict(sample_dict, key, list_of_values):
    if key not in sample_dict.keys():
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def main():
    pass

if __name__ == '__main__':
    pass