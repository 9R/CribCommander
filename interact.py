import subprocess
import config
import string

d = { 'toggle': '-t',
      'on': '-o',
      'off':'-f',
      'status':'-g'
}

def gembird(action):
  command, plug = fixed_action(string.split(action, sep="-"))
  if command in d:
    return sispmctl(d[command], plug)
  elif command == help:
    return 'Help is comming soon way'
  else:
    return 'Unknown command!'

def fixed_action(action):
  if len(action) == 1:
    action.append("all")
  else:
    pass
  return action[0], action[1]

def sispmctl(cmd, plug=all):
  sis = subprocess.Popen(["/usr/bin/sispmctl", cmd, plug], stdout=subprocess.PIPE, universal_newlines=True)
  return sis.communicate()[0].replace("\n","<br>").replace("outlet 1",config.outlet_names[0]).replace("outlet 2",config.outlet_names[1]).replace("outlet 3",config.outlet_names[2]).replace("outlet 4",config.outlet_names[3])
