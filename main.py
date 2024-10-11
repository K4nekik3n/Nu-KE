import os, sys, platform, subprocess, time, random
from Tools.TemplateWps import *

# -> Color palette <-
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
# -> Color palette <-

def autoWrites(txt, delay:float):
  for x in txt + '\n':
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(random.random() * delay)

def WebProjectSetup(dir):
  os.makedirs(dir, exist_ok=True)
  os.makedirs(f'{dir}/assets', exist_ok=True)
  with open(f'{dir}/index.html', 'w') as html_f:
    html_f.write(WPS.HTML)
  with open(f'{dir}/style.css', 'w') as css_f:
    css_f.write(WPS.CSS)
  with open(f'{dir}/script.js', 'w'): pass



def cmd_input(command:str):
  if command.lower() in ['clear', 'cls']:
    if platform.system() == "Windows":
      os.system('cls')
    else:
      os.system('clear')


  elif command.lower().startswith('cd'):
    if command.strip() == 'cd':
      dir = os.path.expanduser('~')
    else:
      dir = command.split('cd ')[1].strip()
    try:
      os.chdir(dir)
    except FileNotFoundError:
      print(f' Error : {Colors.LIGHT_RED}Directory not found{Colors.END}')

  elif command.lower().startswith('wsp '):
    dir_name = command.split(' ')[1]
    if dir_name:
      autoWrites(f'{Colors.LIGHT_WHITE}Loading...................................... {Colors.LIGHT_GREEN}Success!!{Colors.END}', 0.05)
      WebProjectSetup(dir_name)
    else:
      print('Error: n wsp(Web Setup Project) --name-folder')

def shell():
  while True:
    autoWrites(f'{Colors.LIGHT_WHITE} + {Colors.LIGHT_GRAY}----------{Colors.RED}{Colors.BLINK} Menu {Colors.END}{Colors.LIGHT_GRAY}----------{Colors.LIGHT_WHITE}\n{Colors.LIGHT_GRAY} | wsp : Web Setup Project\n |\n |\n + --------------------------\n', 0.06)
    cmd=input(f'{Colors.LIGHT_WHITE}{os.getcwd()} | : ')
    if cmd.lower() in ['quit', 'exit']:
      break
    cmd_input(cmd)


shell()