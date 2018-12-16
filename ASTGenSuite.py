import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin end"""
    #     expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))
    #
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ():INTEGER; begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    #
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         getIntLn();
    #     end
    #     function foo ():INTEGER; begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
    #             FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,302))

    # From me
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin
                end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_program_2(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin
                end
                procedure MaiN();
                begin
                end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType()),FuncDecl(Id("MaiN"),[],[],[],VoidType())]))
        expect = "Program([FuncDecl(Id(main),[],VoidType(),[],[]),FuncDecl(Id(MaiN),[],VoidType(),[],[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program_3(self):
        """Simple program: int main() {} """
        input = """procedure mAIN();
                begin
                end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType())]))
        expect = "Program([FuncDecl(Id(mAIN),[],VoidType(),[],[])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_program_4(self):
        """Simple program: int main() {} """
        input = """function foo(): integer;
                begin
                end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
        # expect = "Program([FuncDecl(Id(foo),[],IntType,[],[a,b,c,d])])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_simple_program_5(self):
        # real is FloatType
        input = """function foo(): real;
                begin
                end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        # expect = "Program([FuncDecl(Id(foo),[],IntType,[],[a,b,c,d])])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_simple_program_6(self):
        # test varDecl simple
        input = """function foo(): real;
                begin
                end
                var a,b:integer;
                    d:real;
                    f:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[],FloatType,[],[]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(f),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_program_7(self):
        # test varDecl list complex
        input = """function foo(): real;
                begin
                end
                var a,b,c:integer;
                    d,e:real;
                    f,g,h,i,j,k:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],FloatType,[],[]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType),VarDecl(Id(f),StringType),VarDecl(Id(g),StringType),VarDecl(Id(h),StringType),VarDecl(Id(i),StringType),VarDecl(Id(j),StringType),VarDecl(Id(k),StringType)])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_simple_program_8(self):
        # test varDecl list complex
        input = """ var a,b,c:integer;
                        d,e:real;
                        f,g,h,i,j,k:string;
                    function foo(): real;
                        begin
                        end
                    var a,b,c:integer;
                        d,e:real;
                        f,g,h,i,j,k:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType),VarDecl(Id(f),StringType),VarDecl(Id(g),StringType),VarDecl(Id(h),StringType),VarDecl(Id(i),StringType),VarDecl(Id(j),StringType),VarDecl(Id(k),StringType),FuncDecl(Id(foo),[],FloatType,[],[]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType),VarDecl(Id(f),StringType),VarDecl(Id(g),StringType),VarDecl(Id(h),StringType),VarDecl(Id(i),StringType),VarDecl(Id(j),StringType),VarDecl(Id(k),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_statement(self):
        # test varDecl list complex
        input = """function foo(): real;
                        begin
                            continue;
                        end
                    var a,b,c:integer;
                        d:real;
                        e,f:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[],FloatType,[],[Continue]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),StringType),VarDecl(Id(f),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,309))

    def test_function_var(self):
        # test varDecl list complex
        input = """function foo(): real;
                        var x,y:string;
                            k,n:integer;
                        begin
                        end
                    var a,b,c:integer;
                        d:real;
                        e,f:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[],FloatType,[VarDecl(Id(x),StringType),VarDecl(Id(y),StringType),VarDecl(Id(k),IntType),VarDecl(Id(n),IntType)],[]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),StringType),VarDecl(Id(f),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,310))

    def test_function_argument(self):
        # test varDecl list complex
        input = """function foo(s:string;i:integer): real;
                        var x,y:string;
                            k,n:integer;
                        begin
                        end
                    var a,b,c:integer;
                        d:real;
                        e,f:string;
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[VarDecl(Id(s),StringType),VarDecl(Id(i),IntType)],FloatType,[VarDecl(Id(x),StringType),VarDecl(Id(y),StringType),VarDecl(Id(k),IntType),VarDecl(Id(n),IntType)],[]),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),StringType),VarDecl(Id(f),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,311))

    def test_function_argument_multi(self):
        # test varDecl list complex
        input = """function foo(sa,sb:string;ia,ib:integer): real;
                        var x,y:string;
                            k,n:integer;
                        begin
                            continue;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[VarDecl(Id(sa),StringType),VarDecl(Id(sb),StringType),VarDecl(Id(ia),IntType),VarDecl(Id(ib),IntType)],FloatType,[VarDecl(Id(x),StringType),VarDecl(Id(y),StringType),VarDecl(Id(k),IntType),VarDecl(Id(n),IntType)],[Continue])])"""
        self.assertTrue(TestAST.test(input,expect,312))

    def test_function_argument_multi_2(self):
        # test varDecl list complex
        input = """function foo(s1,s2:string;i1,i2,i3:integer): real;
                        var x,y:string;
                            k,n:integer;
                        begin
                            continue;
                            break;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[VarDecl(Id(s1),StringType),VarDecl(Id(s2),StringType),VarDecl(Id(i1),IntType),VarDecl(Id(i2),IntType),VarDecl(Id(i3),IntType)],FloatType,[VarDecl(Id(x),StringType),VarDecl(Id(y),StringType),VarDecl(Id(k),IntType),VarDecl(Id(n),IntType)],[Continue,Break])])"""
        self.assertTrue(TestAST.test(input,expect,313))

    def test_procedure(self):
        # test varDecl list complex
        input = """procedure foo(s1,s2:string;i1,i2,i3:integer);
                        var x,y:string;
                            k,n:integer;
                        begin
                            continue;
                            break;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = """Program([FuncDecl(Id(foo),[VarDecl(Id(s1),StringType),VarDecl(Id(s2),StringType),VarDecl(Id(i1),IntType),VarDecl(Id(i2),IntType),VarDecl(Id(i3),IntType)],VoidType(),[VarDecl(Id(x),StringType),VarDecl(Id(y),StringType),VarDecl(Id(k),IntType),VarDecl(Id(n),IntType)],[Continue,Break])])"""
        self.assertTrue(TestAST.test(input,expect,314))

    def test_stmt_assign(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            a := 7;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(7))])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_stmt_assign_string(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            a := "i am learning";
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[AssignStmt(Id(a),StringLiteral(i am learning))])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_stmt_assign_multi(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            a := b := "i am learning.";
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[AssignStmt(Id(b),StringLiteral(i am learning.)),AssignStmt(Id(a),Id(b))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_stmt_if(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            a := "i am learning.";
                            if a then
                                break;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[AssignStmt(Id(a),StringLiteral(i am learning.)),If(Id(a),[Break],[])])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_stmt_if_else(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            a := "i am learning.";
                            if a then
                                x := y := "stringX";;;;;
                            else
                                continue;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[AssignStmt(Id(a),StringLiteral(i am learning.)),If(Id(a),[AssignStmt(Id(y),StringLiteral(stringX)),AssignStmt(Id(x),Id(y))],[]),Continue])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_stmt_while(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            continue;
                            while a do
                                x := y := 15;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[Continue,While(Id(a),[AssignStmt(Id(y),IntLiteral(15)),AssignStmt(Id(x),Id(y))])])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_stmt_for(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            for i := 3 to 5 do
                                x := y := 100;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[For(Id(i)IntLiteral(3),IntLiteral(5),BooleanLiteral(true),[AssignStmt(Id(y),IntLiteral(100)),AssignStmt(Id(x),Id(y))])])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_stmt_return(self):
        # test varDecl list complex
        input = """procedure foo();
                        begin
                            for i := 3 to 5 do
                                x := y := 100;
                            return x;
                        end
                """
        # expect = str(Program([FuncDecl("MAIN",[],[],[])]))
        # expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[For(Id(i)IntLiteral(3),IntLiteral(5),BooleanLiteral(true),[AssignStmt(Id(y),IntLiteral(100)),AssignStmt(Id(x),Id(y))]),Return(Some(Id(x)))])])"
        self.assertTrue(TestAST.test(input,expect,322))