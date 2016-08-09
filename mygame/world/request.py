from evennia.utils.evtable import EvTable


def start(caller):
	caller.ndb._menutree.title = "BLANK"
	caller.ndb._menutree.body = "BLANK"
	text = \
	"""
	Welcome to the request system.
	
	This is used to submit trouble or issue tickets to wizards, who can then address the problem you're having.
	
	What would you like to do?
	
	Type "QUIT" to exit.
	"""
	
	options = ({"desc": "Open a new ticket.",
				"goto": "open_ticket"},
				{"desc": "View my open tickets.",
				"goto": "view_open_tickets"},
				{"desc": "Close a ticket.",
				"goto": "close_ticket"},
				{"desc": "View my closed tickets.",
				"goto": "view_closed_tickets"})
				
	return text, options
	
def open_ticket(caller):
	text = \
	"""
	|500 OPEN TICKET|n
	
	Alright! Let's open a ticket, then.
	
	Type "QUIT" to exit without submitting and discard changes.
	"""
	
	text += "|/Your ticket's current info is:"
	text += "|/|/Title: %s" % caller.ndb._menutree.title
	text += "|/|/Body: %s" % caller.ndb._menutree.body
	options = ({"desc": "Edit Title.",
				"goto": "edittitle"},
				{"desc": "Edit body.",
				"goto": "editbody"},
				{"desc": "Submit ticket.",
				"exec": _create_ticket,
				"goto": "start"})
				
	return text, options
	
def edittitle(caller):
	text = \
	"""
	Enter the title for your ticket.
	
	Be clear and concice on what your issue is.
	
	This is only a TITLE; save the details for the description!
	"""
	
	options = ({"key": "_default",
				"exec": _set_title,
				"goto": "open_ticket"})
	return text, options
	
def editbody(caller):
	text = \
	"""
	Enter the body for your ticket.
	
	Here you can give as much detail as you like! Screenshots, etc.
	
	Please note that if you are reporting a bug in code, you should submit an issue on github instead.
	"""
	
	options = ({"key": "_default",
				"exec": _set_body,
				"goto": "open_ticket"})
	return text, options
	
	
def _set_title(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a title!")
	else:
		caller.ndb._menutree.title = "%s" % inp
		caller.msg("Title set to %s." % caller.ndb._menutree.title)
		
def _set_body(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		caller.ndb._menutree.body = "%s" % inp
		caller.msg("Title set to %s." % caller.ndb._menutree.body)
		
def _create_ticket(caller):
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.msg("Submitting your ticket...")
	if caller.ndb._menutree.body == "BLANK" or caller.ndb._menutree.title == "BLANK":
		caller.msg("You tried to submit an unfinished ticket! Try again.")
	else:
		(target.db.requestdict["reqtext%i" % target.db.requestnum]) = caller.ndb._menutree.body
		(target.db.requestdict["reqtitle%i" % target.db.requestnum]) = caller.ndb._menutree.title
		caller.db.requestsmade.append(target.db.requestnum)
		caller.msg("Your ticket has been submitted as #%i" % target.db.requestnum)
		target.db.requestnum += 1