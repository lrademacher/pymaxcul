import telnetlib
from urllib.parse import urlparse


class TelnetSerial:

    def __init__(self, device_path, timeout):
        parsed_device_path = urlparse(device_path)

        try:
            self._telnet = telnetlib.Telnet(
                parsed_device_path.hostname,
                parsed_device_path.port
            )
        except:
            raise TelnetException()

        self._timeout = timeout

    def close(self):
        self._telnet.close()

    def readline(self):
        return self._telnet.read_until(b'\n', timeout=self._timeout)

    def write(self, data):
        self._telnet.write(data)


class TelnetException(IOError):
    pass
