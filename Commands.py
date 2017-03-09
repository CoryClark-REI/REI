import RobotInterface

rows = [];
command = "";
history = [];

def size(size):
	global rows 
	rows = [0] * size

def add(pos):
	rows[pos] = 1
	RobotInterface.open()
	RobotInterface.reset()
	RobotInterface.close()
	RobotInterface.moveToPosition(pos)
	RobotInterface.open()

def rm(pos):
	rows[pos] = 0
	RobotInterface.open()
	RobotInterface.moveToPosition(pos)
	RobotInterface.close()
	RobotInterface.reset()
	RobotInterface.open()

def mv(moveFrom, moveTo):
	rows[moveFrom] = 0
	rows[moveTo] = 1

	RobotInterface.open()
	RobotInterface.moveToPosition(moveFrom)
	RobotInterface.close()
	RobotInterface.moveToPosition(moveTo)
	RobotInterface.open()

def replay(last):
	runLastCommand(last)

def printRows():
	for x in enumerate(rows):
		pos = x[0]
		val = x[1]
		string = str(pos) + ": "
		if val == 1:
			string = string + 'X'
		print(string)

def getArg(string):
	return string[string.index('[')+1:string.index(']')]

def getArgs(string):
	combined = getArg(string)
	combined.replace(" ", "")
	print(combined)
	first = combined[0:combined.index(',')]
	second = combined[combined.index(',')+1:len(combined)]
	return (first, second)

def waitForInput():
	global command
	global history

	command = raw_input(":")
	runLastCommand(command)

def undo(toUndo):
	print(toUndo)
	if toUndo.startswith("add["):
		arg = int(getArg(toUndo))
		rm(arg)
		printRows()
		waitForInput()
	elif toUndo.startswith("rm["):
		arg = asInt(getArg(toUndo))
		add(arg)
		printRows()
		waitForInput()
	elif toUndo.startswith("mv["):
		arg = getArgs(toUndo)
		mv(asInt(arg[1]), asInt(arg[0]))
		printRows()
		waitForInput()


def asInt(object):
	try:
		return int(object)
	except TypeError:
		print("Invalid Argument")
		waitForInput()

def runLastCommand(lastCommand):
	global command
	global history

	history = history + [lastCommand]
	command = lastCommand
	if (command.startswith("size[") and command.endswith("]")):
		arg = asInt(getArg(command))
		size(arg)
		printRows()
		waitForInput()
	elif len(rows) <= 0:
		print("You must start with the size[x] command")
		waitForInput()
	elif (command.startswith("add[") and command.endswith("]")):
		arg = asInt(getArg(command))
		add(arg)
		printRows()
		waitForInput()
	elif command.startswith("mv["):
		arg = getArgs(command)
		mv(asInt(arg[0]), asInt(arg[1]))
		printRows()
		waitForInput()
	elif (command.startswith("rm[") and command.endswith("]")):
		arg = asInt(getArg(command))
		rm(arg)
		printRows()
		waitForInput()
	elif (command.startswith("replay") and history[len(history)] != "replay"):
		command = history[len(history)]
		runLastCommand(command)
	elif command.startswith("undo["):
		arg = asInt(getArg(command))
		i = 1
		while arg >= i :
			print(i)
			undo(history[len(history) - i - 1])
			i+=1
		printRows()
		waitForInput()
	elif (command == "exit"):
		pass
	else :
		print("Command not recognized")
		waitForInput()