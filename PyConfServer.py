import socket
class response:
    def gen(self, type_r, action, action_to, myuname):
        response = type_r+":"+action+":"+action_to
        return response
    def get_response(self):
        sock = socket.socket()
        sock.bind(("", 5081))
        sock.listen(10)
        conn,addr = sock.accept()
        return conn.recv(16384).decode("utf-8")