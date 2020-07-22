# The MIT License (MIT)

# Copyright (c) 2020, Tangliufeng for labplus Industries

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from bluetooth import UUID
from ..gatts import Profile
from ..services import Service
from ..characteristics import Characteristic
from .peripheral import Peripheral


class BLEUART(Peripheral):
    """ UART (Transmit transparently) """

    def __init__(self, name=b'ble_uart', appearance=0, rxbuf=100):
        UART_SERVICE = Service(UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E'))
        UART_TX = Characteristic(UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E'), properties='-n')
        UART_RX = Characteristic(UUID('6E400002-B5A3-F393-E0A9-E50E24DCCA9E'), properties='-w')
        profile = Profile()
        profile.add_services(UART_SERVICE.add_characteristics(UART_TX, UART_RX))
        super().__init__(name=name, profile=profile, resp_services=profile.services_uuid, appearance=appearance)

        self._rx_handle = UART_RX.value_handle
        self._tx_handle = UART_TX.value_handle
        self.rx_buffer = bytearray()
        self.ble.gatts_set_buffer(self._rx_handle, rxbuf, True)
        self.write_callback(self._uart_cb)
        self._rx_cb = None
        self.advertise(True)

    def _uart_cb(self, conn_handle, attr_handle, data):
        if attr_handle == self._rx_handle:
            self.rx_buffer += data
            if self._rx_cb:
                self._rx_cb()

    def irq(self, handler):
        self._rx_cb = handler

    def any(self):
        return len(self.rx_buffer)

    def read(self, size=None):
        if not size:
            size = len(self.rx_buffer)
        result = self.rx_buffer[0:size]
        self.rx_buffer = self.rx_buffer[size:]
        return result

    def write(self, data):
        self.attrubute_write(self._tx_handle, data, notify=True)

    def close(self):
        self.disconnect()
