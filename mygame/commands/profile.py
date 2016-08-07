"""
Profile system for brief looks at someone's character, without a long description. 'At a glance' profile.

Meant to replicate the +finger/+hoof system from ProtoMUCK/MUF.
"""


from evennia import Command as BaseCommand
from evennia import default_cmds

class CmdViewProfile(default_cmds.MuxCommand):
	"""
	View the profile of another character. Race, gender, etc.
	
	usage:
	hoof <character>
	
	Written by Applejack/Baron Von Clop
	"""
	
	key = "+profile"
	help_category = "mush"
	aliases = ["hoof", "+hoof", "profile"]
	
	
	def func(self):
		errmsg = "That isn't a player name I recognize."
		caller = self.caller
		
		#if no equals sign, we assume it's a player, attempt to target it, and display profile for it.
		if not self.rhs:
			target = caller.search(self.args, global_search=True, typeclass="typeclasses.characters.Character")
			if not target:
				return
			if target:
				self.caller.msg("  |303/=============================\\")
				self.caller.msg(" |303/===========|550 PROFILE |303===========\\")
				self.caller.msg("|303/=================================\\")
				self.caller.msg("%(1)s the %(2)s %(3)s" % {"1" : target.name, "2" : target.db.gender, "3" : target.db.race})
				self.caller.msg("       AGE: %s" % target.db.age)
				self.caller.msg("    HEIGHT: %s" % target.db.height)
				self.caller.msg("    WEIGHT: %s" % target.db.weight)
				self.caller.msg("      COAT: %s" % target.db.coat)
				self.caller.msg("      MANE: %s" % target.db.mane)
				self.caller.msg("CUTIE MARK: %s" % target.db.cutiemark)
				self.caller.msg("|303.=================================.")
			
		if self.lhs == "race":
			errmsg = "You must supply a race under 20 characters."
			
			if not self.rhs:
				self.caller.msg(errmsg)
			
				
				
		
				
class CmdSetRace(default_cmds.MuxCommand):
    """
    Set the race of a character. This will be displayed on your +hoof.
	<=20 characters.
	
	Must follow the Wiki's guidelines for allowed races or you will be DENIED.
    
    Usage:
    +race <race>
    
    """

    key = "+race"
    help_category = "mush"
    
    def func(self):
        "Performs the actual command."
        errmsg = "You must supply a race under 20 characters."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            race = str(self.args)
        except ValueError:
            self.caller.msg(errmsg)
            return
        if not (len(race) < 20):
            self.caller.msg(errmsg)
            return
        # arg is valid, so set it.
        self.caller.db.race = race.strip()
        self.caller.msg("Your race was set to %s." % race)


class CmdSetGender(default_cmds.MuxCommand):
	"""
	Set the gender of a character. This will be displayed on your +hoof.
	<=20 characters.
	
	usage:
	+gender <gender>
	"""
	
	key = "+gender"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a gender under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			gender = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(gender) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.gender = gender
		self.caller.msg("Your gender was set to %s." % gender)
		
class CmdSetAge(default_cmds.MuxCommand):
	"""
	Set the Age of a character. This will be displayed on your +hoof.
	Numbers only.
	<=3 characters.
	
	usage:
	+age <age>
	"""
	
	key = "+age"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a number."
		errmsglen = "You must enter a number under 10 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			age = int(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.age = age
		self.caller.msg("Your age was set to %i." % age)
		
class CmdSetHeight(default_cmds.MuxCommand):
	"""
	Set the height of a character. This will be displayed on your +hoof.
	You can use a number or a description.
	<=20 characters.
	
	usage:
	+height <height>
	"""
	
	key = "+height"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a height under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			height = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(height) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.height = height
		self.caller.msg("Your height was set to %s." % height)
		
class CmdSetWeight(default_cmds.MuxCommand):
	"""
	Set the weight of a character. This will be displayed on your +hoof.
	You can use a number or a description.
	<=20 characters.
	
	usage:
	+weight <weight>
	"""
	
	key = "+weight"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a weight under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			weight = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(weight) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.weight = weight
		self.caller.msg("Your weight was set to %s." % weight)
		
class CmdSetCoat(default_cmds.MuxCommand):
	"""
	Set the coat color of a character. This will be displayed on your +hoof.
	<=20 characters.
	
	usage:
	+coat <coat>
	"""
	
	key = "+coat"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a coat color under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			coat = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(coat) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.coat = coat
		self.caller.msg("Your coat color was set to %s." % coat)
		
class CmdSetMane(default_cmds.MuxCommand):
	"""
	Set the mane color of a character. This will be displayed on your +hoof.
	<=20 characters.
	
	usage:
	+mane <mane>
	"""
	
	key = "+mane"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a mane color under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			mane = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(mane) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.mane = mane
		self.caller.msg("Your mane color was set to %s." % mane)
		
class CmdSetCutieMark(default_cmds.MuxCommand):
	"""
	Set the cutie mark of a character. This will be displayed on your +hoof.
	<=20 characters.
	
	usage:
	+cutiemark <Cutie Mark>
	"""
	
	key = "+cutiemark"
	help_category= "mush"
	
	def func(self):
		"Performs the actual command."
		errmsg = "You must enter a cutie mark under 20 characters."
		
		if not self.args:
			self.caller.msg(errmsg)
			return
		try:
			cutiemark = str(self.args)
		except ValueError:
			self.caller.msg(errmsg)
			return
		if not (len(cutiemark) <20 ):
			self.caller.msg(errmsg)
			return
		#arg has passed, so we can set it.
		self.caller.db.cutiemark = cutiemark
		self.caller.msg("Your cutie mark was set to %s." % cutiemark)