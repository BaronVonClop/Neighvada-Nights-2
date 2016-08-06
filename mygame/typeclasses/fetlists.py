"""
Creation of a fetlist item. This hosts the tag dict for fetlist.

@create/drop fetlist:fetlists.fetlist

Theoretically this can be made with a create_object "setup" command, but that's way too elegant for me.

GUARD THE CREATED ITEM WITH YOUR LIFE, it hosts all the fetlist tags. Deletion or modification means all your fetlist tags are deleted.

You must also have NOTHING else named exactly "fetlist" in the game.
"""

from typeclasses.objects import Object
	
class fetlist(Object):
	def at_object_creation(self):
		self.db.fetlisttagdict = {}
		self.db.fetlisttaglist = []