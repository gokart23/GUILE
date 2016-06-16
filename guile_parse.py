from pyparsing import *

# Token classes
GUI_START, GUI_END = Literal("%%"), Literal("%%")
NEWLINE = Literal("\n")
COLON, COMMA, FWD_SLASH, ASSOC = Literal(":"), Literal(","), Literal("/"), Literal("->")
OPENSQUARE, CLOSESQUARE, OPENPAREN, CLOSEPAREN = Literal("["), Literal("]"), Literal("("), Literal(")")
GTYPE = Literal("Textbox") | Literal("Button")

#Grammar rules
statement = Group ( ZeroOrMore ( Word(alphanums) | "_" | " " ) + LineEnd() )
prologue = ZeroOrMore ( statement ).suppress()
epilogue = ZeroOrMore ( statement ).suppress()

varname = Word(alphanums + "_")
varname_list = Group ( OneOrMore ( varname + Optional(COMMA).suppress() ) )
decl = GTYPE + COLON + varname_list + LineEnd().suppress()
decl_section = Group( ZeroOrMore ( decl ) ).setResultsName("decl_section")

var_use = Forward()
comp_list = Forward()
operator = COMMA | FWD_SLASH
comp_list << ((var_use + operator + var_use) | (var_use + operator + comp_list))
var_use << ( varname | OPENPAREN + comp_list + CLOSEPAREN )
composition = OPENSQUARE + comp_list + CLOSESQUARE + LineEnd()
composition_section = ZeroOrMore ( composition )

event_name = Literal("on_") + varname.setResultsName("event_name")
func_name = Word( alphanums + "_" )
association = var_use + ASSOC + func_name + Optional(COMMA)
chain = event_name + COLON + OneOrMore(association) + LineEnd() 
chaining_section = ZeroOrMore( chain )

gui_section = decl_section + composition_section + chaining_section
abc = Group( ZeroOrMore( statement ) )

#Testing
p = raw_input()
p += raw_input()
ab = decl.parseString(p)
print ab.dump()

