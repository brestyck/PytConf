import socket, platform
class c:
    def g(self):return "\u001b[32m"
    def b(self):return "\u001b[34m"
    def y(self):return "\u001b[33m"
    def r(self):return "\u001b[31m"
    def d(self):return "\u001b[39m"
class sc:
    def r(self):return c.d(0)+"["+c.r(0)+"*"+c.d(0)+"] "
    def b(self):return c.d(0)+"["+c.r(0)+"*"+c.d(0)+"] "
    def y(self):return c.d(0)+"["+c.r(0)+"*"+c.d(0)+"] "
    def g(self):return c.d(0)+"["+c.r(0)+"*"+c.d(0)+"] "
if platform.system() == "Windows":
    cmds = {
        "hello": "PYCONF Client v1"
    }
else:
    cmds = {
        "hello": "PYCONF Client "+c.g(0)+"v1"+c.d(0)
    }
class response:
    def send_to(self, server, response_str, myuname):
        sock = socket.socket()
        sock.connect((server, 5081))
        sock.send(response_str.encode("utf-8"))
        sock.close()
    def get(self, server):
        sock = socket.socket()
        sock.connect((server, 5081))
        sock.send(b"parse")
        feedback = sock.recv(16384).decode("utf-8")
        return feedback
class parse_fbs:
    def out_sys_event(self,response):
        response = response.split(":")
        if platform.system() != "Windows":
            if response[4] == "low":
                out = sc.b(0)+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "happy":
                out = sc.g(0)+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "attention":
                out = sc.y(0)+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "critical":
                out = sc.r(0)+response[1]+" "+response[2]+" "+response[3]
        else:
            if response[4] == "low":
                out = "[*] "+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "happy":
                out = "[*] "+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "attention":
                out = "[*] "+response[1]+" "+response[2]+" "+response[3]
            if response[4] == "critical":
                out = "[*] "+response[1]+" "+response[2]+" "+response[3]
        return out
    def parse_msgs(self,response):
        response.split(":")
        out = response[1]+": "+response[2]
        return out
#MAIN CYCLE HERE:
print(cmds["hello"])