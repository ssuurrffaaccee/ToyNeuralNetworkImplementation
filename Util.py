from DataNode import *
from FunctionNode import *

#Store by Row
def Matrix(h,w,Data,DataNodeCreater=ConstDataNode):
    assert len(Data)==h*w
    return {"Dim":[h,w],"Data":[DataNodeCreater(Elem) for Elem in Data]}

def GetElem(HIndex,WIndex,Matrix):
    InnerHIndex=HIndex+1
    InnerWIndex=WIndex+1
    Index=((InnerHIndex-1)*Matrix["Dim"][1]+InnerWIndex)-1
    return Matrix["Data"][Index]

def TestGetElem():
    M=Matrix(2,3,[1,2,3,4,5,6])
    print(GetElem(1,1,M).Data)
    print(GetElem(1,2,M).Data)
    print(GetElem(0,0,M).Data)

def Vector(l,Data,DataNodeCreater=ConstDataNode):
    assert len(Data)==l
    return {"Dim":[l,1],"Data":[DataNodeCreater(Elem) for Elem in Data]}

def SumDataNodeList(List):
    Sum=List[0]
    for Elem in List[1:]:
        AddNode=Add()
        Sum=AddNode.Forward(Sum,Elem)
    return Sum

def SumVector(Vector):
    Data=Vector["Data"]
    return SumDataNodeList(Data)

def DotProductDataNodeList(List1,List2):
    Muls=[]
    for X,Y in zip(List1,List2):
        MulNode=Mul()
        Muls.append(MulNode.Forward(X,Y))
    return SumDataNodeList(Muls)

def DotProduct(Vector1,Vector2):
    assert Vector1["Dim"]==Vector2["Dim"]
    Data1=Vector1["Data"]
    Data2=Vector2["Data"]
    return DotProductDataNodeList(Data1,Data2)

def MatrixMul(Matrix1,Matrix2):
    def MulInIndex(HIndex,WIndex,Matrix1,Matrix2):
        Row=[]
        for i in range(Matrix1["Dim"][1]):
            Row.append(GetElem(HIndex,i,Matrix1))
        Column=[]
        for i in range(Matrix2["Dim"][0]):
            Column.append(GetElem(i,WIndex,Matrix2))
        return DotProductDataNodeList(Row,Column)
        
    Matrix1H=Matrix1["Dim"][0]
    Matrix1W=Matrix1["Dim"][1]
    Matrix2H=Matrix2["Dim"][0]
    Matrix2W=Matrix2["Dim"][1]
    assert Matrix1W==Matrix2H
    ResultH=Matrix1H
    ResultW=Matrix2W
    ResultData=[]
    for HIndex in range(ResultH):
        for WIndex in range(ResultW):
            ResultData.append(MulInIndex(HIndex,WIndex,Matrix1,Matrix2))
    return {"Dim":[ResultH,ResultW],"Data":ResultData}
from ToDot import ToDotFile
def TestMatrixMul():
    M=Matrix(20,20,[i+1 for i in range(20*20) ])
    V=Vector(20,[i+1 for i in range(20)])
    Result=SumVector(MatrixMul(M,V))
    PrintDataNode(Result)
    ToDotFile(Result,"NN3.gv")
    M=Matrix(2,3,[1,2,10,4,5,6])
    V=Vector(3,[1,2,3])
    Result=SumVector(MatrixMul(M,V))
    PrintDataNode(Result)
    ToDotFile(Result,"NN2.gv")
if __name__=="__main__":
    TestGetElem()
    TestMatrixMul()

