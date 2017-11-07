# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from .endpoint_number import EndpointNumber
from .linux_usb_setup import LinuxUsbSetup
class Usbmon(KaitaiStruct):
    """A native pcap header of [usbmon](https://www.kernel.org/doc/Documentation/usb/usbmon.txt) part of Linux kernel.
    
    .. seealso::
       Source - https://www.kernel.org/doc/Documentation/usb/usbmon.txt
       https://www.kernel.org/doc/html/latest/driver-api/usb/URB.html
       https://wiki.wireshark.org/USB
    """
    def __init__(self, header_size, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.header_size = header_size
        self._read()

    def _read(self):
        self._raw_header = self._io.read_bytes(self.header_size)
        io = KaitaiStream(BytesIO(self._raw_header))
        self.header = self._root.Header(io, self, self._root)
        self.data = self._io.read_bytes(self.header.data_size)

    class Timestamp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.seconds = self._io.read_s8le()
            self.microseconds = self._io.read_s4le()


    class Header(KaitaiStruct):
        """The header, except for the 'setup' field, is in host byte order.
        """

        class EventType(Enum):
            completion = 67
            error = 69
            submit = 83

        class TransferType(Enum):
            isochronous = 0
            interrupt = 1
            control = 2
            bulk = 3

        class SetupFlag(Enum):
            relevant = 0
            irrelevant = 45

        class DataFlag(Enum):
            present = 0
            incoming = 60
            outgoing = 62
            error = 69
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.urb_id = self._io.read_u8le()
            self.event_type = self._root.Header.EventType(self._io.read_u1())
            self.transfer_type = self._root.Header.TransferType(self._io.read_u1())
            self.endpoint_number = EndpointNumber(self._io)
            self.device_address = self._io.read_u1()
            self.bus_id = self._io.read_u2le()
            self.setup_flag = self._root.Header.SetupFlag(self._io.read_u1())
            self.data_flag = self._root.Header.DataFlag(self._io.read_u1())
            self.timestamp = self._root.Timestamp(self._io, self, self._root)
            self.status = self._io.read_s4le()
            self.urb_size = self._io.read_s4le()
            self.data_size = self._io.read_s4le()
            if self.setup_flag == self._root.Header.SetupFlag.relevant:
                self.setup = LinuxUsbSetup(self._io)




