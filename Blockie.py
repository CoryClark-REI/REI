import Commands

'''
Assumptions

-The '-1' position is the default and where blocks are picked up or dropped off.
-The robot already knows how to move to the appropriate physical location when given a position to move to.
-The robot attempting to interact with conflicting positions is not fatal (For example, rm() on an exmpty slot), and would be avoided by user observation.
-The inidicator of "X" for the satus of a slot means there is one recognized block per slot. This means 1 + 1 = 1.
-The replay() command actually has a use. This may be an issue because of the assume 1 block per slot.
'''
command = raw_input('Begin by defining the number of rows (ex: size[3]):')
Commands.runLastCommand(command)