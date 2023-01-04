
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSASSIGN BEGIN CBR COMMA COMPLEMENT CPAR DIFFERENCE DIGRAPH DIV EDGE ELIF ELSE END EQUAL FLOAT FOREDGE FORVERTEX GRAPH GREATER GREATEREQ ID IF IN INT INTERSECTION LESS LESSEQ MINUS MUL MULTIGRAPH NEQUAL OBR OPAR PLOT PLUS PSEUDOGRAPH STRING UNIONInstructions    : Instructions InstructionInstructions    : Instruction Instruction      : Plot_instr\n                        | If_instr\n                        | If_else_instr\n                        | For_vertex_instr\n                        | Assign_instr\n                        | For_edge_instrIf_instr         : IF OPAR logic_expression CPAR BEGIN Instructions ENDIf_else_instr  : IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions ENDFor_vertex_instr   : FORVERTEX ID IN ID BEGIN Instructions ENDFor_edge_instr   : FOREDGE ID IN ID BEGIN Instructions ENDPlot_instr    : PLOT OPAR ID CPARAssign_instr     : ID ASSIGN graph_expressiongraph_expression   : GRAPH OPAR INT COMMA edge_expression CPAR\n                            | DIGRAPH OPAR INT COMMA edge_expression CPAR\n                            | GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | graph_expression UNION graph_expression\n                            | graph_expression INTERSECTION graph_expressionvertex_expression    : vertex_expression INT\n                            | INTedge_expression  : edge_expression OPAR INT COMMA INT CPAR\n                        | OPAR INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA INT CPAR\n                        | OPAR INT COMMA INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR \n                        | OPAR INT COMMA INT COMMA FLOAT CPAR\n                        logic_expression     : value_expression EQUAL value_expression\n                            | value_expression GREATER value_expression\n                            | value_expression LESS value_expression\n                            | value_expression GREATEREQ value_expression\n                            | value_expression LESSEQ value_expression\n                            | value_expression NEQUAL value_expressionvalue_expression     : algebraic_expressionalgebraic_expression     : INT\n                                | FLOAT\n                                | algebraic_expression PLUS algebraic_expression\n                                | algebraic_expression MINUS algebraic_expression\n                                | algebraic_expression MUL algebraic_expression\n                                | algebraic_expression DIV algebraic_expression\n                                | MINUS algebraic_expression %prec UMINUS\n                                '
    
_lr_action_items = {'PLOT':([0,1,2,3,4,5,6,7,8,14,21,32,51,52,57,68,69,75,76,77,84,85,86,89,91,98,101,102,103,107,],[9,9,-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,9,9,9,9,9,9,-9,-11,-12,-15,-16,9,-17,-18,9,-10,]),'IF':([0,1,2,3,4,5,6,7,8,14,21,32,51,52,57,68,69,75,76,77,84,85,86,89,91,98,101,102,103,107,],[11,11,-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,11,11,11,11,11,11,-9,-11,-12,-15,-16,11,-17,-18,11,-10,]),'FORVERTEX':([0,1,2,3,4,5,6,7,8,14,21,32,51,52,57,68,69,75,76,77,84,85,86,89,91,98,101,102,103,107,],[12,12,-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,12,12,12,12,12,12,-9,-11,-12,-15,-16,12,-17,-18,12,-10,]),'ID':([0,1,2,3,4,5,6,7,8,12,13,14,15,21,30,31,32,51,52,57,68,69,75,76,77,84,85,86,89,91,98,101,102,103,107,],[10,10,-2,-3,-4,-5,-6,-7,-8,18,19,-1,20,-14,49,50,-13,-19,-20,10,10,10,10,10,10,-9,-11,-12,-15,-16,10,-17,-18,10,-10,]),'FOREDGE':([0,1,2,3,4,5,6,7,8,14,21,32,51,52,57,68,69,75,76,77,84,85,86,89,91,98,101,102,103,107,],[13,13,-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,13,13,13,13,13,13,-9,-11,-12,-15,-16,13,-17,-18,13,-10,]),'$end':([1,2,3,4,5,6,7,8,14,21,32,51,52,84,85,86,89,91,101,102,107,],[0,-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,-9,-11,-12,-15,-16,-17,-18,-10,]),'END':([2,3,4,5,6,7,8,14,21,32,51,52,75,76,77,84,85,86,89,91,101,102,103,107,],[-2,-3,-4,-5,-6,-7,-8,-1,-14,-13,-19,-20,84,85,86,-9,-11,-12,-15,-16,-17,-18,107,-10,]),'OPAR':([9,11,22,23,70,73,79,82,90,92,96,97,105,111,112,113,116,117,],[15,17,35,36,78,78,88,88,78,78,88,88,-24,-23,-26,-28,-25,-27,]),'ASSIGN':([10,],[16,]),'GRAPH':([16,33,34,],[22,22,22,]),'DIGRAPH':([16,33,34,],[23,23,23,]),'INT':([17,29,35,36,38,39,40,41,42,43,44,45,46,47,54,56,71,72,74,78,81,88,94,100,104,110,],[27,27,53,55,27,27,27,27,27,27,27,27,27,27,72,72,81,-22,81,87,-21,95,99,106,108,114,]),'FLOAT':([17,29,38,39,40,41,42,43,44,45,46,47,104,110,],[28,28,28,28,28,28,28,28,28,28,28,28,109,115,]),'MINUS':([17,26,27,28,29,38,39,40,41,42,43,44,45,46,47,48,64,65,66,67,],[29,45,-36,-37,29,29,29,29,29,29,29,29,29,29,29,-42,-38,-39,-40,-41,]),'IN':([18,19,],[30,31,]),'CPAR':([20,24,26,27,28,48,58,59,60,61,62,63,64,65,66,67,79,82,96,97,99,105,106,108,109,111,112,113,114,115,116,117,],[32,37,-35,-36,-37,-42,-29,-30,-31,-32,-33,-34,-38,-39,-40,-41,89,91,101,102,105,-24,111,112,113,-23,-26,-28,116,117,-25,-27,]),'UNION':([21,51,52,89,91,101,102,],[33,33,33,-15,-16,-17,-18,]),'INTERSECTION':([21,51,52,89,91,101,102,],[34,34,34,-15,-16,-17,-18,]),'EQUAL':([25,26,27,28,48,64,65,66,67,],[38,-35,-36,-37,-42,-38,-39,-40,-41,]),'GREATER':([25,26,27,28,48,64,65,66,67,],[39,-35,-36,-37,-42,-38,-39,-40,-41,]),'LESS':([25,26,27,28,48,64,65,66,67,],[40,-35,-36,-37,-42,-38,-39,-40,-41,]),'GREATEREQ':([25,26,27,28,48,64,65,66,67,],[41,-35,-36,-37,-42,-38,-39,-40,-41,]),'LESSEQ':([25,26,27,28,48,64,65,66,67,],[42,-35,-36,-37,-42,-38,-39,-40,-41,]),'NEQUAL':([25,26,27,28,48,64,65,66,67,],[43,-35,-36,-37,-42,-38,-39,-40,-41,]),'PLUS':([26,27,28,48,64,65,66,67,],[44,-36,-37,-42,-38,-39,-40,-41,]),'MUL':([26,27,28,48,64,65,66,67,],[46,-36,-37,-42,46,46,-40,-41,]),'DIV':([26,27,28,48,64,65,66,67,],[47,-36,-37,-42,47,47,-40,-41,]),'OBR':([35,36,],[54,56,]),'BEGIN':([37,49,50,93,],[57,68,69,98,]),'COMMA':([53,55,80,83,87,95,99,106,],[70,73,90,92,94,100,104,110,]),'CBR':([71,72,74,81,],[80,-22,83,-21,]),'ELSE':([84,],[93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Instructions':([0,57,68,69,98,],[1,75,76,77,103,]),'Instruction':([0,1,57,68,69,75,76,77,98,103,],[2,14,2,2,2,14,14,14,2,14,]),'Plot_instr':([0,1,57,68,69,75,76,77,98,103,],[3,3,3,3,3,3,3,3,3,3,]),'If_instr':([0,1,57,68,69,75,76,77,98,103,],[4,4,4,4,4,4,4,4,4,4,]),'If_else_instr':([0,1,57,68,69,75,76,77,98,103,],[5,5,5,5,5,5,5,5,5,5,]),'For_vertex_instr':([0,1,57,68,69,75,76,77,98,103,],[6,6,6,6,6,6,6,6,6,6,]),'Assign_instr':([0,1,57,68,69,75,76,77,98,103,],[7,7,7,7,7,7,7,7,7,7,]),'For_edge_instr':([0,1,57,68,69,75,76,77,98,103,],[8,8,8,8,8,8,8,8,8,8,]),'graph_expression':([16,33,34,],[21,51,52,]),'logic_expression':([17,],[24,]),'value_expression':([17,38,39,40,41,42,43,],[25,58,59,60,61,62,63,]),'algebraic_expression':([17,29,38,39,40,41,42,43,44,45,46,47,],[26,48,26,26,26,26,26,26,64,65,66,67,]),'vertex_expression':([54,56,],[71,74,]),'edge_expression':([70,73,90,92,],[79,82,96,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Instructions","S'",1,None,None,None),
  ('Instructions -> Instructions Instruction','Instructions',2,'p_instructions_list','parser_rules.py',13),
  ('Instructions -> Instruction','Instructions',1,'p_instructions_instruction','parser_rules.py',19),
  ('Instruction -> Plot_instr','Instruction',1,'p_instruction','parser_rules.py',24),
  ('Instruction -> If_instr','Instruction',1,'p_instruction','parser_rules.py',25),
  ('Instruction -> If_else_instr','Instruction',1,'p_instruction','parser_rules.py',26),
  ('Instruction -> For_vertex_instr','Instruction',1,'p_instruction','parser_rules.py',27),
  ('Instruction -> Assign_instr','Instruction',1,'p_instruction','parser_rules.py',28),
  ('Instruction -> For_edge_instr','Instruction',1,'p_instruction','parser_rules.py',29),
  ('If_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END','If_instr',7,'p_if_instr','parser_rules.py',35),
  ('If_else_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions END','If_else_instr',11,'p_if_else_instr','parser_rules.py',40),
  ('For_vertex_instr -> FORVERTEX ID IN ID BEGIN Instructions END','For_vertex_instr',7,'p_for_vertex_instr','parser_rules.py',45),
  ('For_edge_instr -> FOREDGE ID IN ID BEGIN Instructions END','For_edge_instr',7,'p_for_edge_instr','parser_rules.py',50),
  ('Plot_instr -> PLOT OPAR ID CPAR','Plot_instr',4,'p_Plot_instr','parser_rules.py',56),
  ('Assign_instr -> ID ASSIGN graph_expression','Assign_instr',3,'p_assign_instr','parser_rules.py',61),
  ('graph_expression -> GRAPH OPAR INT COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',67),
  ('graph_expression -> DIGRAPH OPAR INT COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',68),
  ('graph_expression -> GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',69),
  ('graph_expression -> DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',70),
  ('graph_expression -> graph_expression UNION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',71),
  ('graph_expression -> graph_expression INTERSECTION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',72),
  ('vertex_expression -> vertex_expression INT','vertex_expression',2,'p_vertex_expression','parser_rules.py',86),
  ('vertex_expression -> INT','vertex_expression',1,'p_vertex_expression','parser_rules.py',87),
  ('edge_expression -> edge_expression OPAR INT COMMA INT CPAR','edge_expression',6,'p_edge_expression','parser_rules.py',95),
  ('edge_expression -> OPAR INT COMMA INT CPAR','edge_expression',5,'p_edge_expression','parser_rules.py',96),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA INT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',97),
  ('edge_expression -> OPAR INT COMMA INT COMMA INT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',98),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',99),
  ('edge_expression -> OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',100),
  ('logic_expression -> value_expression EQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',114),
  ('logic_expression -> value_expression GREATER value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',115),
  ('logic_expression -> value_expression LESS value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',116),
  ('logic_expression -> value_expression GREATEREQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',117),
  ('logic_expression -> value_expression LESSEQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',118),
  ('logic_expression -> value_expression NEQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',119),
  ('value_expression -> algebraic_expression','value_expression',1,'p_value_expression','parser_rules.py',124),
  ('algebraic_expression -> INT','algebraic_expression',1,'p_algebraic_expression','parser_rules.py',130),
  ('algebraic_expression -> FLOAT','algebraic_expression',1,'p_algebraic_expression','parser_rules.py',131),
  ('algebraic_expression -> algebraic_expression PLUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',132),
  ('algebraic_expression -> algebraic_expression MINUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',133),
  ('algebraic_expression -> algebraic_expression MUL algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',134),
  ('algebraic_expression -> algebraic_expression DIV algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',135),
  ('algebraic_expression -> MINUS algebraic_expression','algebraic_expression',2,'p_algebraic_expression','parser_rules.py',136),
]
