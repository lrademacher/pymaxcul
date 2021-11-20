import telnetlib
from urllib.parse import urlparse


class TelnetSerial:

    def __init__(self, device_path, timeout=None):
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
        try:
            return self._telnet.read_until(b'\n', timeout=self._timeout)
        except:
            # TODO: improve error handling
            raise TelnetException()

    def write(self, data):
        try:
            self._telnet.write(data)
        except:
            # TODO: improve error handling
            raise TelnetException()


class TelnetException(IOError):
    pass
