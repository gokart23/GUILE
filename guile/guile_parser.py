from pyparsing import *
ws = ' \t'
ParserElement.setDefaultWhitespaceChars(ws)

# Token classes
GUI_START, GUI_END = Literal("%%"), Literal("%%")
NEWLINE = Literal("\n")
ASSIGN, COMMENT_HASH, SEMI, COLON, COMMA, FWD_SLASH, ASSOC = Literal("="), Literal("#"), Literal(";"), Literal(":"), Literal(","), Literal("/"), Literal("->")
OPENSQUARE, CLOSESQUARE, OPENPAREN, CLOSEPAREN = Literal("["), Literal("]"), Literal("("), Literal(")")
GTYPE = Literal("Textbox") | Literal("Button")

#Grammar rules
statement = Group ( ZeroOrMore ( Word(printables) ) + LineEnd() )
prologue = ZeroOrMore ( statement ).suppress()
epilogue = ZeroOrMore ( statement ).suppress()
comment = Suppress(COMMENT_HASH + statement) | LineEnd().suppress()

varname = Word(alphanums + "_")
varname_list = Group ( OneOrMore ( varname + Optional(COMMA).suppress() ) )
decl = Group ( GTYPE + COLON.suppress() + varname_list + LineEnd().suppress() )
decl_section = Group( ZeroOrMore ( decl | comment ) ).setResultsName("decl_section")

var_use = Forward()
comp_list = Forward()
operator = COMMA | FWD_SLASH
comp_list << (Group(var_use + operator + var_use) | Group(var_use + operator + OPENSQUARE.suppress() + comp_list + CLOSESQUARE.suppress()))
var_use << ( varname | OPENPAREN + comp_list + CLOSEPAREN )
composition = Group( var_use + ASSIGN.suppress() + OPENSQUARE.suppress() + comp_list + CLOSESQUARE.suppress() + LineEnd().suppress() )
composition_section = Group( ZeroOrMore ( composition | comment ) ).setResultsName("composition_section")

event_name = Literal("on_") + varname.setResultsName("event_name")
func_name = Word( alphanums + "_" )
association = var_use + ASSOC + func_name + Optional(COMMA)
chain = event_name + COLON + OneOrMore(association) + LineEnd() 
chaining_section = ZeroOrMore( chain | comment )

gui_section = decl_section + composition_section + chaining_section

