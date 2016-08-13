def start(caller):
	text = \
	"""
	Welcome to editplayer. This is a guided tool to set up your at-a-glance profile.
	
	What would you like to do?
	
	Your current profile:
	
	"""
	text += "%(1)s the %(2)s %(3)s" % {"1" : caller.name, "2" : caller.db.gender, "3" : caller.db.race}
	text += "|/AGE: %s" % caller.db.age
	text += "|/HEIGHT: %s" % caller.db.height
	text += "|/WEIGHT: %s" % caller.db.weight
	text += "|/COAT: %s" % caller.db.coat
	text += "|/MANE: %s" % caller.db.mane
	text += "|/CUTIE MARK: %s" % caller.db.cutiemark
	text += "|/Description: |/%s" % caller.db.desc
	
	
	options = ({"desc": "Edit gender.",
				"goto": "edit_gender"},
				{"desc": "Edit race.",
				"goto": "edit_race"},
				{"desc": "Edit height.",
				"goto": "edit_height"},
				{"desc": "Edit weight.",
				"goto": "edit_weight"},
				{"desc": "Edit coat.",
				"goto": "edit_coat"},
				{"desc": "Edit mane.",
				"goto": "edit_mane"},
				{"desc": "Edit cutie mark.",
				"goto": "edit_cutie"},
				{"desc": "Edit description.",
				"goto": "edit_desc"})
				
	return text, options
	
def edit_gender(caller):
	text = \
	"""
	Editing your gender.
	
	Type what you want your gender to appear as.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_gender,
			"goto": "start"})
			
	return text, options
	
def _edit_gender(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		if len(inp) <= 20:
			caller.db.gender = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")