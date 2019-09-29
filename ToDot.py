class Name:
    def __init__(self):
        self.Count=0
    def Reset(self):
        self.Count=0
    def GeName(self):
        Name= "N"+str(self.Count)
        self.Count=self.Count+1
        return Name
def ToDotFile(DataNode,FileName):
    Head="digraph{\n"
    Tail="}\n"
    NameGenerator=Name()
    NameEnv={}
    #print(type(DataNode))
    BodyString=GetName(DataNode,NameEnv,NameGenerator)+"[label=\""+str(DataNode.Data[0])+"\"];\n"
    BodyString=BodyString+BFS(DataNode,NameEnv,NameGenerator)
    WholeString=Head+BodyString+Tail
    with open(FileName,"w") as fd:
        fd.write(WholeString)
def GetName(DataNode,NameEnv,NameGenerator):
    try:
         return NameEnv[DataNode]
    except KeyError :
        Name=NameGenerator.GeName()
        NameEnv[DataNode]=Name
        return Name

def BFS(DataNode,NameEnv,NameGenerator):
    DefineString=""
    if DataNode.ParentDataNode!=[]:
        for Node in list(set(DataNode.ParentDataNode)):
            DefineString=DefineString+GetName(Node,NameEnv,NameGenerator)+"[label=\""+str(Node.Data[0])+"\"];\n"
    EdgeString=""
    ParentName=GetName(DataNode,NameEnv,NameGenerator)
    if DataNode.ParentDataNode!=[]:
        for Node in list(set(DataNode.ParentDataNode)):
            EdgeString=EdgeString+ParentName+"->"+GetName(Node,NameEnv,NameGenerator)+";\n"
    ChildrenString=""
    if DataNode.ParentDataNode!=[]:
        for Node in list(set(DataNode.ParentDataNode)):
            ChildrenString=ChildrenString+BFS(Node,NameEnv,NameGenerator)
    return DefineString+EdgeString+ChildrenString
from FunctionNode import *
from DataNode import *
def TestDot():
    Node1=ConstDataNode(3.0)
    Node2=GradDataNode(-2.0)
    AddNode1=Add()
    Node3=AddNode1.Forward(Node1,Node2)

    Node4=GradDataNode(-7.0)
    Node5=ConstDataNode(4.0)
    AddNode2=Add()
    Node6=AddNode2.Forward(Node4,Node5)


    AddNode3=Add()
    Node7=AddNode3.Forward(Node3,Node6)

    MulNode4=Mul()
    Node8=MulNode4.Forward(Node7,Node7)
    ReluNode=Relu()
    Node9=ReluNode.Forward(Node8)
    ToDotFile(Node9,"NN1.gv")
if __name__=="__main__":
    TestDot()