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