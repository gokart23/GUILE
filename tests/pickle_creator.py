import cPickle
from guile import guile_parser as gp

# Test case ground-truth creation (after manual checking)
f = open("tests/test_sample.txt", "r")
print "Test case name:"
t_name = raw_input().strip()
ab = gp.gui_section.parseString(f.read())
print ab.dump()
choice = raw_input().strip()
if choice.lower() == "y":
	with open("tests/pickles/"+t_name+".pkl","w+") as fn:
		cPickle.dump(ab, fn)
	print "Dumped " + t_name + ".pkl"
else:
	print "Skipped " + t_name + ".pkl"
f.close()

