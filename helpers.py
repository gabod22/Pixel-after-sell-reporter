import pandas as pd

def split_client_info(str):
    if str != None or str != "":
        print(str)
        client_arr = str.split(" - ")
        client_id = client_arr[0]
        client_name = client_arr[1]
        client_phone = client_arr[2]
        return client_id, client_name, client_phone

def array_to_string(arr):
    string = ""
    for i, item in enumerate(arr):
        if i > 0:
            string += "," + item
        else:
            string += item
    return string


def get_last_index(dataframe: pd.DataFrame):
    """Return the last index of a Pandas Dataframe

    Args:
        dataframe (pd.DataFrame): Is the dataframe to get the last index
    """
    return dataframe[len(dataframe) - 1 :].index[0]



def replace_nan(string):
    if type(string) == float:
        print(string, type(string))
        return ""
    return f"({string})"


