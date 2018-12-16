///**
// * Student name: Vo Quang Tuyen
// * Student ID: 1770165
// * from lexerror import * // assignment 1
// * from lexererr import * // assignment 2
// */

grammar MP;

@lexer::header {
from lexerror import *
}

options{
	language=Python3;
}

//==========RECOGNITION==========
//program: decl* procedureMain decl* EOF ;
program: decl+ EOF ;
decl: funcDecl | procedureDecl | varDecl;
//procedureMain: PROCEDURE MAIN LRB RRB SEMICOLON varDecl? stmtCompound;

funcDecl: FUNCTION ID LRB argLst? RRB COLON varType SEMICOLON varDecl? stmtCompound;
procedureDecl: PROCEDURE ID LRB argLst? RRB SEMICOLON varDecl? stmtCompound;
varDecl: VAR (varLst SEMICOLON)+;

argLst: varLst (SEMICOLON varLst)*;
varType: INTEGERTYPE | STRINGTYPE | REALTYPE | BOOLEANTYPE | arrayTYPE;  //wrong if "ARRAYTYPE"
//body: varDecl? BEGIN stmt* END;
//body: varDecl? stmtCompound;
varLst: ID (COMMA ID)* COLON varType;
stmtCompound: BEGIN stmt* END;  // Have none this class on Teacher's structure, so pay attention

stmt: stmtAssign SEMICOLON | stmtIf | stmtWhile | stmtFor | stmtBreak SEMICOLON | stmtContinue SEMICOLON | stmtReturn SEMICOLON | stmtCompound | stmtWith | stmtCall SEMICOLON;
arrayTYPE: ARRAY LSB expr DOUBLE_DOT expr RSB OF (INTEGERTYPE | STRINGTYPE | REALTYPE | BOOLEANTYPE);

stmtAssign: expr (ASSIGNOP expr)* ASSIGNOP expr ;
stmtIf: IF expr THEN stmt (ELSE stmt)?;
stmtWhile: WHILE expr DO stmt;
stmtFor: FOR ID ASSIGNOP expr (TO | DOWNTO) expr DO stmt;
stmtBreak: BREAK;
stmtContinue: CONTINUE;
stmtReturn: RETURN expr?;
stmtWith: WITHSTMT (varLst SEMICOLON)+ DO stmt;
stmtCall: ID LRB (expr (COMMA expr)*)? RRB;

expr: expr ( ORELSEOP | ANDTHENOP ) term1 | term1;  //final
term1: term2 (EQOP | NEQOP | LTOP | LTEQOP | GTOP | GTEQOP) term2 | term2;
term2: term2 (ADDOP | SUBOP | OROP) term3 | term3;
term3: term3 (DIVISIONOP | MULOP | DIVOP | MODOP) term4 | term4;
term4: (NOTOP | SUBOP) term4 | term5;
term5: ID | ID LSB expr RSB | IntLit | RealLit | BoolLit | StrLit | stmtCall | LRB expr RRB | stmtCall LSB expr RSB;

//==========fragment is the replace algorithm and top_down
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];
fragment DIGIT: [0-9];
//fragment CHARACTER: [a-zA-Z];
//fragment CHARACTER: [A-Z];
//fragment CHARACTER: [A - Z];
fragment CHARACTER: (A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z);

//==========LEXER==========
/* Keywords */
//MAIN: M A I N; //main() is special procedure but it is not a keyword
BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
TO: T O;
DOWNTO: D O W N T O;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
BEGIN: B E G I N;
END: E N D;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
VAR: V A R;
TRUE: T R U E;
FALSE: F A L S E;
OF: O F;

/* Types declaration */
ARRAY: A R R A Y;
REALTYPE: R E A L;
BOOLEANTYPE: B O O L E A N;
INTEGERTYPE: I N T E G E R;
STRINGTYPE: S T R I N G;

/* Operators */
NOTOP: N O T;
ANDOP: A N D;
OROP: O R;
DIVOP: D I V;
MODOP: M O D;
WITHSTMT: W I T H;  // do not know
ORELSEOP: OROP (' ')+ ELSE;
ANDTHENOP: ANDOP (' ')+ THEN;
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVISIONOP: '/';
NEQOP: '<>';
EQOP: '=';
LTOP: '<';
GTOP: '>';
LTEQOP: '<=';
GTEQOP: '>=';
ASSIGNOP: ':=';

/* Separators */
LSB: '[';
RSB: ']';
COLON: ':';
LRB: '(';
RRB: ')';
SEMICOLON: ';';
DOUBLE_DOT: ' .. ';
COMMA: ',';

/* Literals */
IntLit: DIGIT+;
RealLit
    :DIGIT+ '.'
    |DIGIT+ '.' DIGIT+
    |DIGIT* '.' DIGIT+
    |DIGIT+ ('e'|'E')[+-]? DIGIT+
    |DIGIT* '.' DIGIT+ ('e'|'E')[+-]? DIGIT+
    ;
BoolLit: TRUE | FALSE;

StrLit: '"' (~[\b\f\r\n\t'"\\]  | ESCAPE_SEQUENCE)* '"'
        {self.text = self.text[1 : len(self.text) - 1];}  ;
fragment ESCAPE_SEQUENCE: '\\' [bfrnt'"\\];
//Chuoi thoat co 8 characters trong file MP.pdf
//def test_string_ESCAPE_Sequence_3(self):
//    self.assertTrue(TestLexer.test("x:= y := \"line one \\n line two\"", "x,:=,y,:=,line one \\n line two,<EOF>", 131))
// From Mr Dung
// StrLit: '"' (~[\b\f\r\n\t'"\\]  | '\\'[bfrnt"'\\])* '"'
//self.assertTrue(TestLexer.test("\"this is a string isn't   abcd\"", "this is a string isn't   abcd,<EOF>", 119))
//fragment ESCAPE_SEQUENCE: '\\' [btnfr"'\\];

/* Comments */
// In ANTLR, character "?" mean that exist or not but except 'character at end position'
TRADITIONAL_COMMENT: '(*' (.)*? '*)' -> skip;
BLOCK_COMMENT: '{' (.)*? '}' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS : [ \b\f\r\n\t]+ -> skip ; // skip spaces, tabs, newlines
// With \/; \\ is that forward slash (0x2F) and back slash (0x5C)

/* Identifier */
ID: ('_'|CHARACTER)(DIGIT|'_'|CHARACTER)*;

ILLEGAL_ESCAPE: '"' ~[\r\n"]* '\\' ~[bfrnt'"\\]* '"' ;

UNCLOSE_STRING:'"' (~'"')* EOF ;

ERROR_CHAR: . {raise ErrorToken(self.text)};