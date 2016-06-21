from guile import guile_parser as gp

#Testing
f = open("sample", "r")
ab = gp.gui_section.parseString(f.read())
print ab.dump()
f.close()

