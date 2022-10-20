start Geometria

class Project:
	name = "HelloWorld"
	version = "0.1"
	cmd = "hellow"

# Description.

def hello():
	print(f"""

██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░  
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗  
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║  
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║  
██║░░██║███████╗███████╗███████╗╚█████╔╝  
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░  

░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║██║
░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║╚═╝
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝██╗
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝

(v{Project.version})

A library made for printing "Hello World"
into the screen!

To get started, run:

	"{Project.cmd} add"

to add this library to your game.

		""")

end_safezone()

def cmd(command):
	if command == "add":
		print("Adding to Geometria project...")