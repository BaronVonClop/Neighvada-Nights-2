"""
+staff

Shows a list of wizards, their names, and their roles.
"""

from evennia import Command as BaseCommand
from evennia import default_cmds


class cmdStaff(default_cmds.MuxCommand):
	"""
	Shows a list of staff members.
	
	Usage:
	+staff
	"""
	
	key = "+staff"
	help_category = "general"
	aliases = ["staff", "wiz"]
	target = None
	
	
	def func(self):
	
		def checkonline(target):
			if target.has_player == 1:
				self.online = "|040YES|n"
			else:
				self.online = "|500NO|n"
	
		caller = self.caller
		
		caller.msg("================= IMMORTALS ================")
		caller.msg("!   NAME   !      ROLE      !    ONLINE    !")
		target = caller.search("Applejack")
		checkonline(target)
		caller.msg("!Applejack ! Head Wiz/Coder !     %s" % self.online)