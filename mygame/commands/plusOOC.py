from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdPlusOoc(default_cmds.MuxCommand):
	
	
	key = "+OOC"
	aliases = ["GoOOC"]
	help_category = "movement"
	
	def func (self):
		caller = self.caller
		args = self.args
		caller.db.beforeooc = caller.location
		
		target = caller.search("[OOC] Lounge", global_search=True)
		
		caller.move_to(target)

class cmdPlusIC(default_cmds.MuxCommand):

	key = "+IC"
	aliases = ["GoIC"]
	help_category = "movement"
	
	def func (self):
		caller = self.caller
		args = self.args
		
		if not caller.db.beforeooc:
			caller.msg("You have no previous IC location.")
		else:
			caller.move_to(caller.db.beforeooc)
		