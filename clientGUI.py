import socket
import pickle
from PySide6 import QtWidgets

class ClientApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client")
        self.setGeometry(200, 200, 200, 150)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = "1"
        self.port = 12345

        self.connect_button = QtWidgets.QPushButton("Send Task", self)
        self.connect_button.clicked.connect(self.send_task)
        layout.addWidget(self.connect_button)

        self.result_label = QtWidgets.QLabel("Result: ", self)
        layout.addWidget(self.result_label)

        self.client_socket.connect((self.server_ip, self.port))

    def send_task(self):
        task = 10
        self.client_socket.send(pickle.dumps(task))
        result_data = self.client_socket.recv(1024)
        result = pickle.loads(result_data)
        self.result_label.setText("Result: " + str(result))

app = QtWidgets.QApplication([])
client_window = ClientApp()
client_window.show()
app.exec()
