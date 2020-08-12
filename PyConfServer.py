import socket
class response:
    def gen_sys_event(self,who,what,to_who,flag):
        event = "sys:"+who+":"+what+":"+to_who+":"+flag
        return event
    def gen_msg(self,who,content):
        event = "msg:"+who+":"+content
        return event
    def get_response(self):
        sock = socket.socket()
        sock.bind(("", 5081))
        sock.listen(10)
        conn,addr = sock.accept()
        return conn.recv(16384).decode("utf-8")