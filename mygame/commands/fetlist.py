"""
Fetlist. Serves as replacement for wixxx from ProtoMUCK.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdFetlist(default_cmds.MuxCommand):
	"""
	Read another player's fetlist.
	
	Usage:
	+fetlist <player>
	
	Other commands; use 'help <command>' for more detail:
	+fetlistaddf - Adds a kink to your "fave" category.
	+fetlistaddy - Adds a kink to your "yes" category.
	+fetlistaddm - Adds a kink to your "maybe" category.
	+fetlistclear - Deletes all your kinks.
	
	By Applejack/Baron Von Clop.
	"""

	key = "+fetlist"
	aliases = ["fetlist", "wixxx", "+wixxx"]
	help_category= "fetlist"
	
	def func(self):
	
		#Target the player
		target = self.caller.search(self.args)
		#Find the longest list:
		# if (len(target.db.fetlistf) >= len(target.db.fetlisty)):
			# maxlength = len(target.db.fetlistf)
		# if (len(target.db.fetlisty) >= len(target.db.fetlistf)):
			# maxlength = len(target.db.fetlisty)
		# if (maxlength < target.db.fetlistm):
			# maxlength = len(target.db.fetlistm)
		#print beginning
		self.caller.msg("======= |015FAVE|n =======$======= |040YES|n ========$======= |550MAYBE|n ======$")
		#now let's print the rest
		maxlength = 50
		x=1
		while (x < maxlength):
			#if all three have an entry at fetlistn[x]
			if len(target.db.fetlistf) >= x and len(target.db.fetlisty) >= x and len(target.db.fetlistm) >= x:
				self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
				x += 1
			#if only f and y have an entry at fetlistn[x]
			elif len(target.db.fetlistf) >= x and len(target.db.fetlisty) >= x:
				self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("") + "$")
				x += 1
			#if only y and m have an entry at fetlistn[x]
			elif len(target.db.fetlisty) >= x and len(target.db.fetlistm) >= x:
				self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
				x += 1
			#if only f and m have an entry at fetlistn[x]
			elif len(target.db.fetlistf) >= x and len(target.db.fetlistm) >= x:
				self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
				x += 1
			#if only m has an entry at fetlistn[x]
			elif len(target.db.fetlistm) >= x:
				self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
				x += 1
			#if only y has an entry at fetlistn[x]
			elif len(target.db.fetlisty) >= x:
				self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("") + "$")
				x += 1
			#if only f has an entry at fetlistn[x]
			elif len(target.db.fetlistf) >= x:
				self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("") + "$")
				x += 1
			#catch to prevent infinite loop
			else:
				x +=1
				
			
			
		#print ending
		self.caller.msg("====================$====================$====================$")
		
		
		

		
class cmdFetlistaddf(default_cmds.MuxCommand):
	"""
	Add something to your favorites on fetlist.
	"""
	
	key = "+fetlistaddf"
	aliases = ["fetlistaddf", "wixxxaddf", "+wixxxaddf"]
	help_category = "fetlist"
	
	def func(self):
		
		caller = self.caller
		
		#Check length
		if not (len(self.args) <=20):
			self.caller.msg("That is too long! Additions must be <=20 characters.")
			return
			
		#Length passed, add to kink list
		caller.db.fetlistf.append(self.args)
		caller.msg("Added %s to your Favorites on fetlist." % self.args)
		
class cmdFetlistaddy(default_cmds.MuxCommand):
	"""
	Add something to your "yes" list on fetlist.
	
	Usage:
	+fetlistaddf <kink>
	"""
	
	key = "+fetlistaddy"
	aliases = ["fetlistaddy", "wixxxaddy", "+wixxxaddy"]
	help_category = "fetlist"
	
	def func(self):
		
		caller = self.caller
		
		#Check length
		if not (len(self.args) <=20):
			self.caller.msg("That is too long! Additions must be <=20 characters.")
			return
			
		#Length passed, add to kink list
		caller.db.fetlisty.append(self.args)
		caller.msg("Added %s to your Yes list on fetlist." % self.args)
		
class cmdFetlistaddm(default_cmds.MuxCommand):
	"""
	Add something to your "maybe" list on fetlist.
	
	Usage:
	+fetlistaddm <kink>
	"""
	
	key = "+fetlistaddm"
	aliases = ["fetlistaddm", "wixxxaddm", "+wixxxaddm"]
	help_category = "fetlist"
	
	def func(self):
		
		caller = self.caller
		
		#Check length
		if not (len(self.args) <=20):
			self.caller.msg("That is too long! Additions must be <=20 characters.")
			return
			
		#Length passed, add to kink list
		caller.db.fetlistm.append(self.args)
		caller.msg("Added %s to your Maybe list on fetlist." % self.args)
		
class cmdFetlistclear(default_cmds.MuxCommand):
	"""
	Clear all your kinks.
	
	This will IRREVERSIBLY wipe out ALL of your kink list; be sure you want to do this!
	
	Usage:
	+Fetlistclear
	"""
	
	key = "+fetlistclear"
	aliases = ["fetlistclear", "wixxxclear", "+wixxxclear"]
	help_category = "fetlist"
	
	def func(self):
		
		caller = self.caller
		del caller.db.fetlistf[:]
		del caller.db.fetlisty[:]
		del caller.db.fetlistm[:]
		caller.msg("Your kinks have been cleared.")
		
		
#DEPRECIATED CODE BELOW
#Used for the old system of tags and a main tag DB. No longer needed.
#Replaced in favor of the more flexible and far less frustrating "custom" tag system.
		
		
#class cmdFetlistnewtag(default_cmds.MuxCommand):
	# """
	# Add a tag to the Fetlist db.
	
	# Wizards only.
	
	# Usage:
	# +fetlistnewtag <tag>=<definition>
	# """
	
	# key = "+fetlistnewtag"
	# help_category = "fetlist"
	
	# def parse(self):
		# #split args into two things; tag and desc
		# tag, desc = None, None
		# if "=" in self.args:
			# tag, desc = [part.strip() 
							# for part in self.args.rsplit("=", 1)]
			# self.tag, self.desc = tag, desc
	
	# def func(self):
		
		# #target the fetlist master item
		# target = self.caller.search("fetlist")
		# #check length for stuff
		# if (len(self.tag) > 3):
			# self.caller.msg("Tag length too long. Must be <=3 characters.")
			# return
		# if (len(self.desc) > 20):
			# self.caller.msg("Description too long. Must be <=20 characters.")
			# return
		# #arg passed, let's commit it to the DB
		# target.db.fetlisttagdict["%s" % self.tag] = self.desc
		# target.db.fetlisttaglist.append(self.tag)
		# self.caller.msg("Tag %(1)s added with definition %(2)s" % {"1" : self.tag, "2" : self.desc})

# class cmdFetlisttags(default_cmds.MuxCommand):
	# """
	# View all tags.
	
	# Usage:
	# +fetlisttags
	# """
	# key = "+fetlisttags"
	# help_category = "fetlist"
	
	# def func(self):
		# #target fetlist master
		# target = self.caller.search("fetlist")

		# #if no args, display whole list
		# if not self.args:
			# #header
			# self.caller.msg("The following tags are in the database and available for use:")
			# #while loop for tags
			# x=0
			# tagnumber = len(target.db.fetlisttaglist)
			# while (x < tagnumber):
				# self.caller.msg("%s" % target.db.fetlisttaglist[x])
				# x += 1
		