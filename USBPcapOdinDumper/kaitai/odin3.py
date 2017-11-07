# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import struct


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Odin3(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/Benjamin-Dobell/Heimdall/tree/master/heimdall/source
    """

    class ChipType(Enum):
        ram = 0
        nand = 1

    class TrRequest(Enum):
        flash = 0
        dump = 1
        part = 2
        end = 3
        unknown2000 = 8192

    class Destination(Enum):
        phone = 0
        modem = 1

    class PacketType(Enum):
        send_file_part = 0
        session = 100
        pit_file = 101
        file_transfer = 102
        end_session = 103
        unknown06e0001b = 115343387
        unknown4590001b = 1167065115
        unknown6a60001b = 1784676379
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.type = self._root.PacketType(self._io.read_u4le())
        _on = self.type
        if _on == self._root.PacketType.end_session:
            self._raw_content = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_content))
            self.content = self._root.EndSession(io, self, self._root)
        elif _on == self._root.PacketType.file_transfer:
            self._raw_content = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_content))
            self.content = self._root.FileTransfer(io, self, self._root)
        elif _on == self._root.PacketType.pit_file:
            self._raw_content = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_content))
            self.content = self._root.PitFile(io, self, self._root)
        elif _on == self._root.PacketType.session:
            self._raw_content = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_content))
            self.content = self._root.Session(io, self, self._root)
        else:
            self.content = self._io.read_bytes_full()

    class EndSession(KaitaiStruct):

        class Request(Enum):
            end_session = 0
            reboot_device = 1
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = self._root.EndSession.Request(self._io.read_u4le())


    class FileTransfer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = self._root.TrRequest(self._io.read_u4le())
            _on = self.request
            if _on == self._root.TrRequest.flash:
                self.content = self._root.FileTransfer.Flash(self._io, self, self._root)
            elif _on == self._root.TrRequest.dump:
                self.content = self._root.FileTransfer.Dump(self._io, self, self._root)
            elif _on == self._root.TrRequest.part:
                self.content = self._root.FileTransfer.Part(self._io, self, self._root)
            elif _on == self._root.TrRequest.end:
                self.content = self._root.FileTransfer.End(self._io, self, self._root)

        class Flash(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sequence_byte_count = self._io.read_u4le()


        class Part(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sequence_byte_count = self._io.read_u4le()
                self.part_index = self._io.read_u4le()


        class Dump(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.chip_type = self._root.ChipType(self._io.read_u4le())
                self.chip_id = self._io.read_u4le()


        class End(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.destination = self._root.Destination(self._io.read_u4le())
                self.sequence_byte_count = self._io.read_u4le()
                self.unknown1 = self._io.read_u4le()
                self.device_type = self._io.read_u4le()
                _on = self.destination
                if _on == self._root.Destination.phone:
                    self.content = self._root.FileTransfer.End.Phone(self._io, self, self._root)
                self.end_of_file = self._io.read_u4le()

            class Phone(KaitaiStruct):

                class File(Enum):
                    primary_bootloader = 0
                    pit = 1
                    secondary_bootloader = 3
                    secondary_bootloader_backup = 4
                    kernel = 6
                    recovery = 7
                    tablet_modem = 8
                    modem = 11
                    unknown12 = 18
                    efs = 20
                    param_lfs = 21
                    factory_file_system = 22
                    database_data = 23
                    cache = 24
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.file_identifier = self._root.FileTransfer.End.Phone.File(self._io.read_u4le())




    class PitFile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = self._root.TrRequest(self._io.read_u4le())
            _on = self.request
            if _on == self._root.TrRequest.flash:
                self.content = self._root.PitFile.Flash(self._io, self, self._root)
            elif _on == self._root.TrRequest.part:
                self.content = self._root.PitFile.Part(self._io, self, self._root)
            elif _on == self._root.TrRequest.end:
                self.content = self._root.PitFile.End(self._io, self, self._root)

        class Flash(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.part_size = self._io.read_u4le()


        class Part(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.part_index = self._io.read_u4le()


        class End(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.file_size = self._io.read_u4le()



    class Session(KaitaiStruct):

        class Request(Enum):
            begin_session = 0
            device_type = 1
            total_bytes = 2
            enable_some_sort_of_flag = 3
            file_part_size = 5
            enable_tflash = 8
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = self._root.Session.Request(self._io.read_u4le())
            _on = self.request
            if _on == self._root.Session.Request.total_bytes:
                self.content = self._root.Session.TotalBytes(self._io, self, self._root)
            elif _on == self._root.Session.Request.file_part_size:
                self.content = self._root.Session.FilePartSize(self._io, self, self._root)

        class FilePartSize(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.file_part_size = self._io.read_u4le()


        class TotalBytes(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.total_bytes = self._io.read_u4le()



    @property
    def odin_handshake_message(self):
        if hasattr(self, '_m_odin_handshake_message'):
            return self._m_odin_handshake_message if hasattr(self, '_m_odin_handshake_message') else None

        self._m_odin_handshake_message = self._io.ensure_fixed_contents(struct.pack('5b', 79, 68, 73, 78, 0))
        return self._m_odin_handshake_message if hasattr(self, '_m_odin_handshake_message') else None

    @property
    def loke_handshake_message(self):
        if hasattr(self, '_m_loke_handshake_message'):
            return self._m_loke_handshake_message if hasattr(self, '_m_loke_handshake_message') else None

        self._m_loke_handshake_message = self._io.ensure_fixed_contents(struct.pack('4b', 76, 79, 75, 69))
        return self._m_loke_handshake_message if hasattr(self, '_m_loke_handshake_message') else None


