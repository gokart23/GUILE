##GUILE Grammar

###Grammar Rules

1. start: prologue GUI\_START gui\_section GUI\_END epilogue start | EPS
2. prologue: ([a-zA-Z0-9_])* NEWLINE
3. epilogue: ([a-zA-Z0-9_])* NEWINE
4. gui\_section: decl_section composition_section chaining_section
5. decl_section: decl decl_section | EPS
6. decl: GTYPE COLON varname_list
7. varname_list: varname COMMA varname_list | EPS
8. varname: ([a-zA-Z0-9_])+
9. composition_section: composition composition_section | EPS 
10. composition: OPENSQUARE comp_list CLOSESQUARE
11. comp_list: var_use operator var_use | var_use operator comp_list
12. var_use: varname | OPENPAREN comp_list CLOSEPAREN
13. operator: COMMA | FWD_SLASH
14. chaining_section: chain chaining_section | EPS
15. chain: event_name COLON association
16. event_name: "on_" varname
16. association: var_use ASSOC func_name

###Token Classes
1. GUI\_START "%%"
2. GUI\_END "%%"
3. NEWLINE "\n"
4. COLON ":"
5. COMMA ","
6. FWD_SLASH "/"
7. OPENSQUARE "["
8. CLOSESQUARE "]"
9. OPENPAREN "("
10. CLOSEPAREN ")"
11. GTYPE "Textbox"|"Button"
12. ASSOC "->"
