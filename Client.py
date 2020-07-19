import socket
import time

class ClientError(Exception):
    pass


class Client:
    def __init__(self,ip, port, timeout = None):
        self.sock = socket.create_connection((ip, port), timeout)

    def put(self, metrik_name, value, timestamp = None):
        if  timestamp == None:
            timestamp = int(time.time())
        data = "put " + metrik_name + " " + str(value) + " " + str(timestamp) + "\n"
        try:
            self.sock.sendall(data.encode("utf-8"))
            response = self.sock.recv(1024)
            if response == "error\nwrong command\n\n":
                raise ClientError

        except socket.timeout:
            raise ClientError
        response = response.decode("utf-8")
        response = response.split("\n")
        response = [i for i in response if i]
        if not len(response) == 1 or not response[0] == "ok":
            raise ClientError

    def get_dict(self, data):
        d = {}
        data = data.split("\n")
        data = [i for i in data if i]
        if data[0] != "ok":
            raise ClientError
        if len(data) > 1:
            data = data[1::]
            for metrik in data:
                metrik =metrik.split()
                if len(metrik) != 3:
                    raise ClientError
                try:
                    metrik[1] = float(metrik[1])
                    metrik[2] = int(metrik[2])
                    values = tuple(metrik[2:0:-1])
                    if metrik[0] in d:
                        d[metrik[0]].append(values)
                    else:
                        d[metrik[0]] = []
                        d[metrik[0]].append(values)
                except ValueError:
                    raise ClientError
            d1 = dict()
            for key, value in d.items():
                value = sorted(value, key = lambda m: m[0])
                d1[key]=value
            return d1


        return d


    def get(self, name_metrik):
        data = "get " + name_metrik + "\n"
        try:
            self.sock.sendall(data.encode("utf-8"))
            response = self.sock.recv(1024)
            if response == "error\nwrong command\n\n":
                raise ClientError

        except socket.timeout:
            raise ClientError

        response = response.decode("utf-8")
        d = self.get_dict(response)

        return d

    def close(self):
        self.sock.close()



if __name__ == "__main__":


    client = Client("127.0.0.1", 8888, timeout=15)
    print(client.get("*"))

    client.close()

