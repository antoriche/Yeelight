import telnetlib
import json

class Yeelight:
    def __init__(self, host, port=55443):
        self.telnet = telnetlib.Telnet(host, port)
    def __sel__(self):
        self.telnet.close()
    def __send_message(self, id_, method, params):
        self.telnet.write(str.encode(json.dumps({'id':id_, 'method':method, 'params':params})+"\r\n"))
        resp = None
        try:
            msg = self.telnet.read_until(b'\r\n', 1)
            resp = json.loads(msg)
        except:
            pass
        return resp


    def toggle(self):
        self.__send_message(0, 'toggle', [])
    def set_rgb(self, rgb, effect="smooth", duration=500):
        self.__send_message(0, 'set_rgb', [rgb, effect, duration])