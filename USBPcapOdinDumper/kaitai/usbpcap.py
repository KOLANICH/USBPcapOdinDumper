# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from .endpoint_number import EndpointNumber
class Usbpcap(KaitaiStruct):
    """A native pcap header of [usbpcap](https://github.com/desowin/usbpcap) - an app to capture USB frames in Windows OSes.
    
    .. seealso::
       Source - http://desowin.org/usbpcap/captureformat.html
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._root.Header(self._io, self, self._root)
        self.data = self._io.read_bytes(self.header.header_main.data_size)

    class UsbdStatus(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.code = self._io.read_u4le()


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header_size = self._io.read_u2le()
            self._raw_header_main = self._io.read_bytes((self.header_size - 2))
            io = KaitaiStream(BytesIO(self._raw_header_main))
            self.header_main = self._root.Header.HeaderMain(io, self, self._root)

        class HeaderMain(KaitaiStruct):

            class TransferType(Enum):
                isochronous = 0
                interrupt = 1
                control = 2
                bulk = 3
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.io_request_packet_id = self._io.read_u8le()
                self.usbd_status_code = self._root.UsbdStatus(self._io, self, self._root)
                self.urb_function = self._io.read_u2le()
                self.io_request_info = self._root.Header.HeaderMain.Info(self._io, self, self._root)
                self.bus = self._io.read_u2le()
                self.device_address = self._io.read_u2le()
                self.endpoint_number = EndpointNumber(self._io)
                self.transfer_type = self._root.Header.HeaderMain.TransferType(self._io.read_u1())
                self.data_size = self._io.read_u4le()
                _on = self.transfer_type
                if _on == self._root.Header.HeaderMain.TransferType.isochronous:
                    self._raw_additional_header = self._io.read_bytes_full()
                    io = KaitaiStream(BytesIO(self._raw_additional_header))
                    self.additional_header = self._root.Header.HeaderMain.IsochHeader(io, self, self._root)
                elif _on == self._root.Header.HeaderMain.TransferType.control:
                    self._raw_additional_header = self._io.read_bytes_full()
                    io = KaitaiStream(BytesIO(self._raw_additional_header))
                    self.additional_header = self._root.Header.HeaderMain.ControlHeader(io, self, self._root)
                else:
                    self.additional_header = self._io.read_bytes_full()

            class Info(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.reserved = self._io.read_bits_int(7)
                    self.pdo_to_fdo = self._io.read_bits_int(1) != 0


            class IsochHeader(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.start_frame = self._io.read_u8le()
                    self.packet_count = self._io.read_u8le()
                    self.error_count = self._io.read_u8le()
                    self.packet = self._root.Header.HeaderMain.IsochHeader.IsochPacket(self._io, self, self._root)

                class IsochPacket(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.offset = self._io.read_u8le()
                        self.size = self._io.read_u8le()
                        self.status = self._root.UsbdStatus(self._io, self, self._root)



            class ControlHeader(KaitaiStruct):

                class Stage(Enum):
                    setup = 0
                    data = 1
                    status = 2
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.stage = self._root.Header.HeaderMain.ControlHeader.Stage(self._io.read_u1())





