"""
Casino games for the casinos.

Mostly written as an experiment for myself to learn more with.
"""

from evennia import Command as BaseCommand
from evennia import default_cmds
import random

class cmdSlots(default_cmds.MuxCommand):
	"""
	Slot machine!
	
	Accepts bits, spits out maybe some more bits!
	
	Incomplete.
	"""
	#Based on the assumed odds from "Double Strike". Found here:
	#http://wizardofodds.com/games/slots/appendix/1/
	
	key = "slots"
	help_category = "casinos"
	
	def func(self):
		caller = self.caller
		
		#Translation:
		#B7: Blue 7
		#D5B: Double 5 bar
		#R7: Red 7
		#G7: Green 7
		#DB7: Double Blue 7
		#SB: Single Bar
		#DR7: Double Red 7
		#5B: Five Bar
		#
		
		#Weighted slot list.
		slotlist = ["G7", "B7"]
		#For building the UI later
		#I am absolutely certain there HAS to be a better way to do this, because this is dumb as fuck.
		#But so am I, so I don't know a better way!
		B7 = {"pos1" : "=", "pos2" : " ", "pos3" : "|0157", "pos4" : " ", "pos5" : "5=5"}
		Blank1 = {"pos1" : " ", "pos2" : "|0157", "pos3" : " ", "pos4" : "5=5", "pos5" : " "}
		D5B = {"pos1" : "|0157", "pos2" : " ", "pos3" : "5=5", "pos4" : " ", "pos5" : "|5007"}
		Blank2 = {"pos1" : " ", "pos2" : "5=5", "pos3" : " ", "pos4" : "|5007", "pos5" : ""}
		R7 = {"pos1" : "5=5", "pos2" : " ", "pos3" : "|5007", "pos4" : " ", "pos5" : "= ="}
		Blank3 = {"pos1" : " ", "pos2" : "|5007", "pos3" : "", "pos4" : "= =", "pos5" : " "}
		DSB = {"pos1" : "|5007", "pos2" : " ", "pos3" : "= =", "pos4" : " ", "pos5" : "|0407"}
		Blank4 = {"pos1" : " ", "pos2" : "= =", "pos3" : " ", "pos4" : "|0407", "pos5" : " "}
		G7 = {"pos1" : "= =", "pos2" : " ", "pos3" : "|0407", "pos4" : " ", "pos5" : "|0157 7"}
		Blank5 = {"pos1" : " ", "pos2" : "|0407", "pos3" : " ", "pos4" : "|0157 7", "pos5" : " "}
		DB7 = {"pos1" : "|0407", "pos2" : " ", "pos3" : "|0157 7", "pos4" : " ", "pos5" : "="}
		Blank6 = {"pos1" : " ", "pos2" : "|0157 7", "pos3" : " ", "pos4" : "=", "pos5" : " "}
		SB1 = {"pos1" : "|0157 7", "pos2" : " ", "pos3" : "=", "pos4" : " ", "pos5" : "|5007 7"}
		Blank7 = {"pos1" : " ", "pos2" : "=", "pos3" : " ", "pos4" : "|5007 7", "pos5" : " "}
		DR7 = {"pos1" : "=", "pos2" : " ", "pos3" : "|5007 7", "pos4" : " ", "pos5" : "=5="}
		Blank8 = {"pos1" : " ", "pos2" : "|5007 7", "pos3" : " ", "pos4" : "=5=", "pos5" : " "}
		B5 = {"pos1" : "|5007 7", "pos2" : " ", "pos3" : "=5=", "pos4" : " ", "pos5" : "|0407 7"}
		Blank9 = {"pos1" : " ", "pos2" : "=5=", "pos3" : " ", "pos4" : "|0407 7", "pos5" : " "}
		DG7 = {"pos1" : "=5=", "pos2" : " ", "pos3" : "|0407 7", "pos4" : " ", "pos5" : "="}
		Blank10 = {"pos1" : " ", "pos2" : "|0407 7", "pos3" : " ", "pos4" : "=", "pos5" : " "}
		SB2 = {"pos1" : "|0407 7", "pos2" : " ", "pos3" : "=", "pos4" : " ", "pos5" : "|0157"}
		Blank11 = {"pos1" : " ", "pos2" : "=", "pos3" : " ", "pos4" : "|0157", "pos5" : " "}
		
		#Performs the actual roll, randomly picks from the weighted list
		leftroll = random.choice(slotlist)
		midroll = random.choice(slotlist)
		rightroll = random.choice(slotlist)
		
		#declare columns
		leftcolumn = {}
		midcolumn = {}
		rightcolumn = {}
		
		#Remember what I said about being dumb as fuck?
		#Hey-o!
		#This builds the columns. Again, got to be a better way.
		if leftroll == "G7":
			leftcolumn = G7.copy()
		if midroll == "G7":
			midcolumn = G7.copy()
		if rightroll == "G7":
			rightcolumn = G7.copy()
		if leftroll == "B7":
			leftcolumn = B7.copy()
		if midroll == "B7":
			midcolumn = B7.copy()
		if rightroll == "B7":
			rightcolumn = B7.copy()
		
		
		#Debug message to player for testing, remove me when done
		caller.msg("%(1)s   %(2)s   %(3)s" % {"1" : leftroll, "2" : midroll, "3" : rightroll})
		
		#Display the roll to the player
		caller.msg("------------------------")
		caller.msg("$  %(1)s  |n$  %(2)s  $  %(3)s  $" % {"1" : leftcolumn["pos1"], "2" : midcolumn["pos1"], "3" : rightcolumn["pos1"]})
		caller.msg("$  %(1)s  $  %(2)s  $  %(3)s  $" % {"1" : leftcolumn["pos2"], "2" : midcolumn["pos2"], "3" : rightcolumn["pos2"]})
		caller.msg("$> %(1)s  $  %(2)s  $  %(3)s  $" % {"1" : leftcolumn["pos3"], "2" : midcolumn["pos3"], "3" : rightcolumn["pos3"]})
		caller.msg("$  %(1)s  $  %(2)s  $  %(3)s  $" % {"1" : leftcolumn["pos4"], "2" : midcolumn["pos4"], "3" : rightcolumn["pos4"]})
		caller.msg("$  %(1)s  $  %(2)s  $  %(3)s  $" % {"1" : leftcolumn["pos5"], "2" : midcolumn["pos5"], "3" : rightcolumn["pos5"]})
