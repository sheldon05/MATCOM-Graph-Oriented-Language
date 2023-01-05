
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSADD ASSIGN BEGIN CBR COMMA COMPLEMENT CONCAT CPAR DIFFERENCE DIGRAPH DIV EDGE ELIF ELSE END EQUAL FLOAT FOREDGE FORVERTEX GRAPH GREATER GREATEREQ ID IF IN INT INTERSECTION LESS LESSEQ MINUS MUL MULTIGRAPH NEQUAL NODES_COUNT OBR OPAR PLOT PLUS POINT PSEUDOGRAPH STRING UNIONInstructions    : Instructions InstructionInstructions    : Instruction Instruction      : Plot_instr\n                        | If_instr\n                        | If_else_instr\n                        | For_vertex_instr\n                        | Assign_instr\n                        | For_edge_instr\n                        | Add_vertex_instr\n                        | Add_edge_instr\n                        | Add_vertex_and_edge_instrIf_instr         : IF OPAR logic_expression CPAR BEGIN Instructions ENDIf_else_instr  : IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions ENDFor_vertex_instr   : FORVERTEX ID IN ID BEGIN Instructions ENDFor_edge_instr   : FOREDGE ID IN ID BEGIN Instructions ENDPlot_instr   : PLOT OPAR ID CPARAssign_instr     : ID ASSIGN graph_expressionAdd_vertex_instr      : ID ADD OPAR vertex_expression CPARAdd_edge_instr     : ID ADD OPAR edge_expression CPARAdd_vertex_and_edge_instr      : ID ADD OPAR vertex_expression COMMA edge_expression CPARgraph_expression   : GRAPH OPAR value_expression COMMA edge_expression CPAR\n                            | DIGRAPH OPAR value_expression COMMA edge_expression CPAR\n                            | GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | graph_expression UNION graph_expression\n                            | graph_expression INTERSECTION graph_expression\n                            | graph_expression DIFFERENCE graph_expression\n                            | graph_expression CONCAT graph_expression\n                            | ID\n                            vertex_expression    : vertex_expression INT\n                            | INTedge_expression  : edge_expression OPAR INT COMMA INT CPAR\n                        | OPAR INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA INT CPAR\n                        | OPAR INT COMMA INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR \n                        | OPAR INT COMMA INT COMMA FLOAT CPAR\n                        | empty\n                        logic_expression     : value_expression EQUAL value_expression\n                            | value_expression GREATER value_expression\n                            | value_expression LESS value_expression\n                            | value_expression GREATEREQ value_expression\n                            | value_expression LESSEQ value_expression\n                            | value_expression NEQUAL value_expressionvalue_expression     : algebraic_expression\n                            | functionalgebraic_expression      : INT\n                                | FLOATalgebraic_expression     : algebraic_expression PLUS algebraic_expression\n                                | algebraic_expression MINUS algebraic_expression\n                                | algebraic_expression MUL algebraic_expression\n                                | algebraic_expression DIV algebraic_expression\n                                | MINUS algebraic_expression %prec UMINUS\n                                empty :function     : graph_expression POINT NODES_COUNT'
    
_lr_action_items = {'PLOT':([0,1,2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,81,93,94,102,103,104,110,112,113,114,115,117,129,130,131,136,139,],[12,12,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,12,12,12,12,12,12,-20,-12,-14,-15,-21,-22,12,-23,-24,12,-13,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,81,93,94,102,103,104,110,112,113,114,115,117,129,130,131,136,139,],[14,14,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,14,14,14,14,14,14,-20,-12,-14,-15,-21,-22,14,-23,-24,14,-13,]),'FORVERTEX':([0,1,2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,81,93,94,102,103,104,110,112,113,114,115,117,129,130,131,136,139,],[15,15,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,15,15,15,15,15,15,-20,-12,-14,-15,-21,-22,15,-23,-24,15,-13,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19,21,25,26,38,39,40,41,42,43,44,45,46,53,54,55,56,57,58,67,68,69,70,76,80,81,93,94,102,103,104,110,112,113,114,115,117,129,130,131,136,139,],[13,13,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,22,23,-1,24,25,25,-29,-17,65,66,-16,25,25,25,25,25,25,25,25,25,25,25,25,-25,-26,-27,-28,-18,-19,13,13,13,13,13,13,-20,-12,-14,-15,-21,-22,13,-23,-24,13,-13,]),'FOREDGE':([0,1,2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,81,93,94,102,103,104,110,112,113,114,115,117,129,130,131,136,139,],[16,16,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,16,16,16,16,16,16,-20,-12,-14,-15,-21,-22,16,-23,-24,16,-13,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,110,112,113,114,115,117,130,131,139,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,-20,-12,-14,-15,-21,-22,-23,-24,-13,]),'END':([2,3,4,5,6,7,8,9,10,11,17,25,26,40,67,68,69,70,76,80,102,103,104,110,112,113,114,115,117,130,131,136,139,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-29,-17,-16,-25,-26,-27,-28,-18,-19,112,113,114,-20,-12,-14,-15,-21,-22,-23,-24,139,-13,]),'OPAR':([12,14,20,27,28,29,49,51,77,95,97,100,105,107,116,118,120,123,124,128,132,133,137,138,],[18,21,29,45,46,47,79,-38,47,47,47,79,79,79,47,47,-33,79,79,-32,-35,-37,-34,-36,]),'ASSIGN':([13,],[19,]),'ADD':([13,],[20,]),'GRAPH':([19,21,41,42,43,44,45,46,53,54,55,56,57,58,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DIGRAPH':([19,21,41,42,43,44,45,46,53,54,55,56,57,58,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'INT':([21,29,36,45,46,47,48,50,53,54,55,56,57,58,59,60,61,62,72,74,78,79,96,98,99,111,119,127,],[34,50,34,34,34,75,78,-31,34,34,34,34,34,34,34,34,34,34,50,50,-30,101,78,78,109,121,125,134,]),'FLOAT':([21,36,45,46,53,54,55,56,57,58,59,60,61,62,119,127,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,126,135,]),'MINUS':([21,32,34,35,36,45,46,53,54,55,56,57,58,59,60,61,62,63,88,89,90,91,],[36,60,-47,-48,36,36,36,36,36,36,36,36,36,36,36,36,36,-53,-49,-50,-51,-52,]),'IN':([22,23,],[38,39,]),'CPAR':([24,29,30,32,33,34,35,48,49,50,51,63,77,78,82,83,84,85,86,87,88,89,90,91,92,95,97,100,105,107,109,116,118,120,121,123,124,125,126,128,132,133,134,135,137,138,],[40,-54,52,-45,-46,-47,-48,76,80,-31,-38,-53,-54,-30,-39,-40,-41,-42,-43,-44,-49,-50,-51,-52,-55,-54,-54,110,115,117,120,-54,-54,-33,128,130,131,132,133,-32,-35,-37,137,138,-34,-36,]),'UNION':([25,26,37,67,68,69,70,115,117,130,131,],[-29,41,41,41,41,41,41,-21,-22,-23,-24,]),'INTERSECTION':([25,26,37,67,68,69,70,115,117,130,131,],[-29,42,42,42,42,42,42,-21,-22,-23,-24,]),'DIFFERENCE':([25,26,37,67,68,69,70,115,117,130,131,],[-29,43,43,43,43,43,43,-21,-22,-23,-24,]),'CONCAT':([25,26,37,67,68,69,70,115,117,130,131,],[-29,44,44,44,44,44,44,-21,-22,-23,-24,]),'POINT':([25,37,67,68,69,70,115,117,130,131,],[-29,64,-25,-26,-27,-28,-21,-22,-23,-24,]),'EQUAL':([31,32,33,34,35,63,88,89,90,91,92,],[53,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'GREATER':([31,32,33,34,35,63,88,89,90,91,92,],[54,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'LESS':([31,32,33,34,35,63,88,89,90,91,92,],[55,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'GREATEREQ':([31,32,33,34,35,63,88,89,90,91,92,],[56,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'LESSEQ':([31,32,33,34,35,63,88,89,90,91,92,],[57,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'NEQUAL':([31,32,33,34,35,63,88,89,90,91,92,],[58,-45,-46,-47,-48,-53,-49,-50,-51,-52,-55,]),'COMMA':([32,33,34,35,48,50,63,71,73,75,78,88,89,90,91,92,101,106,108,109,121,],[-45,-46,-47,-48,77,-31,-53,95,97,99,-30,-49,-50,-51,-52,-55,111,116,118,119,127,]),'PLUS':([32,34,35,63,88,89,90,91,],[59,-47,-48,-53,-49,-50,-51,-52,]),'MUL':([32,34,35,63,88,89,90,91,],[61,-47,-48,-53,61,61,-51,-52,]),'DIV':([32,34,35,63,88,89,90,91,],[62,-47,-48,-53,62,62,-51,-52,]),'OBR':([45,46,],[72,74,]),'CBR':([50,78,96,98,],[-31,-30,106,108,]),'BEGIN':([52,65,66,122,],[81,93,94,129,]),'NODES_COUNT':([64,],[92,]),'ELSE':([112,],[122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Instructions':([0,81,93,94,129,],[1,102,103,104,136,]),'Instruction':([0,1,81,93,94,102,103,104,129,136,],[2,17,2,2,2,17,17,17,2,17,]),'Plot_instr':([0,1,81,93,94,102,103,104,129,136,],[3,3,3,3,3,3,3,3,3,3,]),'If_instr':([0,1,81,93,94,102,103,104,129,136,],[4,4,4,4,4,4,4,4,4,4,]),'If_else_instr':([0,1,81,93,94,102,103,104,129,136,],[5,5,5,5,5,5,5,5,5,5,]),'For_vertex_instr':([0,1,81,93,94,102,103,104,129,136,],[6,6,6,6,6,6,6,6,6,6,]),'Assign_instr':([0,1,81,93,94,102,103,104,129,136,],[7,7,7,7,7,7,7,7,7,7,]),'For_edge_instr':([0,1,81,93,94,102,103,104,129,136,],[8,8,8,8,8,8,8,8,8,8,]),'Add_vertex_instr':([0,1,81,93,94,102,103,104,129,136,],[9,9,9,9,9,9,9,9,9,9,]),'Add_edge_instr':([0,1,81,93,94,102,103,104,129,136,],[10,10,10,10,10,10,10,10,10,10,]),'Add_vertex_and_edge_instr':([0,1,81,93,94,102,103,104,129,136,],[11,11,11,11,11,11,11,11,11,11,]),'graph_expression':([19,21,41,42,43,44,45,46,53,54,55,56,57,58,],[26,37,67,68,69,70,37,37,37,37,37,37,37,37,]),'logic_expression':([21,],[30,]),'value_expression':([21,45,46,53,54,55,56,57,58,],[31,71,73,82,83,84,85,86,87,]),'algebraic_expression':([21,36,45,46,53,54,55,56,57,58,59,60,61,62,],[32,63,32,32,32,32,32,32,32,32,88,89,90,91,]),'function':([21,45,46,53,54,55,56,57,58,],[33,33,33,33,33,33,33,33,33,]),'vertex_expression':([29,72,74,],[48,96,98,]),'edge_expression':([29,77,95,97,116,118,],[49,100,105,107,123,124,]),'empty':([29,77,95,97,116,118,],[51,51,51,51,51,51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Instructions","S'",1,None,None,None),
  ('Instructions -> Instructions Instruction','Instructions',2,'p_instructions_list','parser_rules.py',15),
  ('Instructions -> Instruction','Instructions',1,'p_instructions_instruction','parser_rules.py',21),
  ('Instruction -> Plot_instr','Instruction',1,'p_instruction','parser_rules.py',26),
  ('Instruction -> If_instr','Instruction',1,'p_instruction','parser_rules.py',27),
  ('Instruction -> If_else_instr','Instruction',1,'p_instruction','parser_rules.py',28),
  ('Instruction -> For_vertex_instr','Instruction',1,'p_instruction','parser_rules.py',29),
  ('Instruction -> Assign_instr','Instruction',1,'p_instruction','parser_rules.py',30),
  ('Instruction -> For_edge_instr','Instruction',1,'p_instruction','parser_rules.py',31),
  ('Instruction -> Add_vertex_instr','Instruction',1,'p_instruction','parser_rules.py',32),
  ('Instruction -> Add_edge_instr','Instruction',1,'p_instruction','parser_rules.py',33),
  ('Instruction -> Add_vertex_and_edge_instr','Instruction',1,'p_instruction','parser_rules.py',34),
  ('If_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END','If_instr',7,'p_if_instr','parser_rules.py',40),
  ('If_else_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions END','If_else_instr',11,'p_if_else_instr','parser_rules.py',45),
  ('For_vertex_instr -> FORVERTEX ID IN ID BEGIN Instructions END','For_vertex_instr',7,'p_for_vertex_instr','parser_rules.py',50),
  ('For_edge_instr -> FOREDGE ID IN ID BEGIN Instructions END','For_edge_instr',7,'p_for_edge_instr','parser_rules.py',55),
  ('Plot_instr -> PLOT OPAR ID CPAR','Plot_instr',4,'p_Plot_instr','parser_rules.py',61),
  ('Assign_instr -> ID ASSIGN graph_expression','Assign_instr',3,'p_assign_instr','parser_rules.py',67),
  ('Add_vertex_instr -> ID ADD OPAR vertex_expression CPAR','Add_vertex_instr',5,'p_add_vertex_instr','parser_rules.py',73),
  ('Add_edge_instr -> ID ADD OPAR edge_expression CPAR','Add_edge_instr',5,'p_add_edge_instr','parser_rules.py',79),
  ('Add_vertex_and_edge_instr -> ID ADD OPAR vertex_expression COMMA edge_expression CPAR','Add_vertex_and_edge_instr',7,'p_add_vertex_and_edge_instr','parser_rules.py',84),
  ('graph_expression -> GRAPH OPAR value_expression COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',89),
  ('graph_expression -> DIGRAPH OPAR value_expression COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',90),
  ('graph_expression -> GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',91),
  ('graph_expression -> DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',92),
  ('graph_expression -> graph_expression UNION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',93),
  ('graph_expression -> graph_expression INTERSECTION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',94),
  ('graph_expression -> graph_expression DIFFERENCE graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',95),
  ('graph_expression -> graph_expression CONCAT graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',96),
  ('graph_expression -> ID','graph_expression',1,'p_graph_expression','parser_rules.py',97),
  ('vertex_expression -> vertex_expression INT','vertex_expression',2,'p_vertex_expression','parser_rules.py',113),
  ('vertex_expression -> INT','vertex_expression',1,'p_vertex_expression','parser_rules.py',114),
  ('edge_expression -> edge_expression OPAR INT COMMA INT CPAR','edge_expression',6,'p_edge_expression','parser_rules.py',122),
  ('edge_expression -> OPAR INT COMMA INT CPAR','edge_expression',5,'p_edge_expression','parser_rules.py',123),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA INT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',124),
  ('edge_expression -> OPAR INT COMMA INT COMMA INT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',125),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',126),
  ('edge_expression -> OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',127),
  ('edge_expression -> empty','edge_expression',1,'p_edge_expression','parser_rules.py',128),
  ('logic_expression -> value_expression EQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',144),
  ('logic_expression -> value_expression GREATER value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',145),
  ('logic_expression -> value_expression LESS value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',146),
  ('logic_expression -> value_expression GREATEREQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',147),
  ('logic_expression -> value_expression LESSEQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',148),
  ('logic_expression -> value_expression NEQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',149),
  ('value_expression -> algebraic_expression','value_expression',1,'p_value_expression','parser_rules.py',154),
  ('value_expression -> function','value_expression',1,'p_value_expression','parser_rules.py',155),
  ('algebraic_expression -> INT','algebraic_expression',1,'p_algebraic_expression_number','parser_rules.py',161),
  ('algebraic_expression -> FLOAT','algebraic_expression',1,'p_algebraic_expression_number','parser_rules.py',162),
  ('algebraic_expression -> algebraic_expression PLUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',167),
  ('algebraic_expression -> algebraic_expression MINUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',168),
  ('algebraic_expression -> algebraic_expression MUL algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',169),
  ('algebraic_expression -> algebraic_expression DIV algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',170),
  ('algebraic_expression -> MINUS algebraic_expression','algebraic_expression',2,'p_algebraic_expression','parser_rules.py',171),
  ('empty -> <empty>','empty',0,'p_empty','parser_rules.py',180),
  ('function -> graph_expression POINT NODES_COUNT','function',3,'p_function_nodes_count','parser_rules.py',184),
]
