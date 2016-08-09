"""
Casino games for the casinos.

Mostly written as an experiment for myself to learn more with.
"""

from evennia import Command as BaseCommand
from evennia import default_cmds
import random
from evennia.utils import evtable

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
		
		if self.args == "payouts":
			payouttable = evtable.EvTable("", "No Doubles", "One Double", "Two Doubles", "Three Doubles",
										table=[["Any 3", "Any 3 Bars", "3 Single Bars", "3 Double Bars",
										"Any 7s", "3 Green 7s", "3 Blue 7s", "3 Red 7s"], ["2", "5",
										"10", "20", "20", "40", "100", "200"],
										["4", "10", "20", "40", "40", "80", "200", "400"],
										["8", "20", "40", "80", "80", "160", "400", "800"],
										["16", "40", "80", "160", "160", "320", "400", "2500"]],
										border="cells")
			caller.msg(payouttable)
		else:
	
			#Translation:
			#B7: Blue 7
			#D5B: Double 5 bar
			#R7: Red 7
			#G7: Green 7
			#DB7: Double Blue 7
			#SB1: Single Bar
			#DR7: Double Red 7
			#B5: Five Bar
			#DG7: Double Green 7
			#SB2: Single Bar
			
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
			
			#declaring payout calculations
			numB7 = 0
			numG7 = 0
			numR7 = 0
			double7 = 0
			numBlank= 0
			numSingleBar = 0
			numFiveBar = 0	
			doubleBar = 0

			#Remember what I said about being dumb as fuck?
			#Hey-o!
			#This builds the columns. Again, got to be a better way, because this is fucking DUMB.
			if leftroll == "B7":
				leftcolumn = B7.copy()
				numB7 += 1
			if midroll == "B7":
				midcolumn = B7.copy()
				numB7 += 1
			if rightroll == "B7":
				rightcolumn = B7.copy()
				numB7 += 1
			if leftroll == "Blank1":
				leftcolumn = Blank1.copy()
				numBlank += 1
			if midroll == "Blank1":
				midcolumn = Blank1.copy()
				numBlank += 1
			if rightroll == "Blank1":
				rightcolumn = Blank1.copy()
				numBlank += 1
			if leftroll == "D5B":
				leftcolumn = D5B.copy()
				numFiveBar += 1
				doubleBar += 1
			if midroll == "D5B":
				midcolumn = D5B.copy()
				numFiveBar += 1
				doubleBar += 1
			if rightroll == "D5B":
				rightcolumn = D5B.copy()
				numFiveBar += 1
				doubleBar += 1
			if leftroll == "Blank2":
				leftcolumn = Blank2.copy()
				numBlank += 1
			if midroll == "Blank2":
				midcolumn = Blank2.copy()
				numBlank += 1
			if rightroll == "Blank2":
				rightcolumn = Blank2.copy()
				numBlank += 1
			if leftroll == "R7":
				leftcolumn = R7.copy()
				numR7 += 1
			if midroll == "R7":
				midcolumn = R7.copy()
				numR7 += 1
			if rightroll == "R7":
				rightcolumn = R7.copy()
				numR7 += 1
			if leftroll == "Blank3":
				leftcolumn = Blank3.copy()
				numBlank += 1
			if midroll == "Blank3":
				midcolumn = Blank3.copy()
				numBlank += 1
			if rightroll == "Blank3":
				rightcolumn = Blank3.copy()
				numBlank += 1
			if leftroll == "DSB":
				leftcolumn = DSB.copy()
				numSingleBar += 1
				doubleBar += 1
			if midroll == "DSB":
				midcolumn = DSB.copy()
				numSingleBar += 1
				doubleBar += 1
			if rightroll == "DSB":
				rightcolumn = DSB.copy()
				numSingleBar += 1
				doubleBar += 1
			if leftroll == "Blank4":
				leftcolumn = Blank4.copy()
				numBlank += 1
			if midroll == "Blank4":
				midcolumn = Blank4.copy()
				numBlank += 1
			if rightroll == "Blank4":
				rightcolumn = Blank4.copy()
				numBlank += 1
			if leftroll == "G7":
				leftcolumn = G7.copy()
				numG7 += 1
			if midroll == "G7":
				midcolumn = G7.copy()
				numG7 += 1
			if rightroll == "G7":
				rightcolumn = G7.copy()
				numG7 += 1
			if leftroll == "Blank5":
				leftcolumn = Blank5.copy()
				numBlank += 1
			if midroll == "Blank5":
				midcolumn = Blank5.copy()
				numBlank += 1
			if rightroll == "Blank5":
				rightcolumn = Blank5.copy()
				numBlank += 1
			if leftroll == "DB7":
				leftcolumn = DB7.copy()
				numB7 += 1
				double7 += 1
			if midroll == "DB7":
				midcolumn = DB7.copy()
				numB7 += 1
				double7 += 1
			if rightroll == "DB7":
				rightcolumn = DB7.copy()
				numB7 += 1
				double7 += 1
			if leftroll == "Blank6":
				leftcolumn = Blank6.copy()
				numBlank += 1
			if midroll == "Blank6":
				midcolumn = Blank6.copy()
				numBlank += 1
			if rightroll == "Blank6":
				rightcolumn = Blank6.copy()
				numBlank += 1
			if leftroll == "SB1":
				leftcolumn = SB1.copy()
				numSingleBar += 1
			if midroll == "SB1":
				midcolumn = SB1.copy()
				numSingleBar += 1
			if rightroll == "SB1":
				rightcolumn = SB1.copy()
				numSingleBar += 1
			if leftroll == "Blank7":
				leftcolumn = Blank7.copy()
				numBlank += 1
			if midroll == "Blank7":
				midcolumn = Blank7.copy()
				numBlank += 1
			if rightroll == "Blank7":
				rightcolumn = Blank7.copy()
				numBlank += 1
			if leftroll == "DR7":
				leftcolumn = DR7.copy()
				double7 += 1
				numR7 += 1
			if midroll == "DR7":
				midcolumn = DR7.copy()
				double7 += 1
				numR7 += 1
			if rightroll == "DR7":
				rightcolumn = DR7.copy()
				double7 += 1
				numR7 += 1
			if leftroll == "Blank8":
				leftcolumn = Blank8.copy()
				numBlank += 1
			if midroll == "Blank8":
				midcolumn = Blank8.copy()
				numBlank += 1
			if rightroll == "Blank8":
				rightcolumn = Blank8.copy()
				numBlank += 1
			if leftroll == "B5":
				leftcolumn = B5.copy()
				numFiveBar += 1
			if midroll == "B5":
				midcolumn = B5.copy()
				numFiveBar += 1
			if rightroll == "B5":
				rightcolumn = B5.copy()
				numFiveBar += 1
			if leftroll == "Blank9":
				leftcolumn = Blank9.copy()
				numBlank += 1
			if midroll == "Blank9":
				midcolumn = Blank9.copy()
				numBlank += 1
			if rightroll == "Blank9":
				rightcolumn = Blank9.copy()
				numBlank += 1
			if leftroll == "DG7":
				leftcolumn = DG7.copy()
				double7 += 1
				numG7 += 1
			if midroll == "DG7":
				midcolumn = DG7.copy()
				double7 += 1
				numG7 += 1
			if rightroll == "DG7":
				rightcolumn = DG7.copy()
				double7 += 1
				numG7 += 1
			if leftroll == "Blank10":
				leftcolumn = Blank10.copy()
				numBlank += 1
			if midroll == "Blank10":
				midcolumn = Blank10.copy()
				numBlank += 1
			if rightroll == "Blank10":
				rightcolumn = Blank10.copy()
				numBlank += 1
			if leftroll == "SB2":
				leftcolumn = SB2.copy()
				numSingleBar += 1
			if midroll == "SB2":
				midcolumn = SB2.copy()
				numSingleBar += 1
			if rightroll == "SB2":
				rightcolumn = SB2.copy()
				numSingleBar += 1
			if leftroll == "Blank11":
				leftcolumn = Blank11.copy()
				numBlank += 1
			if midroll == "Blank11":
				midcolumn = Blank11.copy()
				numBlank += 1
			if rightroll == "Blank11":
				rightcolumn = Blank11.copy()
				numBlank += 1

			#Let's start working on PAYOUTS
			#Calculations all assume one bit paid in
			#For 2-3 bit plays, just multiply result by n
			
			#Three of anything
			if numBlank == 0:
				payout = 2
				if (doubleBar + double7) == 1:
					payout = 4
				if (doubleBar + double7) == 2:
					payout = 8
				if (doubleBar + double7) == 3:
					payout = 16
			#Three of any bar
			if (numSingleBar + numFiveBar) == 3:
				payout = 5
				if doubleBar == 1:
					payout = 10
				if doubleBar == 2:
					payout = 20
				if doubleBar == 3:
					payout = 40
			#Three single bars
			if numSingleBar == 3:
				payout = 10
				if doubleBar == 1:
					payout = 20
				if doubleBar == 2:
					payout = 40
				if doubleBar == 3:
					payout = 80
			#Three five bars
			if numFiveBar == 3:
				payout = 20
				if doubleBar == 1:
					payout = 40
				if doubleBar == 2:
					payout = 80
				if doubleBar == 3:
					payout = 160
			#Three of any 7s
			if (numB7 + numG7 + numR7) == 3:
				payout = 20
				if double7 == 1:
					payout = 40
				if double7 == 2:
					payout = 80
				if double7 == 3:
					payout = 160
			#Three green 7
			if numG7 == 3:
				payout = 40
				if double7 == 1:
					payout = 80
				if double7 == 2:
					payout = 160
				if double7 == 3:
					payout = 320
			#Three blue 7
			if numB7 == 3:
				payout = 100
				if double7 == 1:
					payout = 200
				if double7 == 2:
					payout = 400
				if double7 == 3:
					payout = 800
			#Three red 7
			if numR7 == 3:
				payout = 200
				if double7 == 1:
					payout = 400
				if double7 == 2:
					payout = 800
				#Jackpot
				if double7 == 3:
					payout = 2500
					
			slots = evtable.EvTable(table=[["", "", ">", "", ""],
									[leftcolumn["pos1"], leftcolumn["pos2"], leftcolumn["pos3"], leftcolumn["pos4"], leftcolumn["pos5"]],
									[midcolumn["pos1"], midcolumn["pos2"], midcolumn["pos3"], midcolumn["pos4"], midcolumn["pos5"]],
									[rightcolumn["pos1"], rightcolumn["pos2"], rightcolumn["pos3"], rightcolumn["pos4"], rightcolumn["pos5"]]],
									border="cells")
			slots.reformat(width=24, align="c")
			
			caller.msg('{:-^24}'.format("SLOTS"))
			caller.msg(slots)
			
			#post payout
			if payout == 0:
				caller.msg("Sorry, you lose!")
			if payout > 0 and payout < 2500:
				caller.msg("You win! %i bits come tumbling out." % payout)
			if payout >=2500:
				caller.msg("JACKPOT! A massive number of bits start pouring out, totaling %i!" % payout)
