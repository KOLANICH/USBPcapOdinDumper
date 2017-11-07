import os
from glob import glob
import importlib
from .OdinDumping import OdinDumping
from .USBPcapDumping import USBPcapDumping
from .PcapDumping import PcapDumping
from .Dumper import Dumper
import colorama
import sys, platform
from RichConsole import groups, RichStr

neededCharacters="←→"
if __name__=="__main__":
	import plumbum.cli
	class UnpackerCLI(plumbum.cli.Application):
		DESCRIPTION=r"""This shit unpacks usbpcap or usbmon .pcap files with odin3 protocol captures.It creates a directory for each file. If called without arguments, it processes all the pcap files in current folder. For the license see UNLICENSE file."""
		def main(self, *pcaps:plumbum.cli.ExistingFile):
			#sys.stdout = open('./res.txt','wt', encoding="utf-8")
			if platform.system() == "Windows":
				#colorama.init() # extremely glitchy
				try:
					bytes(neededCharacters, encoding=sys.stdout.encoding)
				except:
					print(groups.Fore.red("Your current console codepage (", groups.Fore.blue(sys.stdout.encoding), ") cannot show all the needed characters (", groups.Fore.green(repr(neededCharacters)) ,"). Type ", groups.Back.lightblackEx(groups.Fore.green("chcp"), " ", groups.Fore.blue("65001")), " to switch to ", groups.Fore.green("UTF-8")))
					return 1
			if not pcaps:
				pcaps=glob("./*.pcap")
			dumper=Dumper([PcapDumping, USBPcapDumping, OdinDumping])
			for fn in pcaps:
				print(RichStr("processing file ", groups.Fore.cyan(fn), " ..."))
				dumper.dump(fn)
	UnpackerCLI.run()