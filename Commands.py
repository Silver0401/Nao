from state import state
from almath import TO_RAD 
import time

# ------------------------------------------------------------------ #
# Robot Specific Actions

def Talk():
	word = raw_input("que digo amo?")
	state["sentence"] = word
	return state["sentence"]

def LeftArmUp():
	state["ArticulationNames"] = ["LShoulderPitch", "LElbowRoll"]
	state["Angles"] = [-90.0*TO_RAD, -4.0*TO_RAD]
	state["ActionTime"] = [4,1]
	state["IsAbsolute"] = True	
	

def RightArmUp():
	state["ArticulationNames"] = ["RShoulderPitch", "RElbowRoll"]
	state["Angles"] = [-90.0*TO_RAD, 4.0*TO_RAD]
	state["ActionTime"] = [4,1]
	state["IsAbsolute"] = True


def ArmsUp():
	state["ArticulationNames"] = ["LShoulderPitch", "RShoulderPitch", "RElbowRoll", "LElbowRoll"]
	state["Angles"] = [-90.0*TO_RAD, -90.0*TO_RAD, 4.0*TO_RAD, -4.0*TO_RAD] 
	state["ActionTime"] = [4.0, 4.0, 1.0, 1.0]
	state["IsAbsolute"] = True		

def OpenArms():
	state["ArticulationNames"] = ["LShoulderRoll", "RShoulderRoll", "LElbowRoll", "RElbowRoll"]
	state["Angles"] = [75.0*TO_RAD, -75*TO_RAD, -2*TO_RAD, 2*TO_RAD]
	state["ActionTime"] = [2.0, 2.0, 1.0, 1.0]
	state["IsAbsolute"] = True	

def DiagonalArms():
	state["ArticulationNames"] = [

	"LShoulderPitch", "RShoulderPitch",
	 "LElbowRoll", "RElbowRoll",
	 "LShoulderRoll", "RShoulderRoll"]

	state["Angles"] = [

	-90.0*TO_RAD, -90.0*TO_RAD, 
	-2*TO_RAD, 2*TO_RAD,
	45*TO_RAD, -45*TO_RAD]

	state["ActionTime"] = [3.0, 3.0, 1.0, 1.0,1.5, 1.5]
	state["IsAbsolute"] = True


def Situp():
	state["ArticulationNames"] = [

	"LHipPitch", "RHipPitch",
	"LKneePitch","RKneePitch",
	"LAnklePitch", "RAnklePitch",
	"LShoulderPitch", "RShoulderPitch",
	"LElbowRoll","RElbowRoll",
	"LShoulderRoll", "RShoulderRoll", 
	"LElbowYaw", "RElbowYaw", 
	"LWristYaw", "RWristYaw"]

	state["Angles"] = [

	-41.2*TO_RAD, -41.2*TO_RAD, 
	65*TO_RAD,65*TO_RAD,
	-19.8*TO_RAD, -19.8*TO_RAD, 
	-10*TO_RAD, -10*TO_RAD,
	-2.2*TO_RAD, 2.2*TO_RAD,
	0, 0,
	0, 0, 
	0, 0]

	state["ActionTime"] = [

	4, 4, 4, 4, 4, 4, 4, 4,
	4, 4, 4, 4, 4, 4, 4, 4]

	state["IsAbsolute"] = True

def HandsBehindHead():
	state["ArticulationNames"] = [

	"LShoulderRoll", "RShoulderRoll",
	"LShoulderPitch", "RShoulderPitch",
	"LElbowYaw", "RElbowYaw",
	"LElbowRoll", "RElbowRoll",
	"LWristYaw", "RWristYaw"]

	state["Angles"] = [

	23*TO_RAD, -23*TO_RAD,
	-100*TO_RAD, -100*TO_RAD,
	-16.5*TO_RAD, 16.5*TO_RAD,
	-81.5*TO_RAD, 81.5*TO_RAD,
	0, 0]

	state["ActionTime"] = [

	1.5, 1.5, 3.5, 3.5, 1.0, 
	1.0, 1.5, 1.5, 1.0, 1.0]

	state["IsAbsolute"] = True

def LeftHandFace():
	state["ArticulationNames"] = [

	"LShoulderRoll","LWristYaw",
	"LElbowRoll","LElbowYaw","LShoulderPitch"]

	state["Angles"] = [

	23*TO_RAD,-104.4*TO_RAD,
	-82*TO_RAD,1*TO_RAD,-54*TO_RAD]

	state["ActionTime"] = [1.5, 1.0, 1.5, 1.0, 2.0]
	state["IsAbsolute"] = True

def RightHandFace():
	state["ArticulationNames"] = [

	"RShoulderRoll","RWristYaw",
	"RElbowRoll","RElbowYaw","RShoulderPitch"]

	state["Angles"] = [

	-23*TO_RAD,104.4*TO_RAD,
	82*TO_RAD,-1*TO_RAD,-54*TO_RAD]

	state["ActionTime"] = [1.5, 1.0, 1.5, 1.0, 2.0]
	state["IsAbsolute"] = True

def HandsFace():
	state["ArticulationNames"] = [

	"LShoulderRoll", "RShoulderRoll",
	"LWristYaw", "RWristYaw",
	"LElbowRoll", "RElbowRoll",
	"LElbowYaw", "RElbowYaw",
	"LShoulderPitch", "RShoulderPitch"]

	state["Angles"] = [

	23*TO_RAD, -23*TO_RAD, -104.4*TO_RAD, 104.4*TO_RAD,
	-82*TO_RAD, 82*TO_RAD, 1*TO_RAD, -1*TO_RAD, -54*TO_RAD, -54*TO_RAD]

	state["ActionTime"] = [1.5, 1.5, 1.0, 1.0, 1.5, 1.5, 1.0, 1.0, 2.0, 2.0]
	state["IsAbsolute"] = True

	

# ------------------------------------------------------------------ #




