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

print prologue.parseString("sdfasdf asdfasdf asdfsdf\nadsadasdf sdfasdf \n")

