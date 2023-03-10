from ply import lex


keywords = {
    'graph' : 'GRAPH',
    'multigraph' : 'MULTIGRAPH',
    'pseudograph' : 'PSEUDOGRAPH',
    'digraph' : 'DIGRAPH',
    'if' : 'IF',
    'else' : 'ELSE',
    'elif' : 'ELIF',
    'edge' : 'EDGE',
    'plot' : 'PLOT',
    'foredge' : 'FOREDGE',
    'forvertex' : 'FORVERTEX',
    'begin' : 'BEGIN',
    'end' : 'END',
    'in' : 'IN',
    'union' : 'UNION',
    'intersection' : 'INTERSECTION',
    'difference' : 'DIFFERENCE',
    'complement' : 'COMPLEMENT',
    'add' : 'ADD',
    'nodes_count' : 'NODES_COUNT',
    'concat' : 'CONCAT',
    'edges_count' : 'EDGES_COUNT',
    'weight_sum' : 'WEIGHT_SUM',
    'contain_vertex' : 'CONTAIN_VERTEX',
    'contain_edges' : 'CONTAIN_EDGES',
    'k_color_plot' : 'K_COLOR_PLOT',
    'weighted_plot' : 'WEIGHTED_PLOT',
    'kruskal' : 'KRUSKAL',
    'prim' : 'PRIM',
    'bfs' : 'BFS',
    'dijkstra' : 'DIJKSTRA'
}

tokens = [
    'OPAR',
    'CPAR',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'ID',
    'LESS',
    'GREATER',
    'EQUAL',
    'GREATEREQ',
    'LESSEQ',
    'NEQUAL',
    'INT',
    'FLOAT',
    'STRING',
    'COMMA',
    'OBR',
    'CBR',
    'POINT'
 ] + list(keywords.values())

#TOKENS

t_OPAR = r'\('
t_CPAR = r'\)'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIV = r'/'
t_MUL = r'\*'
t_LESS = r'<' 
t_GREATER = r'>'
t_EQUAL = r'=='
t_GREATEREQ = r'>='
t_LESSEQ = r'<='
t_NEQUAL = r'!='
t_COMMA = r','
t_OBR = r'\['
t_CBR = r'\]'
t_POINT = r'.'

def t_FLOAT (t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_INT (t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = keywords.get(t.value.lower(),'ID')
     return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(debug=True)