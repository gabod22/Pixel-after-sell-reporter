import pandas as pd
# from tabulate import tabulate 

def merge_dict(dict1, dict2):
    res = {**dict1, **dict2}
    return res

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

def df_to_list_str(df, headers: list):
    result = []
    sell_notes_list = list(df[headers].to_dict("list").values())
    for row in range(len(sell_notes_list[0])):
        text = ""
        for col in range(len(sell_notes_list)):
            text = text + str(sell_notes_list[col][row])
            if col != len(sell_notes_list) - 1:
                text = text + " - "
        text = text.replace("\n", "").replace("\r", "").strip()
        result.append(text)

    # sell_notes = [
    #     f"{folio} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
    #     for folio, name, phone in zip(
    #         sell_notes_list[0],
    #         sell_notes_list[1],
    #         sell_notes_list[2],
    #     )
    # ]
    return result

def process_kor_table(detailed_filepath, header, items_header, tables_to_merge):
    id_items = {}
    try:
        detailed_table = pd.read_excel(detailed_filepath)
    except Exception as e:
        raise "No se pudo abrir el documento:" + e

    detailed_table.drop(detailed_table.index[0:7], inplace=True)
    detailed_table = detailed_table.reset_index(drop=True)
    detailed_table = detailed_table.set_axis(header, axis=1)
    folio_column_index = detailed_table.columns.get_loc('Folio')
    
    
    simplified_table = detailed_table.dropna(subset=detailed_table.columns[0], inplace=False)
    if folio_column_index != 0:
        folio_column = simplified_table.pop('Folio')
        print("El folio está en la columna: ", folio_column_index)
        simplified_table.insert(0, folio_column.name, folio_column)
    # print(tabulate(detailed_table))
    last_index = get_last_index(detailed_table)

    table_indexs = simplified_table.index.append(pd.Index([last_index]))
    
    
    for table in tables_to_merge:
        simplified_table = simplified_table.merge(
            table["data"], on=table["on"], how=table["how"]
        ).set_axis(simplified_table.index)
    simplified_table_list = df_to_list_str(simplified_table, ["Folio","Nombre del cliente", "Teléfono"])
    
    for inx in range(len(table_indexs) - 1):
        items_df = pd.DataFrame(
            detailed_table.iloc[
                table_indexs[inx] + 2 : table_indexs[inx + 1] - 1,
                [1, 2, 3, 4, 5, 6, 7, 8],
            ]
        )
        
        # print(items_df)
        items_df.columns = items_header
        if items_df['SKU'].iloc[0] == "No hay registro":
            items = []
        else:
            items = df_to_list_str(items_df, ["SKU", "Descripcion"])
        # print(sell_notes_list)
        id = simplified_table.iloc[inx, 0]

        id_items[id] = items
    return id_items, simplified_table_list


def get_last_index(dataframe: pd.DataFrame):
    """Return the last index of a Pandas Dataframe

    Args:
        dataframe (pd.DataFrame): Is the dataframe to get the last index
    """
    return dataframe[len(dataframe) - 1 :].index[0]

def save_excel(df: pd.DataFrame, book_name: str, sheet_name: str):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(book_name + ".xlsx", engine="xlsxwriter")
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    # Add a format.
    text_format = workbook.add_format({"text_wrap": True})
    # Resize columns for clarity and add formatting to column C.
    worksheet.set_column(4, 4, 70, text_format)
    # Close the Pandas Excel writer and output the Excel file.
    writer.close()

def replace_nan(string):
    if type(string) == float:
        print(string, type(string))
        return ""
    return f"({string})"


