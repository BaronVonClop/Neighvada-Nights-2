"""
Creation of a bboard object. Theoretically, this should only need to be called once ever with:

@create/drop bboard:bboards.bboard

Theoretically this can be made with a create_object "setup" command, but that's way too elegant for me.

GUARD THE CREATED ITEM WITH YOUR LIFE, it hosts all the bboard posts. Deletion or modification means all your bboard posts are deleted.

You must also have NOTHING else named exactly "bboard" in the game.
"""

from typeclasses.objects import Object
	
class bboard(Object):
	def at_object_creation(self):
		self.db.bboardposts = 0
		self.db.bboarddict = {'posttext0': None, 'posttitle0': None, 'postauthor0': None}

		
#Depreciated, but kept just in case

# class bboardpost(Object):
	# def at_object_creation(self):
		# self.db.bboardtext = ""
		# self.db.bboardauthor = ""
		# self.db.date = ""