import ply.lex as lex

tokens = (
    'COMMENT',
    'TYPE',
    'VARIABLE',
    'SEMICOLON',
    'FUNCTIONKEYWORD',
    'FUNCTIONNAME',
    'PAR',
    'BRACKETS',
    'ATRIB',
    'VALUE',
    'OPERATOR',
    'LOOP',
    'IN',
    'RANGE',
    'COMMA',
    'PROGRAM',
    'ATINDEX',
    'ARRAY'
)

t_COMMENT = r'(\/\*(.|\n)*\*\/)|(//.*)'

def t_TYPE(t):
  r'int'
  return t

t_VARIABLE = r'[a-zA-Z](\w|_)*'
t_SEMICOLON = r';'

def t_FUNCTIONKEYWORD(t):
  r'function'
  return t

t_ignore = ' \n\t'

def t_FUNCTIONNAME(t):
  r'\w+(?=\()'
  return t

def t_PAR(t):
  r'(\(|\))'
  return t

def t_BRACKETS(t):
  r'(\(|\)|\{|\})(?!\d)'
  return t

def t_ATRIB(t):
  r'\='
  return t

def t_VALUE(t):
  r'\d+'
  return t

def t_OPERATOR(t):
  r'(\+|\-|\*|\/|\=\=|\<|\>)(?=\s)'
  return t

def t_LOOP(t):
  r'(for|while)'
  return t

def t_IN(t):
  r'in(?=\s)'
  return t

def t_RANGE(t):
  r'\[\w+\.\.\w+\]'
  return t

def t_COMMA(t):
  r','
  return t

def t_PROGRAM(t):
  r'program'
  return t

def t_ATINDEX(t):
  r'\[\w+\]'
  return t

def t_ARRAY(t):
  r'\{[\d+,]*\d+\}'
  return t

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

data2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

lexer.input(data2)

while tok := lexer.token():
    print(tok)