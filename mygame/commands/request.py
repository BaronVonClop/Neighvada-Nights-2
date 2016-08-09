"""
"""
from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils import evtable
from evennia.utils.evmenu import EvMenu

class cmdRequest(default_cmds.MuxCommand):
	"""
	Request system. This is for players to submit support tickets,
	which wizards can access and respond to.
	"""
	
	key = "request"
	help_category = "general"
	
	def func(self):
		
		#target the request item
		target = self.caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
		#If "open" is the arg, we open the new ticket menu
		EvMenu(self.caller, "world.request", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)