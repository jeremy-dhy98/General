def create_dictionary(keys, values):
    # Using zip to combine the two lists and then creating a dictionary
    result_dict = dict(zip(keys, values))
    return result_dict

# Example usage:
if __name__ == "__main__":
    keys_list = ["name", "age", "city"]
    values_list = ["John", 25, "New York"]

    my_dict = create_dictionary(keys_list, values_list)

    print(my_dict)
