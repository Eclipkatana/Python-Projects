import socket
import pickle
import threading
from PySide6 import QtWidgets


class ServerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Server")
        self.setGeometry(200, 200, 200, 100)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.connection_status_label = QtWidgets.QLabel("Disconnected", self)
        layout.addWidget(self.connection_status_label)

        self.connected_clients = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 12345

        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.update_connection_status()

        self.accept_clients_thread = threading.Thread(target=self.accept_clients)
        self.accept_clients_thread.start()

    def update_connection_status(self):
        if self.connected_clients:
            self.connection_status_label.setText("Connected")
            self.connection_status_label.setStyleSheet("color: green")
        else:
            self.connection_status_label.setText("Disconnected")
            self.connection_status_label.setStyleSheet("color: red")

    def accept_clients(self):
        while self.server_socket._closed:
            client_socket, addr = self.server_socket.accept()
            self.connected_clients.append(client_socket)
            self.update_connection_status()
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_socket,)
            )
            client_thread.start()

    def handle_client(self, client_socket):
        print("Connection from", client_socket.getpeername())
        self.connected_clients.append(client_socket)
        self.update_connection_status()

        # Receive data (task) from the client
        task_data = client_socket.recv(1024)
        task = pickle.loads(task_data)

        # Process the task
        result = task * 2

        # Send the result back to the client
        client_socket.send(pickle.dumps(result))

        # Close the connection
        client_socket.close()
        
        # Remove the client socket from the list
        self.connected_clients.remove(client_socket)
        self.update_connection_status()


app = QtWidgets.QApplication([])
server_window = ServerApp()
server_window.show()
app.exec()
