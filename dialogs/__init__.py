from PySide6.QtWidgets import QMessageBox

def showSuccessDialog(parent,message):
    msgBox = QMessageBox(parent=parent)
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle('Todo correcto')
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')

def showFailDialog(parent, message):
    msgBox = QMessageBox(parent=parent)
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(message)
    msgBox.setWindowTitle('Error')
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')
        
def show_yes_no_dialog(parent, title, text):
    msg_box = QMessageBox(parent=parent)
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setDefaultButton(QMessageBox.No)
    
    # Retorna True si el usuario selecciona "Sí", False si selecciona "No"
    return msg_box.exec() == QMessageBox.Yes