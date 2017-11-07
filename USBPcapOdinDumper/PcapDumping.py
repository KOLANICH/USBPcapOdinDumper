from .kaitai.pcap import *
from .Dumping import Dumping
from .Packet import Packet

from RichConsole import groups

class PcapDumping(Dumping):
	def isUseful(dumper, packet):
		return bool(packet.body) and not isinstance(packet.meta, Exception)
	
	def getPackets(fileName):
		p=Pcap.from_file(fileName)
		for i, packet in p.packets.items():
			if isinstance(packet.body, tuple): # an error has occured
				yield Packet(index=i, meta=packet.body[0], body=packet.body[0])
			else:
				yield Packet(index=i, body=packet.body, name=groups.Fore.cyan(str(i)) )