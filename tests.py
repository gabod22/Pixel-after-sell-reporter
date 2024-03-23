import pandas as pd
from helpers import get_last_index, split_client_info
from tabulate import tabulate
from os import path
import sys

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))

delailed_filepath = path.join(dirname, "notasdeventadetalladas.xlsx")
simplied_filepath = path.join(dirname, "notasdeventasimplificada.xlsx")
simplied_invoice_path = path.join(dirname, "Facturacion.xlsx")


def get_clients_list():
    clients_df = pd.read_excel(path.join(dirname, "Clientes.xlsx"))
    clients_df = clients_df[["Nombre del cliente", "Teléfono"]]
    clients_df.drop_duplicates(subset=["Nombre del cliente"], inplace=True)

    return clients_df


clients = get_clients_list()

tables_to_merge = [{"data": clients, "on": "Nombre del cliente", "how": "left"}]

sell_notes_columns = [
    "Folio",
    "Sucursal",
    "Nombre del cliente",
    "Fecha registro",
    "Estado",
    "Subtotal",
    "Descuento",
    "Impuestos",
    "Importe del total",
    "Ejecutivo",
]
sell_notes_columns_view = [
    "Folio",
    "Sucursal",
    "Nombre del cliente",
    "Fecha registro",
    "Estado",
    "Subtotal",
    "Descuento",
    "Impuestos",
    "Importe del total",
    "Ejecutivo",
    "Teléfono",
]
items_cols = [
    "SKU",
    "Descripcion",
    "Cantidad",
    "Precio unitario",
    "Impuestos",
    "Porcentaje de descuento",
    "Subtotal",
    "Importe",
]


def df_to_list_str(df, headers: list):
    lista = []
    sell_notes_list = list(df[headers].to_dict("list").values())
    print(sell_notes_list)
    
        
    sell_notes = [
        f"{folio} - {name} - {phone}".replace("\n", "").replace("\r", "").strip()
        for folio, name, phone in zip(
            sell_notes_list[0],
            sell_notes_list[1],
            sell_notes_list[2],
        )
    ]
    return sell_notes


def process_kor_table(detailed_filepath, header, items_header, tables_to_merge):
    id_items = {}
    try:
        detailed_table = pd.read_excel(detailed_filepath)
    except Exception as e:
        raise "No se pudo abrir el documento:" + e

    detailed_table.drop(detailed_table.index[0:7], inplace=True)
    detailed_table = detailed_table.reset_index(drop=True)
    detailed_table = detailed_table.set_axis(header, axis=1)
    simplified_table = detailed_table.dropna(subset=["Folio"], inplace=False)
    last_index = get_last_index(detailed_table)

    table_indexs = simplified_table.index.append(pd.Index([last_index]))

    for table in tables_to_merge:
        simplified_table = simplified_table.merge(
            table["data"], on=table["on"], how=table["how"]
        ).set_axis(simplified_table.index)

    for inx in range(len(table_indexs) - 1):
        items_df = pd.DataFrame(
            detailed_table.iloc[
                table_indexs[inx] + 2 : table_indexs[inx + 1] - 1,
                [1, 2, 3, 4, 5, 6, 7, 8],
            ]
        )
        # print(items_df)
        items_df.columns = items_header
        sell_notes_list = list(
            items_df[["SKU", "Descripcion"]].to_dict("list").values()
        )
        items = [
            f"{sku} - {description}".replace("\n", "").replace("\r", "").strip()
            for sku, description in zip(
                sell_notes_list[0],
                sell_notes_list[1],
            )
        ]
        # print(sell_notes_list)
        id = simplified_table.iloc[inx, 0]

        id_items[id] = items
    return id_items, simplified_table


id_items, simplified_table = process_kor_table(
    delailed_filepath, sell_notes_columns, items_cols, tables_to_merge
)
print(tabulate(simplified_table, headers=sell_notes_columns_view))
print(
    df_to_list_str(
        simplified_table,
        [
            "Folio",
            "Nombre del cliente",
            "Teléfono",
        ],
    )
)
