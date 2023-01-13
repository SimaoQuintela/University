
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMSUBleftMULTDIVAND ATRIB COLON DEC DEDENT DIV DO ELIF ELSE ENDMARKER EQUIV GEQ GT ID IF INC INDENT INPUT INTDec LCPARENT LEQ LSQBRACKET LT MOD MULT NEQ NEWLINE NOT NUM OR PRINT QUOTE RCPARENT RSQBRACKET STRING SUB SUM WHILE WSProgramaInit : Programa ENDMARKERPrograma : CorpoPrograma : Decls CorpoCorpo : Proc NewlineCorpo : Corpo Proc NewlineCorpo : NewlineNewline : Newline : NEWLINEDedent : Dedent DEDENTDedent : Decls : Decl NewlineDecls : Decls Decl NewlineDecl : INTDec IDDecl : INTDec ID ATRIB NUMDecl : INTDec ID ATRIB InputProc : AtribProc : PrintProc : IfProc : DoWhileIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo DedentIf : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENTDoWhile : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINECond : Expr GT ExprCond : Expr LT ExprCond : Expr GEQ ExprCond : Expr LEQ ExprCond : Expr EQUIV ExprCond : Expr NEQ ExprCond : Cond OR CondCond : Expr AND ExprCond : NOT CondAtrib : ID ATRIB ExprAtrib : ID ATRIB InputPrint : NonFormattedNonFormatted : PRINT LCPARENT Argument RCPARENTArgument : StringArgument : VarArgument : ExprExpr : VarExpr : NUMExpr : Expr SUM ExprExpr : Expr  SUB ExprExpr : Expr  MULT ExprExpr : Expr  DIV ExprExpr : Expr MOD ExprExpr : ID INCExpr : ID DECVar : IDInput : INPUT LCPARENT String RCPARENTString : QUOTE STRING QUOTEString :  '
    
_lr_action_items = {'ID':([0,3,4,5,6,7,8,9,10,11,12,13,15,20,21,22,23,24,25,26,27,29,30,31,33,34,35,36,37,41,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,66,67,69,70,72,73,74,75,76,87,89,92,94,95,96,97,102,104,105,106,],[14,14,14,-7,-6,-7,-16,-17,-18,-19,-8,25,-34,-7,14,-7,-4,-11,-13,33,33,48,-5,-12,-48,-32,-33,-39,-40,33,-14,-15,-46,-47,33,33,33,33,33,33,33,33,33,33,33,33,33,14,-35,-41,-42,-43,-44,-45,14,-49,14,-9,14,33,-20,-22,14,14,-21,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,30,31,33,34,35,36,37,49,50,51,52,69,70,72,73,74,75,76,87,89,92,94,95,97,102,104,105,106,],[16,16,16,-7,-6,-7,-16,-17,-18,-19,-8,-34,-7,16,-7,-4,-11,-13,-5,-12,-48,-32,-33,-39,-40,-14,-15,-46,-47,16,-35,-41,-42,-43,-44,-45,16,-49,16,-9,16,-20,-22,16,16,-21,]),'DO':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,30,31,33,34,35,36,37,49,50,51,52,69,70,72,73,74,75,76,87,89,92,94,95,97,102,104,105,106,],[17,17,17,-7,-6,-7,-16,-17,-18,-19,-8,-34,-7,17,-7,-4,-11,-13,-5,-12,-48,-32,-33,-39,-40,-14,-15,-46,-47,17,-35,-41,-42,-43,-44,-45,17,-49,17,-9,17,-20,-22,17,17,-21,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,30,31,33,34,35,36,37,49,50,51,52,69,70,72,73,74,75,76,87,89,92,94,95,97,102,104,105,106,],[18,18,18,-7,-6,-7,-16,-17,-18,-19,-8,-34,-7,18,-7,-4,-11,-13,-5,-12,-48,-32,-33,-39,-40,-14,-15,-46,-47,18,-35,-41,-42,-43,-44,-45,18,-49,18,-9,18,-20,-22,18,18,-21,]),'ENDMARKER':([0,2,3,4,5,6,7,8,9,10,11,12,15,20,21,22,23,24,25,30,31,33,34,35,36,37,49,50,51,52,70,72,73,74,75,76,89,92,94,95,97,102,106,],[-7,19,-2,-7,-7,-6,-7,-16,-17,-18,-19,-8,-34,-7,-3,-7,-4,-11,-13,-5,-12,-48,-32,-33,-39,-40,-14,-15,-46,-47,-35,-41,-42,-43,-44,-45,-49,-7,-9,-10,-20,-22,-21,]),'NEWLINE':([0,4,5,6,7,8,9,10,11,12,15,20,22,23,24,25,28,30,31,33,34,35,36,37,49,50,51,52,69,70,72,73,74,75,76,78,89,92,94,95,97,100,101,102,104,106,],[12,12,12,-6,12,-16,-17,-18,-19,-8,-34,12,12,-4,-11,-13,12,-5,-12,-48,-32,-33,-39,-40,-14,-15,-46,-47,12,-35,-41,-42,-43,-44,-45,12,-49,12,-9,-10,-20,102,12,-22,12,-21,]),'INTDec':([0,4,7,12,22,24,25,31,49,50,89,],[13,13,-7,-8,-7,-11,-13,-12,-14,-15,-49,]),'$end':([1,19,],[0,-1,]),'WHILE':([5,6,8,9,10,11,12,15,20,23,30,33,34,35,36,37,51,52,69,70,72,73,74,75,76,87,89,91,92,94,95,97,102,106,],[-7,-6,-16,-17,-18,-19,-8,-34,-7,-4,-5,-48,-32,-33,-39,-40,-46,-47,-7,-35,-41,-42,-43,-44,-45,-10,-49,93,-7,-9,-10,-20,-22,-21,]),'DEDENT':([5,6,8,9,10,11,12,15,20,23,30,33,34,35,36,37,51,52,69,70,72,73,74,75,76,87,89,91,92,94,95,97,102,104,105,106,],[-7,-6,-16,-17,-18,-19,-8,-34,-7,-4,-5,-48,-32,-33,-39,-40,-46,-47,-7,-35,-41,-42,-43,-44,-45,-10,-49,94,-7,-9,-10,94,-22,-7,106,-21,]),'ELSE':([5,6,8,9,10,11,12,15,20,23,30,33,34,35,36,37,51,52,70,72,73,74,75,76,89,92,94,95,97,102,106,],[-7,-6,-16,-17,-18,-19,-8,-34,-7,-4,-5,-48,-32,-33,-39,-40,-46,-47,-35,-41,-42,-43,-44,-45,-49,-7,-9,-10,99,-22,-21,]),'INDENT':([12,28,42,78,90,101,103,],[-8,-7,69,-7,92,-7,104,]),'ATRIB':([14,25,],[26,32,]),'LCPARENT':([16,18,38,93,],[27,29,58,96,]),'COLON':([17,59,99,],[28,78,101,]),'NUM':([26,27,29,32,41,53,54,55,56,57,60,61,62,63,64,65,66,67,96,],[37,37,37,49,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'INPUT':([26,32,],[38,38,]),'NOT':([27,41,60,96,],[41,41,41,41,]),'QUOTE':([29,58,71,],[47,47,88,]),'RCPARENT':([29,33,36,37,39,43,44,45,46,48,51,52,58,68,72,73,74,75,76,77,79,80,81,82,83,84,85,86,88,98,],[-51,-48,-39,-40,59,70,-36,-37,-38,-48,-46,-47,-51,-31,-41,-42,-43,-44,-45,89,-29,-23,-24,-25,-26,-27,-28,-30,-50,100,]),'INC':([33,48,],[51,51,]),'DEC':([33,48,],[52,52,]),'SUM':([33,34,36,37,40,45,46,48,51,52,72,73,74,75,76,80,81,82,83,84,85,86,],[-48,53,-39,-40,53,-39,53,-48,-46,-47,-41,-42,-43,-44,53,53,53,53,53,53,53,53,]),'SUB':([33,34,36,37,40,45,46,48,51,52,72,73,74,75,76,80,81,82,83,84,85,86,],[-48,54,-39,-40,54,-39,54,-48,-46,-47,-41,-42,-43,-44,54,54,54,54,54,54,54,54,]),'MULT':([33,34,36,37,40,45,46,48,51,52,72,73,74,75,76,80,81,82,83,84,85,86,],[-48,55,-39,-40,55,-39,55,-48,-46,-47,55,55,-43,-44,55,55,55,55,55,55,55,55,]),'DIV':([33,34,36,37,40,45,46,48,51,52,72,73,74,75,76,80,81,82,83,84,85,86,],[-48,56,-39,-40,56,-39,56,-48,-46,-47,56,56,-43,-44,56,56,56,56,56,56,56,56,]),'MOD':([33,34,36,37,40,45,46,48,51,52,72,73,74,75,76,80,81,82,83,84,85,86,],[-48,57,-39,-40,57,-39,57,-48,-46,-47,-41,-42,-43,-44,57,57,57,57,57,57,57,57,]),'GT':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,61,-46,-47,-41,-42,-43,-44,-45,]),'LT':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,62,-46,-47,-41,-42,-43,-44,-45,]),'GEQ':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,63,-46,-47,-41,-42,-43,-44,-45,]),'LEQ':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,64,-46,-47,-41,-42,-43,-44,-45,]),'EQUIV':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,65,-46,-47,-41,-42,-43,-44,-45,]),'NEQ':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,66,-46,-47,-41,-42,-43,-44,-45,]),'AND':([33,36,37,40,51,52,72,73,74,75,76,],[-48,-39,-40,67,-46,-47,-41,-42,-43,-44,-45,]),'OR':([33,36,37,39,51,52,68,72,73,74,75,76,79,80,81,82,83,84,85,86,98,],[-48,-39,-40,60,-46,-47,60,-41,-42,-43,-44,-45,60,-23,-24,-25,-26,-27,-28,-30,60,]),'STRING':([47,],[71,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ProgramaInit':([0,],[1,]),'Programa':([0,],[2,]),'Corpo':([0,4,69,92,104,],[3,21,87,95,105,]),'Decls':([0,],[4,]),'Proc':([0,3,4,21,69,87,92,95,104,105,],[5,20,5,20,5,20,5,20,5,20,]),'Newline':([0,4,5,7,20,22,28,69,78,92,101,104,],[6,6,23,24,30,31,42,6,90,6,103,6,]),'Decl':([0,4,],[7,22,]),'Atrib':([0,3,4,21,69,87,92,95,104,105,],[8,8,8,8,8,8,8,8,8,8,]),'Print':([0,3,4,21,69,87,92,95,104,105,],[9,9,9,9,9,9,9,9,9,9,]),'If':([0,3,4,21,69,87,92,95,104,105,],[10,10,10,10,10,10,10,10,10,10,]),'DoWhile':([0,3,4,21,69,87,92,95,104,105,],[11,11,11,11,11,11,11,11,11,11,]),'NonFormatted':([0,3,4,21,69,87,92,95,104,105,],[15,15,15,15,15,15,15,15,15,15,]),'Expr':([26,27,29,41,53,54,55,56,57,60,61,62,63,64,65,66,67,96,],[34,40,46,40,72,73,74,75,76,40,80,81,82,83,84,85,86,40,]),'Input':([26,32,],[35,50,]),'Var':([26,27,29,41,53,54,55,56,57,60,61,62,63,64,65,66,67,96,],[36,36,45,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'Cond':([27,41,60,96,],[39,68,79,98,]),'Argument':([29,],[43,]),'String':([29,58,],[44,77,]),'Dedent':([87,95,],[91,97,]),}

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
  ('Proc -> Atrib','Proc',1,'p_Proc_Atrib','yacc.py',93),
  ('Proc -> Print','Proc',1,'p_Proc_Print','yacc.py',97),
  ('Proc -> If','Proc',1,'p_Proc_If','yacc.py',101),
  ('Proc -> DoWhile','Proc',1,'p_DoWhile','yacc.py',105),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent','If',9,'p_If','yacc.py',111),
  ('If -> IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT','If',15,'p_If_Else','yacc.py',116),
  ('DoWhile -> DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE','DoWhile',11,'p_Do_While','yacc.py',122),
  ('Cond -> Expr GT Expr','Cond',3,'p_Cond_GT','yacc.py',127),
  ('Cond -> Expr LT Expr','Cond',3,'p_Cond_LT','yacc.py',131),
  ('Cond -> Expr GEQ Expr','Cond',3,'p_Cond_GEQ','yacc.py',135),
  ('Cond -> Expr LEQ Expr','Cond',3,'p_Cond_LEQ','yacc.py',139),
  ('Cond -> Expr EQUIV Expr','Cond',3,'p_Cond_EQUIV','yacc.py',143),
  ('Cond -> Expr NEQ Expr','Cond',3,'p_Cond_NEQ','yacc.py',147),
  ('Cond -> Cond OR Cond','Cond',3,'p_Cond_OR','yacc.py',151),
  ('Cond -> Expr AND Expr','Cond',3,'p_Cond_AND','yacc.py',155),
  ('Cond -> NOT Cond','Cond',2,'p_Cond_NOT','yacc.py',159),
  ('Atrib -> ID ATRIB Expr','Atrib',3,'p_Atrib_Expr','yacc.py',164),
  ('Atrib -> ID ATRIB Input','Atrib',3,'p_Atrib_Input','yacc.py',172),
  ('Print -> NonFormatted','Print',1,'p_Print_NonFormatted','yacc.py',181),
  ('NonFormatted -> PRINT LCPARENT Argument RCPARENT','NonFormatted',4,'p_NonFormatted','yacc.py',185),
  ('Argument -> String','Argument',1,'p_Argument_String','yacc.py',189),
  ('Argument -> Var','Argument',1,'p_Argument_Var','yacc.py',193),
  ('Argument -> Expr','Argument',1,'p_Argument_Expr','yacc.py',197),
  ('Expr -> Var','Expr',1,'p_Expr_Var','yacc.py',202),
  ('Expr -> NUM','Expr',1,'p_Expr_Num','yacc.py',206),
  ('Expr -> Expr SUM Expr','Expr',3,'p_Expr_Soma','yacc.py',210),
  ('Expr -> Expr SUB Expr','Expr',3,'p_Expr_Sub','yacc.py',214),
  ('Expr -> Expr MULT Expr','Expr',3,'p_Expr_Mult','yacc.py',218),
  ('Expr -> Expr DIV Expr','Expr',3,'p_Expr_Div','yacc.py',222),
  ('Expr -> Expr MOD Expr','Expr',3,'p_Expr_Mod','yacc.py',226),
  ('Expr -> ID INC','Expr',2,'p_Expr_Inc','yacc.py',230),
  ('Expr -> ID DEC','Expr',2,'p_Expr_Dec','yacc.py',234),
  ('Var -> ID','Var',1,'p_Var','yacc.py',238),
  ('Input -> INPUT LCPARENT String RCPARENT','Input',4,'p_Input','yacc.py',251),
  ('String -> QUOTE STRING QUOTE','String',3,'p_String','yacc.py',256),
  ('String -> <empty>','String',0,'p_String_Empty','yacc.py',260),
]
