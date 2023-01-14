
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftSUMSUBleftMULTDIVAND ATRIB COLON DEC DEDENT DIV DO ELIF ELSE ENDMARKER EQUIV GEQ GT ID IF INC INDENT INPUT INTDec LCPARENT LCURLBRACKET LEQ LSQBRACKET LT MOD MULT NEQ NEWLINE NOT NUM OR PRINT QUOTE RCPARENT RCURLBRACKET RSQBRACKET STRING SUB SUM WHILE WSProgramaInit : Programa ENDMARKERPrograma : CorpoPrograma : Decls CorpoCorpo : Proc NewlineCorpo : Corpo Proc NewlineCorpo : NewlineNewline : Newline : NEWLINEDedent : Dedent DEDENTDedent : Decls : Decl NewlineDecls : Decls Decl NewlineDecl : INTDec IDDecl : INTDec ID ATRIB NUMDecl : INTDec ID ATRIB InputDecl : INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValuesDecl : INTDec ID LSQBRACKET NUM RSQBRACKETArrayValues : LCURLBRACKET ArrayIntValues RCURLBRACKETArrayIntValues : ArrayIntValues ',' ExprArrayIntValues : ExprProc : AtribProc : PrintProc : IfProc : DoWhileIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo DedentIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENTDoWhile : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINECond : Expr GT ExprCond : Expr LT ExprCond : Expr GEQ ExprCond : Expr LEQ ExprCond : Expr EQUIV ExprCond : Expr NEQ ExprCond : Cond OR CondCond : Expr AND ExprCond : NOT CondAtrib : ID ATRIB ExprAtrib : ID ATRIB InputAtrib : ID LSQBRACKET Expr RSQBRACKET ATRIB ExprPrint : NonFormattedNonFormatted : PRINT LCPARENT Argument RCPARENTArgument : StringArgument : VarArgument : ExprExpr : VarExpr : NUMExpr : Expr SUM ExprExpr : Expr  SUB ExprExpr : Expr  MULT ExprExpr : Expr  DIV ExprExpr : Expr MOD ExprExpr : ID INCExpr : ID DECVar : IDVar    : ID LSQBRACKET Expr RSQBRACKETInput : INPUT LCPARENT String RCPARENTString : QUOTE STRING QUOTEString :  "
    
_lr_action_items = {'ID':([0,3,4,5,6,7,8,9,10,11,12,13,15,20,21,22,23,24,25,26,27,28,30,31,32,35,36,37,38,39,44,52,53,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,75,76,78,80,81,82,83,84,86,96,99,100,101,104,105,106,108,111,112,113,114,115,121,123,124,125,],[14,14,14,-7,-6,-7,-21,-22,-23,-24,-8,25,-40,-7,14,-7,-4,-11,-13,35,35,35,51,-5,-12,-54,-37,-38,-45,-46,35,-14,-15,-52,-53,35,35,35,35,35,35,35,35,35,35,35,35,35,35,14,-41,-17,-47,-48,-49,-50,-51,35,14,-55,-56,-39,-16,35,14,-9,14,35,-18,35,-25,-27,14,14,-26,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,31,32,35,36,37,38,39,52,53,55,56,75,76,78,80,81,82,83,84,96,99,100,101,104,106,108,111,113,115,121,123,124,125,],[16,16,16,-7,-6,-7,-21,-22,-23,-24,-8,-40,-7,16,-7,-4,-11,-13,-5,-12,-54,-37,-38,-45,-46,-14,-15,-52,-53,16,-41,-17,-47,-48,-49,-50,-51,16,-55,-56,-39,-16,16,-9,16,-18,-25,-27,16,16,-26,]),'DO':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,31,32,35,36,37,38,39,52,53,55,56,75,76,78,80,81,82,83,84,96,99,100,101,104,106,108,111,113,115,121,123,124,125,],[17,17,17,-7,-6,-7,-21,-22,-23,-24,-8,-40,-7,17,-7,-4,-11,-13,-5,-12,-54,-37,-38,-45,-46,-14,-15,-52,-53,17,-41,-17,-47,-48,-49,-50,-51,17,-55,-56,-39,-16,17,-9,17,-18,-25,-27,17,17,-26,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,31,32,35,36,37,38,39,52,53,55,56,75,76,78,80,81,82,83,84,96,99,100,101,104,106,108,111,113,115,121,123,124,125,],[18,18,18,-7,-6,-7,-21,-22,-23,-24,-8,-40,-7,18,-7,-4,-11,-13,-5,-12,-54,-37,-38,-45,-46,-14,-15,-52,-53,18,-41,-17,-47,-48,-49,-50,-51,18,-55,-56,-39,-16,18,-9,18,-18,-25,-27,18,18,-26,]),'ENDMARKER':([0,2,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,31,32,35,36,37,38,39,52,53,55,56,76,78,80,81,82,83,84,99,100,101,104,106,108,111,113,115,121,125,],[-7,19,-2,-7,-7,-6,-7,-21,-22,-23,-24,-8,-40,-7,-3,-7,-4,-11,-13,-5,-12,-54,-37,-38,-45,-46,-14,-15,-52,-53,-41,-17,-47,-48,-49,-50,-51,-55,-56,-39,-16,-7,-9,-10,-18,-25,-27,-26,]),'NEWLINE':([0,4,5,6,7,8,9,10,11,12,15,20,22,23,24,25,29,31,32,35,36,37,38,39,52,53,55,56,75,76,78,80,81,82,83,84,87,99,100,101,104,106,108,111,113,115,119,120,121,123,125,],[12,12,12,-6,12,-21,-22,-23,-24,-8,-40,12,12,-4,-11,-13,12,-5,-12,-54,-37,-38,-45,-46,-14,-15,-52,-53,12,-41,-17,-47,-48,-49,-50,-51,12,-55,-56,-39,-16,12,-9,-10,-18,-25,121,12,-27,12,-26,]),'INTDec':([0,4,7,12,22,24,25,32,52,53,78,100,104,113,],[13,13,-7,-8,-7,-11,-13,-12,-14,-15,-17,-56,-16,-18,]),'$end':([1,19,],[0,-1,]),'WHILE':([5,6,8,9,10,11,12,15,20,23,31,35,36,37,38,39,55,56,75,76,80,81,82,83,84,96,99,100,101,103,106,108,111,115,121,125,],[-7,-6,-21,-22,-23,-24,-8,-40,-7,-4,-5,-54,-37,-38,-45,-46,-52,-53,-7,-41,-47,-48,-49,-50,-51,-10,-55,-56,-39,107,-7,-9,-10,-25,-27,-26,]),'DEDENT':([5,6,8,9,10,11,12,15,20,23,31,35,36,37,38,39,55,56,75,76,80,81,82,83,84,96,99,100,101,103,106,108,111,115,121,123,124,125,],[-7,-6,-21,-22,-23,-24,-8,-40,-7,-4,-5,-54,-37,-38,-45,-46,-52,-53,-7,-41,-47,-48,-49,-50,-51,-10,-55,-56,-39,108,-7,-9,-10,108,-27,-7,125,-26,]),'ELSE':([5,6,8,9,10,11,12,15,20,23,31,35,36,37,38,39,55,56,76,80,81,82,83,84,99,100,101,106,108,111,115,121,125,],[-7,-6,-21,-22,-23,-24,-8,-40,-7,-4,-5,-54,-37,-38,-45,-46,-52,-53,-41,-47,-48,-49,-50,-51,-55,-56,-39,-7,-9,-10,118,-27,-26,]),'INDENT':([12,29,45,87,102,120,122,],[-8,-7,75,-7,106,-7,123,]),'ATRIB':([14,25,64,78,],[26,33,86,98,]),'LSQBRACKET':([14,25,35,51,],[27,34,57,57,]),'LCPARENT':([16,18,40,107,],[28,30,63,112,]),'COLON':([17,65,118,],[29,87,120,]),'NUM':([26,27,28,30,33,34,44,57,58,59,60,61,62,66,67,68,69,70,71,72,73,86,105,112,114,],[39,39,39,39,52,54,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'INPUT':([26,33,],[40,40,]),'NOT':([28,44,66,112,],[44,44,44,44,]),'QUOTE':([30,63,77,],[50,50,97,]),'RCPARENT':([30,35,38,39,42,46,47,48,49,51,55,56,63,74,80,81,82,83,84,85,88,89,90,91,92,93,94,95,97,99,116,],[-58,-54,-45,-46,65,76,-42,-43,-44,-54,-52,-53,-58,-36,-47,-48,-49,-50,-51,100,-34,-28,-29,-30,-31,-32,-33,-35,-57,-55,119,]),'INC':([35,51,],[55,55,]),'DEC':([35,51,],[56,56,]),'SUM':([35,36,38,39,41,43,48,49,51,55,56,79,80,81,82,83,84,89,90,91,92,93,94,95,99,101,110,117,],[-54,58,-45,-46,58,58,-45,58,-54,-52,-53,58,-47,-48,-49,-50,58,58,58,58,58,58,58,58,-55,58,58,58,]),'SUB':([35,36,38,39,41,43,48,49,51,55,56,79,80,81,82,83,84,89,90,91,92,93,94,95,99,101,110,117,],[-54,59,-45,-46,59,59,-45,59,-54,-52,-53,59,-47,-48,-49,-50,59,59,59,59,59,59,59,59,-55,59,59,59,]),'MULT':([35,36,38,39,41,43,48,49,51,55,56,79,80,81,82,83,84,89,90,91,92,93,94,95,99,101,110,117,],[-54,60,-45,-46,60,60,-45,60,-54,-52,-53,60,60,60,-49,-50,60,60,60,60,60,60,60,60,-55,60,60,60,]),'DIV':([35,36,38,39,41,43,48,49,51,55,56,79,80,81,82,83,84,89,90,91,92,93,94,95,99,101,110,117,],[-54,61,-45,-46,61,61,-45,61,-54,-52,-53,61,61,61,-49,-50,61,61,61,61,61,61,61,61,-55,61,61,61,]),'MOD':([35,36,38,39,41,43,48,49,51,55,56,79,80,81,82,83,84,89,90,91,92,93,94,95,99,101,110,117,],[-54,62,-45,-46,62,62,-45,62,-54,-52,-53,62,-47,-48,-49,-50,62,62,62,62,62,62,62,62,-55,62,62,62,]),'RSQBRACKET':([35,38,39,41,54,55,56,79,80,81,82,83,84,99,],[-54,-45,-46,64,78,-52,-53,99,-47,-48,-49,-50,-51,-55,]),'GT':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,67,-52,-53,-47,-48,-49,-50,-51,-55,]),'LT':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,68,-52,-53,-47,-48,-49,-50,-51,-55,]),'GEQ':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,69,-52,-53,-47,-48,-49,-50,-51,-55,]),'LEQ':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,70,-52,-53,-47,-48,-49,-50,-51,-55,]),'EQUIV':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,71,-52,-53,-47,-48,-49,-50,-51,-55,]),'NEQ':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,72,-52,-53,-47,-48,-49,-50,-51,-55,]),'AND':([35,38,39,43,55,56,80,81,82,83,84,99,],[-54,-45,-46,73,-52,-53,-47,-48,-49,-50,-51,-55,]),'OR':([35,38,39,42,55,56,74,80,81,82,83,84,88,89,90,91,92,93,94,95,99,116,],[-54,-45,-46,66,-52,-53,66,-47,-48,-49,-50,-51,66,-28,-29,-30,-31,-32,-33,-35,-55,66,]),'RCURLBRACKET':([35,38,39,55,56,80,81,82,83,84,99,109,110,117,],[-54,-45,-46,-52,-53,-47,-48,-49,-50,-51,-55,113,-20,-19,]),',':([35,38,39,55,56,80,81,82,83,84,99,109,110,117,],[-54,-45,-46,-52,-53,-47,-48,-49,-50,-51,-55,114,-20,-19,]),'STRING':([50,],[77,]),'LCURLBRACKET':([98,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ProgramaInit':([0,],[1,]),'Programa':([0,],[2,]),'Corpo':([0,4,75,106,123,],[3,21,96,111,124,]),'Decls':([0,],[4,]),'Proc':([0,3,4,21,75,96,106,111,123,124,],[5,20,5,20,5,20,5,20,5,20,]),'Newline':([0,4,5,7,20,22,29,75,87,106,120,123,],[6,6,23,24,31,32,45,6,102,6,122,6,]),'Decl':([0,4,],[7,22,]),'Atrib':([0,3,4,21,75,96,106,111,123,124,],[8,8,8,8,8,8,8,8,8,8,]),'Print':([0,3,4,21,75,96,106,111,123,124,],[9,9,9,9,9,9,9,9,9,9,]),'If':([0,3,4,21,75,96,106,111,123,124,],[10,10,10,10,10,10,10,10,10,10,]),'DoWhile':([0,3,4,21,75,96,106,111,123,124,],[11,11,11,11,11,11,11,11,11,11,]),'NonFormatted':([0,3,4,21,75,96,106,111,123,124,],[15,15,15,15,15,15,15,15,15,15,]),'Expr':([26,27,28,30,44,57,58,59,60,61,62,66,67,68,69,70,71,72,73,86,105,112,114,],[36,41,43,49,43,79,80,81,82,83,84,43,89,90,91,92,93,94,95,101,110,43,117,]),'Input':([26,33,],[37,53,]),'Var':([26,27,28,30,44,57,58,59,60,61,62,66,67,68,69,70,71,72,73,86,105,112,114,],[38,38,38,48,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'Cond':([28,44,66,112,],[42,74,88,116,]),'Argument':([30,],[46,]),'String':([30,63,],[47,85,]),'Dedent':([96,111,],[103,115,]),'ArrayValues':([98,],[104,]),'ArrayIntValues':([105,],[109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ProgramaInit","S'",1,None,None,None),
  ('ProgramaInit -> Programa ENDMARKER','ProgramaInit',2,'p_Programa_Init','yacc.py',7),
  ('Programa -> Corpo','Programa',1,'p_Programa','yacc.py',11),
  ('Programa -> Decls Corpo','Programa',2,'p_Programa_Decls','yacc.py',15),
  ('Corpo -> Proc Newline','Corpo',2,'p_Corpo','yacc.py',20),
  ('Corpo -> Corpo Proc Newline','Corpo',3,'p_Corpo_Proc','yacc.py',24),
  ('Corpo -> Newline','Corpo',1,'p_Corpo_Newline','yacc.py',28),
  ('Newline -> <empty>','Newline',0,'p_Newline_Empty','yacc.py',33),
  ('Newline -> NEWLINE','Newline',1,'p_Newline','yacc.py',37),
  ('Dedent -> Dedent DEDENT','Dedent',2,'p_Dedent_Rec','yacc.py',42),
  ('Dedent -> <empty>','Dedent',0,'p_Dedent_Empty','yacc.py',46),
  ('Decls -> Decl Newline','Decls',2,'p_Decls','yacc.py',51),
  ('Decls -> Decls Decl Newline','Decls',3,'p_Decls_Recursiva','yacc.py',55),
  ('Decl -> INTDec ID','Decl',2,'p_Decl_Int','yacc.py',59),
  ('Decl -> INTDec ID ATRIB NUM','Decl',4,'p_Decl_Int_Val','yacc.py',70),
  ('Decl -> INTDec ID ATRIB Input','Decl',4,'p_Decl_Int_Input','yacc.py',81),
  ('Decl -> INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValues','Decl',7,'p_Decl_Int_Array_Val','yacc.py',92),
  ('Decl -> INTDec ID LSQBRACKET NUM RSQBRACKET','Decl',5,'p_Decl_Int_Array','yacc.py',102),
  ('ArrayValues -> LCURLBRACKET ArrayIntValues RCURLBRACKET','ArrayValues',3,'p_ArrayValues','yacc.py',116),
  ('ArrayIntValues -> ArrayIntValues , Expr','ArrayIntValues',3,'p_ArrayIntValues_Rec','yacc.py',120),
  ('ArrayIntValues -> Expr','ArrayIntValues',1,'p_ArrayIntValues','yacc.py',125),
  ('Proc -> Atrib','Proc',1,'p_Proc_Atrib','yacc.py',131),
  ('Proc -> Print','Proc',1,'p_Proc_Print','yacc.py',135),
  ('Proc -> If','Proc',1,'p_Proc_If','yacc.py',139),
  ('Proc -> DoWhile','Proc',1,'p_DoWhile','yacc.py',143),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent','If',9,'p_If','yacc.py',149),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT','If',15,'p_If_Else','yacc.py',154),
  ('DoWhile -> DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE','DoWhile',11,'p_Do_While','yacc.py',160),
  ('Cond -> Expr GT Expr','Cond',3,'p_Cond_GT','yacc.py',165),
  ('Cond -> Expr LT Expr','Cond',3,'p_Cond_LT','yacc.py',169),
  ('Cond -> Expr GEQ Expr','Cond',3,'p_Cond_GEQ','yacc.py',173),
  ('Cond -> Expr LEQ Expr','Cond',3,'p_Cond_LEQ','yacc.py',177),
  ('Cond -> Expr EQUIV Expr','Cond',3,'p_Cond_EQUIV','yacc.py',181),
  ('Cond -> Expr NEQ Expr','Cond',3,'p_Cond_NEQ','yacc.py',185),
  ('Cond -> Cond OR Cond','Cond',3,'p_Cond_OR','yacc.py',189),
  ('Cond -> Expr AND Expr','Cond',3,'p_Cond_AND','yacc.py',193),
  ('Cond -> NOT Cond','Cond',2,'p_Cond_NOT','yacc.py',197),
  ('Atrib -> ID ATRIB Expr','Atrib',3,'p_Atrib_Expr','yacc.py',202),
  ('Atrib -> ID ATRIB Input','Atrib',3,'p_Atrib_Input','yacc.py',210),
  ('Atrib -> ID LSQBRACKET Expr RSQBRACKET ATRIB Expr','Atrib',6,'p_Atrib_Array','yacc.py',218),
  ('Print -> NonFormatted','Print',1,'p_Print_NonFormatted','yacc.py',238),
  ('NonFormatted -> PRINT LCPARENT Argument RCPARENT','NonFormatted',4,'p_NonFormatted','yacc.py',242),
  ('Argument -> String','Argument',1,'p_Argument_String','yacc.py',246),
  ('Argument -> Var','Argument',1,'p_Argument_Var','yacc.py',250),
  ('Argument -> Expr','Argument',1,'p_Argument_Expr','yacc.py',254),
  ('Expr -> Var','Expr',1,'p_Expr_Var','yacc.py',259),
  ('Expr -> NUM','Expr',1,'p_Expr_Num','yacc.py',263),
  ('Expr -> Expr SUM Expr','Expr',3,'p_Expr_Soma','yacc.py',267),
  ('Expr -> Expr SUB Expr','Expr',3,'p_Expr_Sub','yacc.py',271),
  ('Expr -> Expr MULT Expr','Expr',3,'p_Expr_Mult','yacc.py',275),
  ('Expr -> Expr DIV Expr','Expr',3,'p_Expr_Div','yacc.py',279),
  ('Expr -> Expr MOD Expr','Expr',3,'p_Expr_Mod','yacc.py',283),
  ('Expr -> ID INC','Expr',2,'p_Expr_Inc','yacc.py',287),
  ('Expr -> ID DEC','Expr',2,'p_Expr_Dec','yacc.py',291),
  ('Var -> ID','Var',1,'p_Var','yacc.py',296),
  ('Var -> ID LSQBRACKET Expr RSQBRACKET','Var',4,'p_Var_Array','yacc.py',308),
  ('Input -> INPUT LCPARENT String RCPARENT','Input',4,'p_Input','yacc.py',321),
  ('String -> QUOTE STRING QUOTE','String',3,'p_String','yacc.py',326),
  ('String -> <empty>','String',0,'p_String_Empty','yacc.py',330),
]
