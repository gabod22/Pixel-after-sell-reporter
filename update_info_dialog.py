from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QFileDialog,
    QLineEdit,
    QApplication,
    QCompleter,
    QDialog,
)
from PySide6.QtCore import QThreadPool, QThread, QTimer, QSize, Qt

from ui.update_data_dialog_ui import Ui_Dialog

import sys
import pandas as pd
from os import path

from helpers import get_last_index, split_client_info, process_kor_table, merge_dict
from dialogs import showSuccessDialog, showFailDialog

import pickle

# from gspread import *

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable))
elif __file__:
    dirname = path.join(path.dirname(__file__))

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
invoices_columns = [
    "Sucursal",
    "Folio",
    "Nombre del cliente",
    "Condición",
    "Fecha registro",
    "Estado",
    "Subtotal",
    "Descuento",
    "Impuestos",
    "Importe total",
    "Saldo"

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

class UpdateInfoDialog(QDialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dirname = path.dirname(__file__)
        self.exe_dirname = path.dirname(sys.executable)

        self.ui.BtnOpenClientFile.clicked.connect(
            lambda: self.select_file(self.ui.TxtClienFilePath)
        )
        self.ui.BtnOpenInvoiceFile.clicked.connect(
            lambda: self.select_file(self.ui.TxtInvoicesPath)
        )
        self.ui.BtnOpenSellnoteFile.clicked.connect(
            lambda: self.select_file(self.ui.TxtSellnotePath)
        )
        
        self.ui.BtnUpdateData.clicked.connect(self.update_info)

    def select_file(self, line_edit: QLineEdit):
        (fname, _) = QFileDialog.getOpenFileName(
            self, "Open file", self.exe_dirname, "Excel (*.xlsx *.xls)"
        )
        print(fname)
        line_edit.setText(fname)
    
    def get_clients_list(self):
        clients_df = pd.read_excel(self.ui.TxtClienFilePath.text())
        clients_df = clients_df[["Nombre del cliente", "Teléfono"]]
        clients_df.drop_duplicates(subset=["Nombre del cliente"], inplace=True)

        return clients_df
    
    def update_info(self):
        clients = self.get_clients_list()
        tables_to_merge = [{"data": clients, "on": "Nombre del cliente", "how": "left"}]
        
        self.ui.PlantextLog.appendPlainText("Procesando las notas de venta")
        sell_notes_items, sell_notes = process_kor_table(
            self.ui.TxtSellnotePath.text(), sell_notes_columns, items_cols, tables_to_merge
        )
        self.ui.PlantextLog.appendPlainText("Procesando las facturas")
        invoices_items, invoices = process_kor_table(
            self.ui.TxtInvoicesPath.text(), invoices_columns, items_cols, tables_to_merge
        )
        self.ui.PlantextLog.appendPlainText("Juntando la información")
        info_sells = sell_notes + invoices
        info_items = merge_dict(sell_notes_items, invoices_items)

        if path.isfile('sells.pkl') and path.isfile('sell_items.pkl'):
            with open('sells.pkl', 'rb') as file:
                sells = pickle.load(file)
                
            with open('sell_items.pkl', 'rb') as file:
                sell_items = pickle.load(file)
            print(sells)
            sells.append(info_sells)
            sells = list(set(sells))
        
            sell_items.update(info_items)
        
            with open('sells.pkl', 'wb') as file:
                pickle.dump(sells,file)
                
            with open('sell_items.pkl', 'wb') as file:
                pickle.dump(sell_items,file)
                
            print(sells)
            print(sell_items)
        else:
            with open('sells.pkl', 'wb') as file:  
                pickle.dump(info_sells,file)
                
            with open('sell_items.pkl', 'wb') as file:
                pickle.dump(info_items,file)
        showSuccessDialog(self,"Se actualizó la información correctamente")
        self.parent.load_info()
        self.close()
            
        # except Exception as e:
        #     showFailDialog(self,"Ocurrió un error, revise que haya seleccionado los archivos correctos o que los exportó correctamente")
        #     print(e)
        