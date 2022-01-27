from random import randrange
from threading import Thread
import time

def is_number(x):
  try:
    int(x)
    return True
  except:
    return False

coreTemps = [300, 300, 300, 300] # Kelvin
coreFuels = [100, 100, 100, 100] # Remaining Percent
coreRods = [0, 0, 0, 0] # Raised Percent
coreOnline = [False, False, False, False]

money = 40 # Million USD
totalScore = 0 # Electricity Generated (MWh)

def attemptRodPercent(percent, core):
  if percent == coreRods[core-1]:
    print("Nothing has changed.")
  elif percent > coreRods[core-1]:
    print("Attempting to raise control rods of reactor " + str(core) + ".")
    time.sleep(randrange(1,3))
    coreRods[core-1] = percent
    print("Successfully raised control rods of reactor " + str(core) + " to " + str(percent) + "%.")
  else:
    print("Attempting to lower control rods of reactor " + str(core) + ".")
    time.sleep(randrange(1,3))
    if randrange(1500, coreTemps[core-1]) > 2000:
      print("Operation failed, control rods could not be lowered due to a malfunction caused by core temperature!")

def attemptShutdown(core):
  if core:
    print("Attempting to shutdown reactor " + str(core) + ".")

  else:
    print("Attempting to shutdown all reactors.")

print("Commands:\n  Help\n  Stats\n  Shutdown {1, 2, 3, 4}(Optional)\n  Rods {0-100} {1, 2, 3, 4}(Optional)")

while True:
  take = input("\nCommand: ").split(" ")
  
  parameter1 = None
  parameter2 = None
  
  if len(take) == 2:
    parameter1 = take[1]
  elif len(take) == 3:
    parameter1 = take[1]
    parameter2 = take[2]
  
  cmd = take[0]
  
  if cmd.lower() == "help":
    print("\nThis is a very simplified version of a generic fission reactor. Likely not realistic but oh well.")
    print("Uppercase/Lowercase does not matter for commands.")
    print("\nCommands:")
    print("  Stats: Shows important values.")
    print("\nValues you need to know:")
    print("\n  Core Temperatures: Current temperature of a Reactor Core. The reactor core will melt if it reaches 2800 Kelvin. Although, you should try to keep it below 2000 Kelvin to avoid any problems, as you might not be able to lower control rods past 2000 Kelvin. (%50 and less chance of success at/after 2500 Kelvin.)")
    print("\n  Core Fuel Percent: Percentage of fuel remaining inside a core. You need to replace them if they deplete. If fuel percentage of a core goes below 20% the efficiency of the core will decrease immensely.")
    print("\n To start producing electricity, try to raise control rods. This will allow fission to happen, which will in turn create heat and boil the water, making turbines spin.\n  Example: rods 100")
  elif cmd.lower() == "stats":
    for core in range(len(coreTemps)):
      print("\n  Core " + str(core+1) + " Temperature: " + str(coreTemps[core]) + " Kelvin")
      print("  Core " + str(core+1) + " Control Rods: " + str(coreRods[core]) + "% Raised")
    print("\n  Total Electricity Generated: " + str(totalScore) + " MWh")
  elif cmd.lower() == "shutdown":
    attemptShutdown(parameter1)
  elif cmd.lower() == "rods":
    if parameter2:
      if parameter2 in ["1", "2", "3", "4"]:
        if is_number(parameter1):
          if int(parameter1) >= 0 and int(parameter1) <= 100:
            attemptRodPercent(int(parameter1), int(parameter2))
          else:
            print("Invalid percentage: Must be between 0 and 100.")
        else:
          print("Invalid percentage: Must be a number.")
      else:
        print("Invalid core: Must be 1, 2, 3 or 4.")
    else:
      if is_number(parameter1):
        if int(parameter1) >= 0 and int(parameter1) <= 100:
          attemptRodPercent(int(parameter1), 1)
          time.sleep(1)
          attemptRodPercent(int(parameter1), 2)
          time.sleep(1)
          attemptRodPercent(int(parameter1), 3)
          time.sleep(1)
          attemptRodPercent(int(parameter1), 4)
        else:
          print("Invalid percentage: Must be between 0 and 100.")
      else:
        print("Invalid percentage: Must be a number.")
  else:
    print("\nUnknown command: " + cmd)
