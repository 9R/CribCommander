import subprocess
import config
import string

def gembird(action):
  command, plug = fixed_action(string.split(action, sep="-"))
  if command == "toggle":
    cmd = "-t"
    return sispmctl(cmd, plug)
  elif command == "on":
    cmd = "-o"
    return sispmctl(cmd, plug)
  elif command == "off":
    cmd = "-f"
    return sispmctl(cmd, plug)
  elif command == "status":
    cmd = "-g"
    return sispmctl(cmd, plug)
  elif command == "help":
    return "Help is on teh way"
  else:
    return "Unknown Command"

def fixed_action(action):
  if len(action) == 1:
    action.append("all")
  else:
    pass
  return action[0], action[1]

def sispmctl(cmd, plug=all):
  sis = subprocess.Popen(["/usr/bin/sispmctl", cmd, plug], stdout=subprocess.PIPE, universal_newlines=True)
  return sis.communicate()[0].replace("\n","<br>").replace("outlet 1",config.outlet_names[0]).replace("outlet 2",config.outlet_names[1]).replace("outlet 3",config.outlet_names[2]).replace("outlet 4",config.outlet_names[3])
