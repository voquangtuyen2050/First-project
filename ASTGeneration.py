
from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self ,ctx :MPParser.ProgramContext):
        # ctx.decl() ==> List() = [DeclContext0, DeclContext1, DeclContext2, ...., DeclContextN]
        listDecl = []
        for x in ctx.decl():
            a = self.visit(x)
            # check VarDeclare will return a List or not
            if isinstance(a, list):
                for every in a:
                    # print(type(every))
                    listDecl.append(every)
            else:
                listDecl.append(a)
        return Program(listDecl)
        # return Program([self.visit(x) for x in ctx.decl()])
        # a = list(self.visit(x) for x in ctx.decl())
        # y = []
        # for x in a:
        #     y.append(x)
        # return Program(y)

    # MPVisitor Class has this method so we may no need override it
    def visitDecl(self ,ctx :MPParser.DeclContext):
        # ctx.varDecl()
        # if ctx.varDecl():
        return self.visit(ctx.getChild(0))

    def visitProcedureDecl(self ,ctx :MPParser.ProcedureDeclContext):
        cpstmt = self.visit(ctx.stmtCompound())
        paramLst = []
        if ctx.argLst():
            paramLst = self.visit(ctx.argLst())
        varLst = []
        if ctx.varDecl():
            varLst = self.visit(ctx.varDecl())
        return FuncDecl(Id(ctx.ID().getText()),
                        paramLst,     #param List(VarDecl)
                        varLst,     #variable List(VarDecl)
                        cpstmt  #compoundSTMT = List(ObjectStmt0, ObjectStmt1, ObjectStmt2, ......)
                        )       #return Type is VoidType with default

    def visitFuncDecl(self ,ctx :MPParser.FuncDeclContext):
        cpstmt = self.visit(ctx.stmtCompound())
        # print("here")
        # print(type(cpstmt))
        # print(cpstmt)
        # print("here 2")
        paramLst = []
        if ctx.argLst():
            paramLst = self.visit(ctx.argLst())
        varLst = []
        if ctx.varDecl():
            varLst = self.visit(ctx.varDecl())
        return FuncDecl(Id(ctx.ID().getText()),
                        paramLst,     #param List(VarDecl)
                        varLst,     #variable List(VarDecl)
                        cpstmt, #compoundSTMT = List(ObjectStmt0, ObjectStmt1, ObjectStmt2, ......)
                        self.visit(ctx.varType()))       #return TYPE

    def visitVarDecl(self ,ctx :MPParser.VarDeclContext):
        # print("here")
        # x = ctx.varLst()
        # y = ctx.getChildCount()
        # z = ctx.getChild(0)
        # print(len(x))
        # print(y)
        # print("here 2")
        # a = list(self.visit(x) for x in ctx.varLst())
        # return self.visit(ctx.getChild(1))
        # return [(self.visit(x) for x in ctx.varLst())]
        variableLst = []
        for x in ctx.varLst():
            a = self.visit(x)
            # a = visitVarLst(x)
            for y in a:
                variableLst.append(y)
        return variableLst

    def visitVarLst(self, ctx:MPParser.VarLstContext):
        # getType = self.visitVarType(ctx.varType())
        varname = []
        for x in ctx.ID():
            varname.append(x.getText())
        # a = VarDecl(Id(ctx.ID()[0].getText()),self.visit(ctx.varType()))
        # str(a)
        vartype = self.visit(ctx.varType())
        # print(varname)
        # print(vartype)
        varDeclObject = []
        for y in varname:
            varDeclObject.append(VarDecl(Id(y),vartype))
        # return [VarDecl(Id(ctx.ID()[0].getText()),self.visit(ctx.varType()))]
        return varDeclObject

    def visitArgLst(self, ctx:MPParser.ArgLstContext):
        variableLst = []
        x = ctx.varLst()
        for i in x:
            a = self.visit(i)
            for k in a:
                variableLst.append(k)
        return variableLst

    def visitVarType(self ,ctx :MPParser.VarTypeContext):
        # return IntType() if ctx.INTEGERTYPE() else StringType()
        if ctx.INTEGERTYPE():
            return IntType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.REALTYPE():
            return FloatType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        # return arrayTYPE
        else:
            return ArrayType()

    # stmtCompound: BEGIN stmt* END;
    def visitStmtCompound(self ,ctx :MPParser.StmtCompoundContext):
        returnlist = []
        # Alway return List because of MP.g4
        x = ctx.stmt()
        if x:
            for i in x:
                a = self.visit(i)
                # print("here")
                # print(a)
                # print(returnlist)
                # print("here 2")
                if isinstance(a, list):
                    for j in a:
                        returnlist.append(j)
                else:
                    returnlist.append(a)
        else: returnlist = []
        # if x:
        #     for i in x:
        #         returnlist.append(self.visit(i))
        # else: returnlist = []
        return returnlist
        # print("here")
        # print(self.visit(ctx.getChild(1)))
        # print("here 2")
        # return self.visit(ctx.getChild(1))

    # If you do not write this method, research what happen? Not override ParentNode.
    # Note that: ParentNote only visit ChildNode but return value "None"
    # stmt: stmtAssign SEMICOLON | stmtIf | stmtWhile | .............
    def visitStmt(self, ctx:MPParser.StmtContext):
        # if ctx.stmtAssign():
        #     return self.visit(ctx.stmtAssign())
        return self.visit(ctx.getChild(0))

    # stmtAssign: expr (ASSIGNOP expr)* ASSIGNOP expr ;
    def visitStmtAssign(self, ctx:MPParser.StmtAssignContext):
        returnLst = []
        x = ctx.expr()
        # y = ctx.getChildCount()
        i = 0
        while i < (len(x) - 1):
            returnLst.append(Assign(self.visit(x[i]),self.visit(x[i+1])))
            i = i + 1
        return returnLst[::-1]
        # return returnLst

    # stmtIf: IF expr THEN stmt (ELSE stmt)?;
    def visitStmtIf(self, ctx:MPParser.StmtIfContext):
        # returnLst = []
        thenStmt = []
        elseStmt = []
        if ctx.getChildCount() == 4:
            # print("here")
            checklist = self.visit(ctx.stmt()[0])
            # print("here 3")
            if isinstance(checklist, list):
                for i in checklist:
                    thenStmt.append(i)
            else: thenStmt.append(checklist)
        else:
            checklistThen = self.visit(ctx.stmt()[0])
            checklistElse = self.visit(ctx.stmt()[1])
            if isinstance(checklistThen, list):
                for i in checklistThen:
                    thenStmt.append(i)
            else: thenStmt.append(checklistThen)
            if isinstance(checklistElse, list):
                for i in checklistElse:
                    elseStmt.append(i)
            else: elseStmt.append(checklistElse)
        returnObj = If(self.visit(ctx.expr()), thenStmt, elseStmt)
        # print(type(returnObj))
        # print("here 2")
        return returnObj

    # stmtWhile: WHILE expr DO stmt;
    def visitStmtWhile(self, ctx:MPParser.StmtWhileContext):
        stmtLst = []
        checkLst = self.visit(ctx.stmt())
        if isinstance(checkLst, list):
            for i in checkLst:
                stmtLst.append(i)
        else: stmtLst.append(checkLst)
        return While(self.visit(ctx.expr()), stmtLst)

    # stmtFor: FOR ID ASSIGNOP expr (TO | DOWNTO) expr DO stmt;
    def visitStmtFor(self, ctx:MPParser.StmtForContext):
        stmtLst = []
        checkLst = self.visit(ctx.stmt())
        if isinstance(checkLst, list):
            for i in checkLst:
                stmtLst.append(i)
        else:
            stmtLst.append(checkLst)
        if (ctx.getChild(4).getText() == "to"):
            up = BooleanLiteral("true")
        else:
            up = BooleanLiteral("false")
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr()[0]), self.visit(ctx.expr()[1]), up, stmtLst)

    def visitStmtBreak(self, ctx:MPParser.StmtBreakContext):
        # print("here")
        return Break()

    def visitStmtContinue(self, ctx:MPParser.StmtContinueContext):
        # print("here 2")
        # returnLst = []
        # print(type(x))
        return Continue()

    # stmtReturn: RETURN expr?;
    def visitStmtReturn(self, ctx:MPParser.StmtReturnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else: return Return()

    # stmtWith: WITHSTMT (varLst SEMICOLON)+ DO stmt;
    def visitStmtWith(self, ctx:MPParser.StmtWithContext):
        return

    # stmtCall: ID LRB (expr (COMMA expr)*)? RRB;
    def visitStmtCall(self, ctx:MPParser.StmtCallContext):
        return

    # expr: expr ( ORELSEOP | ANDTHENOP ) term1 | term1;
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visit(ctx.getChild(0))

    def visitTerm1(self, ctx:MPParser.Term1Context):
        return self.visit(ctx.getChild(0))

    def visitTerm2(self, ctx:MPParser.Term2Context):
        return self.visit(ctx.getChild(0))

    def visitTerm3(self, ctx:MPParser.Term3Context):
        return self.visit(ctx.getChild(0))

    def visitTerm4(self, ctx:MPParser.Term4Context):
        return self.visit(ctx.getChild(0))

    def visitTerm5(self, ctx:MPParser.Term5Context):
        if ctx.getChildCount() == 1:
            if ctx.IntLit():
                return IntLiteral(int(ctx.IntLit().getText()))
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.RealLit():
                return FloatLiteral(ctx.RealLit())
            elif ctx.BoolLit():
                return BooleanLiteral(ctx.BoolLit())
            elif ctx.StrLit():
                return StringLiteral(ctx.StrLit().getText())
            # Return stmtCall
            else:
                return
        else:
            return None


    # def visitProgram(self ,ctx :MPParser.ProgramContext):
    #     return Program([self.visit(x) for x in ctx.decl()])
    #
    # def visitFuncdecl(self ,ctx :MPParser.FuncdeclContext):
    #     local ,cpstmt = self.visit(ctx.body())
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))
    #
    # def visitProcdecl(self ,ctx :MPParser.ProcdeclContext):
    #     local ,cpstmt = self.visit(ctx.body())
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt)
    #
    # def visitBody(self ,ctx :MPParser.BodyContext):
    #     return [] ,[self.visit(ctx.stmt())] if ctx.stmt() else []
    #
    # def visitStmt(self ,ctx :MPParser.StmtContext):
    #     return self.visit(ctx.funcall())
    #
    # def visitFuncall(self ,ctx :MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()) ,[self.visit(ctx.exp())] if ctx.exp() else [])
    #
    # def visitExp(self ,ctx :MPParser.ExpContext):
    #     return IntLiteral(int(ctx.INTLIT().getText()))
    #
    # def visitMtype(self ,ctx :MPParser.MtypeContext):
    #     return IntType()