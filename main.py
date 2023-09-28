from renamescript import *
from context_menu import menus

fc = menus.FastCommand('Rename Files (Individually)', type='FILES', python=renamio)
fc.compile()
