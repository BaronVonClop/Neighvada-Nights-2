"""
Very rough test of a bboard system.

Follow instructions in typeclasses/bboards.py for setup.
"""

from evennia import Command
from evennia import default_cmds
from evennia import create_object
from typeclasses import bboards

class cmdBbpost(default_cmds.MuxCommand):
	"""
	**VERY HEAVY BETA**
	
	Create a post on the bulletin board.
	
	Usage:
	
	+bbpost <title>=<text>
	
	By Applejack/Baron
	"""

	key = "+bbpost"
	help_category= "BBS"
	

	
	
	def func(self):
	
		#grab the master bboard item
		target = self.caller.search("bboard")
		#increment the post number and then capture it
		target.db.bboardposts += 1
		postnumber = target.db.bboardposts
		#add the text to that post
		target.db.bboarddict["posttext%i" % postnumber] = self.text
		#add the author to that post
		target.db.bboarddict["postauthor%i" % postnumber] = self.caller
		#add title to the post
		target.db.bboarddict["posttitle%i" % postnumber] = self.title
		self.caller.msg("Your post has been added to the bboard as number %s" % postnumber)
		
		#TODO: ADD DATE
		#
		
class cmdBbread(default_cmds.MuxCommand):
	"""
	A barely working bboard read!
	
	Usage:
	+bbread <post number>
	
	Accepts nothing else.
	Well, okay. It does and then crashes.
	"""
	
	key = "+bbread"
	help_category = "BBS"
	
	def func(self):
		
		caller = self.caller
		#target the master bboard item
		target = self.caller.search("bboard")
		#get total number of posts
		postnumber = target.db.bboardposts
		if not self.args:
			self.caller.msg("===== BBOARD =====")
			x = 1
			while (x <= postnumber):
				self.caller.msg("%(1)i: %(2)s" % {"1" : x, "2" : target.db.bboarddict["posttitle%i" % x]})
				x += 1
			self.caller.msg("===== END OF POSTS =====")
		else:
			self.caller.msg("===== POST %s =====" % self.args)
			self.caller.msg("Title: %s" % target.db.bboarddict["posttitle%s" % self.args])
			self.caller.msg("Posted By: %s" % target.db.bboarddict["postauthor%s" % self.args])
			self.caller.msg(" ")
			self.caller.msg("%s" % target.db.bboarddict["posttext%s" % self.args])
			self.caller.msg("===================")
		
		#TODO: Error message for non-valid post
		
# Obviously unfinished +bbdelete.
# class cmdBbdelete(default_cmds.MuxCommand):
	# """
	
	# """
	
	# key = "+bbdelete"
	# help_category = "BBS"