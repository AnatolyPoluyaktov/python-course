import asyncio
metriks = dict()
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
class DataError(Exception):
    pass

def append_in_dict(key, value):
    for i in range(len(metriks[key])):
        if metriks[key][i][1] == value[1]:
            metriks[key][i] = value
    if value not in metriks[key]:
        metriks[key].append(value)


def put_handler(data):
    try:
        data = data[0]
        if not data.endswith("\n"):
            raise DataError
        data = data.split()

        if len(data) == 3:
            name_server, percent, time = data
            time = time.replace("\n","")
            if not is_digit(percent) or not (is_digit(time)):
                 raise DataError

            if not name_server or name_server.isdigit():
                raise DataError
            if name_server in metriks:
                tup = (float(percent), int(time))
                if tup not in metriks[name_server]:
                    append_in_dict(name_server, tup)
            else:
                metriks[name_server] = []
                metriks[name_server].append((float(percent), int(time)))
            return "ok\n\n"

        else:
            raise DataError
    except (DataError,ValueError):
        raise

def get_handler(data):
    ans ="ok"
    data = data[0]
    try:
        if not data.endswith("\n"):
            raise DataError
        data = data.replace("\n","")
        if data == "*":
            for key, values in metriks.items():
                for i in values:
                    ans += ("\n" + key + " " + str(i[0]) + " " + str(i[1]))
            ans +="\n\n"
            return ans
        elif ' ' not in data :
            if data not in metriks:
                return "ok\n\n"
            else:
                for values in metriks[data]:
                    ans += ("\n" + data + " " + str(values[0]) + " " + str(values[1]))
                ans += "\n\n"
                return ans
        else:
            raise DataError
    except DataError:
        raise



    except DataError:
        raise

def process_data(data):
    data = data.split(" ", 1)
    try:
        if data[0] == "put":
            return put_handler(data[1:])

        if data[0] == "get":
            return get_handler(data[1:])

        else:
            raise DataError
    except (DataError, ValueError):
        return "error\nwrong command\n\n"



class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())

        self.transport.write(resp.encode())

def run_server(ip, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        ip, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
#run_server("127.0.0.1",8181)