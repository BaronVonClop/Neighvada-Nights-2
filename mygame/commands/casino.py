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
	
	Usage (debug only):
	slots
	
	Incomplete.
	"""
	#Based on the assumed odds from "Double Strike". Found here:
	#http://wizardofodds.com/games/slots/appendix/1/
	
	key = "slots"
	help_category = "casinos"
	
	def func(self):
		caller = self.caller
		payout = 0
		
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
		slotlist = ["B7", "B7", "B7", "Blank1", "Blank1",
						"D5B", "D5B", "Blank2", "Blank2", "Blank2",
						"R7", "R7", "Blank3", "Blank3", "Blank3",
						"DSB", "DSB", "DSB", "Blank4", "Blank4",
						"G7", "G7", "G7", "G7", "G7", "G7",
						"Blank5", "Blank5", "DB7", "DB7", "Blank6",
						"Blank6", "Blank6", "Blank6", "SB1", "SB1",
						"SB1", "SB1", "SB1", "SB1", "SB1", "Blank7",
						"Blank7", "Blank7", "Blank7", "Blank7",
						"DR7", "Blank8", "Blank8", "Blank8", "Blank8",
						"Blank8", "B5", "B5", "B5", "B5", "B5",
						"B5", "B5", "Blank9", "Blank9", "Blank9",
						"DG7", "DG7", "DG7", "Blank10", "Blank10",
						"SB2", "SB2", "Blank11", "Blank11"]
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
		#This builds the columns. Again, got to be a better way, because this is fucking DUMB.
		if leftroll == "B7":
			leftcolumn = B7.copy()
		if midroll == "B7":
			midcolumn = B7.copy()
		if rightroll == "B7":
			rightcolumn = B7.copy()
		if leftroll == "Blank1":
			leftcolumn = Blank1.copy()
		if midroll == "Blank1":
			midcolumn = Blank1.copy()
		if rightroll == "Blank1":
			rightcolumn = Blank1.copy()
		if leftroll == "D5B":
			leftcolumn = D5B.copy()
		if midroll == "D5B":
			midcolumn = D5B.copy()
		if rightroll == "D5B":
			rightcolumn = D5B.copy()
		if leftroll == "Blank2":
			leftcolumn = Blank2.copy()
		if midroll == "Blank2":
			midcolumn = Blank2.copy()
		if rightroll == "Blank2":
			rightcolumn = Blank2.copy()
		if leftroll == "R7":
			leftcolumn = R7.copy()
		if midroll == "R7":
			midcolumn = R7.copy()
		if rightroll == "R7":
			rightcolumn = R7.copy()
		if leftroll == "Blank3":
			leftcolumn = Blank3.copy()
		if midroll == "Blank3":
			midcolumn = Blank3.copy()
		if rightroll == "Blank3":
			rightcolumn = Blank3.copy()
		if leftroll == "DSB":
			leftcolumn = DSB.copy()
		if midroll == "DSB":
			midcolumn = DSB.copy()
		if rightroll == "DSB":
			rightcolumn = DSB.copy()
		if leftroll == "Blank4":
			leftcolumn = Blank4.copy()
		if midroll == "Blank4":
			midcolumn = Blank4.copy()
		if rightroll == "Blank4":
			rightcolumn = Blank4.copy()
		if leftroll == "G7":
			leftcolumn = G7.copy()
		if midroll == "G7":
			midcolumn = G7.copy()
		if rightroll == "G7":
			rightcolumn = G7.copy()
		if leftroll == "Blank5":
			leftcolumn = Blank5.copy()
		if midroll == "Blank5":
			midcolumn = Blank5.copy()
		if rightroll == "Blank5":
			rightcolumn = Blank5.copy()
		if leftroll == "DB7":
			leftcolumn = DB7.copy()
		if midroll == "DB7":
			midcolumn = DB7.copy()
		if rightroll == "DB7":
			rightcolumn = DB7.copy()
		if leftroll == "Blank6":
			leftcolumn = Blank6.copy()
		if midroll == "Blank6":
			midcolumn = Blank6.copy()
		if rightroll == "Blank6":
			rightcolumn = Blank6.copy()
		if leftroll == "SB1":
			leftcolumn = SB1.copy()
		if midroll == "SB1":
			midcolumn = SB1.copy()
		if rightroll == "SB1":
			rightcolumn = SB1.copy()
		if leftroll == "Blank7":
			leftcolumn = Blank7.copy()
		if midroll == "Blank7":
			midcolumn = Blank7.copy()
		if rightroll == "Blank7":
			rightcolumn = Blank7.copy()
		if leftroll == "DR7":
			leftcolumn = DR7.copy()
		if midroll == "DR7":
			midcolumn = DR7.copy()
		if rightroll == "DR7":
			rightcolumn = DR7.copy()
		if leftroll == "Blank8":
			leftcolumn = Blank8.copy()
		if midroll == "Blank8":
			midcolumn = Blank8.copy()
		if rightroll == "Blank8":
			rightcolumn = Blank8.copy()
		if leftroll == "B5":
			leftcolumn = B5.copy()
		if midroll == "B5":
			midcolumn = B5.copy()
		if rightroll == "B5":
			rightcolumn = B5.copy()
		if leftroll == "Blank9":
			leftcolumn = Blank9.copy()
		if midroll == "Blank9":
			midcolumn = Blank9.copy()
		if rightroll == "Blank9":
			rightcolumn = Blank9.copy()
		if leftroll == "DG7":
			leftcolumn = DG7.copy()
		if midroll == "DG7":
			midcolumn = DG7.copy()
		if rightroll == "DG7":
			rightcolumn = DG7.copy()
		if leftroll == "Blank10":
			leftcolumn = Blank10.copy()
		if midroll == "Blank10":
			midcolumn = Blank10.copy()
		if rightroll == "Blank10":
			rightcolumn = Blank10.copy()
		if leftroll == "SB2":
			leftcolumn = SB2.copy()
		if midroll == "SB2":
			midcolumn = SB2.copy()
		if rightroll == "SB2":
			rightcolumn = SB2.copy()
		if leftroll == "Blank11":
			leftcolumn = Blank11.copy()
		if midroll == "Blank11":
			midcolumn = Blank11.copy()
		if rightroll == "Blank11":
			rightcolumn = Blank11.copy()

		#Begin debug messages, remove when finished
		caller.msg("%(1)s   %(2)s   %(3)s" % {"1" : leftroll, "2" : midroll, "3" : rightroll})
		caller.msg(leftroll)
		caller.msg(midroll)
		caller.msg(rightroll)
		#end debug
		
		#Let's start working on PAYOUTS
		#Calculations all assume one bit paid in
		#For 2-3 bit plays, just multiply result by n
		
		if ((leftroll == "D5B" or leftroll == "DSB" or leftroll == "SB1" or leftroll == "SB2" or leftroll == "B5") and
			(midroll == "D5B" or midroll == "DSB" or midroll == "SB1" or midroll == "SB2" or midroll == "B5") and
			(rightroll == "D5B" or rightroll == "DSB" or rightroll == "SB1" or rightroll == "SB2" or rightroll == "B5")):
			payout = 5
		if leftroll == "SB1" or leftroll == "SB2" or leftroll == "DSB" and midroll == "SB1" or midroll == "SB2" or midroll == "DSB" and rightroll == "SB1" or rightroll == "SB2" or rightroll == "DSB":
			payout = 10
		
		#Display the roll to the player
		caller.msg("------------------------")
		caller.msg("$  %(1)s  |n$  %(2)s  |n$  %(3)s  |n$" % {"1" : leftcolumn["pos1"], "2" : midcolumn["pos1"], "3" : rightcolumn["pos1"]})
		caller.msg("$  %(1)s  |n$  %(2)s  |n$  %(3)s  |n$" % {"1" : leftcolumn["pos2"], "2" : midcolumn["pos2"], "3" : rightcolumn["pos2"]})
		caller.msg("$> %(1)s  |n$  %(2)s  |n$  %(3)s  |n$" % {"1" : leftcolumn["pos3"], "2" : midcolumn["pos3"], "3" : rightcolumn["pos3"]})
		caller.msg("$  %(1)s  |n$  %(2)s  |n$  %(3)s  |n$" % {"1" : leftcolumn["pos4"], "2" : midcolumn["pos4"], "3" : rightcolumn["pos4"]})
		caller.msg("$  %(1)s  |n$  %(2)s  |n$  %(3)s  |n$" % {"1" : leftcolumn["pos5"], "2" : midcolumn["pos5"], "3" : rightcolumn["pos5"]})
		
		#post payout
		if payout == 0:
			caller.msg("Sorry, you lose!")
		if payout > 0:
			caller.msg("You win! %i bits come tumbling out." % payout)
