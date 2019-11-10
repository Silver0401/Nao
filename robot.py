#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import argparse
import time
import almath
import Commands
import sys
from state import state


class NaoRobot():
	def __init__(self, session, topic_path, faceSize):
	# Robot_Initializers/Init Basics

		self.motion_service  = session.service("ALMotion")
		self.posture_service = session.service("ALRobotPosture")
		self.tracker_service = session.service("ALTracker")
		self.memory_service = session.service("ALMemory")
		self.face_detection = session.service("ALFaceDetection")
		self.talk = session.service("ALTextToSpeech")

		self.path = topic_path
		self.ALDialog = session.service("ALDialog")
		self.ALDialog.setLanguage(state["RobotLanguage"])

		self.targetName = "Face"
		self.FaceWidth = faceSize
		self.tracker_service.registerTarget(self.targetName, self.FaceWidth)


		self.motion_service.wakeUp()


	# ------------------------------------------------------------------ #
	# Robot Actions

	def Autonomous(self):

		self.posture_service.goToPosture("Stand",state["PostureSpeed"])

		self.topf_path = self.path.decode('utf-8')
		self.topic_name = self.ALDialog.loadTopic(self.topf_path.encode('utf-8'))
		self.ALDialog.activateTopic(self.topic_name)
		self.ALDialog.subscribe('text2.top')

		self.tracker_service.track(self.targetName)

		try:
			raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
		finally:

			# Stop the dialog engine
			self.ALDialog.unsubscribe('text2.top')
			self.ALDialog.deactivateTopic(self.topic_name)
			self.ALDialog.unloadTopic(self.topic_name)

			# Stop the tracker

			self.tracker_service.stopTracker()
			self.tracker_service.unregisterAllTargets()
			self.motion_service.rest()

	
	def Teleoperated(self):
		while True:

			state["robot"] = raw_input("What should I do master?: ")

			if state["robot"] == "Exit":
				sys.exit(1)
			elif state["robot"] == "ExitAndRest":
				self.motion_service.rest()
				sys.exit(1)
			elif state["robot"] == "Rest":
				self.motion_service.rest()
			elif state["robot"] == "Stand":
				self.posture_service.goToPosture(state["robot"],state["PostureSpeed"])
			elif state["robot"] == "StandInit":
				self.posture_service.goToPosture(state["robot"],state["PostureSpeed"])
			elif state["robot"] == "StandZero":
				self.posture_service.goToPosture(state["robot"],state["PostureSpeed"])
			
			elif state["robot"] == "Talk":
				self.talk.say(Commands.Talk())
			elif state["robot"] == "LeftArmUp":
				Commands.LeftArmUp()
				self.motion_service.goToPosture(state["robot"],state["PostureSpeed"])
			elif state["robot"] == "RightArmUP":
				Commands.RightArmUP()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "ArmsUp":
				Commands.ArmsUp()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "OpenArms":
				Commands.OpenArms()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "DiagonalArms":
				Commands.DiagonalArms()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "HandsBehindHead":
				Commands.HandsBehindHead()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "LeftHandFace":
				Commands.LeftHandFace()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "RightHandFace":
				Commands.RightHandFace()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "HandsFace":
				Commands.HandsFace()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "Situp":
				Commands.Situp()
				self.motion_service.angleInterpolation(state["ArticulationNames"],state["Angles"],state["ActionTime"],state["IsAbsolute"])
			elif state["robot"] == "Autonomous":
				NAO.Autonomous()





# ------------------------------------------------------------------ #
# Declaration of Main Document

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default=state["Adress"],
						help="Robot IP address. On robot or Local Naoqi: use 192.168.1.101")
	parser.add_argument("--port", type=int, default=9559,
						help="Naoqi port number")
	parser.add_argument("--topic-path", type=str, default=state["PathToTextFile"],
						help="absolute path of the dialog topic file (on the robot)")
	parser.add_argument("--facesize", type=float, default=0.1,
						help="Face width.")

	# parser.add_argument("--topic-path", type=str, required=True,
	args = parser.parse_args()
	session = qi.Session()
	try:
		session.connect("tcp://" + args.ip + ":" + str(args.port))
	except RuntimeError:
		print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
			   "Please check your script arguments. Run with -h option for help.")
		sys.exit(1)
	NAO = NaoRobot(session, args.topic_path, args.facesize) 
	NAO.Teleoperated()
