from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.uic import loadUi
import os
import sys


class MyTool(QMainWindow):
    def __init__(self):
        super(MyTool, self).__init__()

        # Sets UI file
        script_directory = os.path.realpath(__file__)
        script_directory = os.path.dirname(script_directory)
        ui_file = script_directory + '/tool.ui'
        widget = loadUi(ui_file)
        self.setCentralWidget(widget)

        self.setWindowTitle('My Tool')

        # Variables for widgets to be used later
        self.name = os.path.basename(script_directory)
        self.versions_file = script_directory + '/../tools_versions.txt'
        self.version_label = None
        self.purposeless_button = None

        self.set_widgets()
        self.set_callbacks()
        self.read_version()

    def set_widgets(self):
        self.version_label = self.findChild(QLabel, 'version_label')
        self.purposeless_button = self.findChild(
            QPushButton, 'purposeless_button')
    
    def set_callbacks(self):
        self.purposeless_button.clicked.connect(
            lambda: print('Why are you doing this? It\'s meaningless...'))
    
    def read_version(self):
        with open(self.versions_file, 'r') as file:
            for line in file:
                line, version = line.split('=')
                if line == self.name:
                    text = f'Version: {version}'
                    self.version_label.setText(text)
                    return
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyTool()
    window.show()
    sys.exit(app.exec_())