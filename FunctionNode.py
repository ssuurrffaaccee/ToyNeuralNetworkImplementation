from DataNode import *
class FunctionNode:
    def __init__(self):
        self.Output=[]
        self.Output.append(ConstDataNode(0.0))
    def Forward(self):
        pass

    def AddDataNodeConnection(self,OuputDataNode,InputDataNodes):
        OuputDataNode.Generator.append(self)
        for Node in InputDataNodes:
            OuputDataNode.ParentDataNode.append(Node)
    
    def GetInputs(self):
        return self.Output[0].ParentDataNode
    def GetOutput(self):
        return self.Output[0]
    def StoreToOutput(self,FloatNum):
        OutputNode=self.GetOutput()
        OutputNode.Data[0]=FloatNum
    def Backward(self):
        print(self.Output[0])
        OutputGrad=self.Output[0].Grad[0]
        Inputs=self.GetInputs()
        for DataNode in Inputs:
            LocalGrad=self.LocalGrad(DataNode)
            if len(DataNode.Grad)==0:
                DataNode.Grad.append(LocalGrad*OutputGrad)
            else:
                DataNode.Grad[0]=DataNode.Grad[0]+LocalGrad*OutputGrad
            
        for DataNode in list(set(Inputs)):
            if len(DataNode.Generator)!=0:
                DataNode.Generator[0].Backward() 
    def LocalGrad(self,DataNode):
        return []


def PrintFunctionNode(FunctionNode):
    print("-------------------")
    print(FunctionNode.Output)

class Add(FunctionNode):
    def __init__(self):
        super().__init__()
    def Forward(self,DataNode1,DataNode2):
        #Calculate
        Sum=DataNode1.Data[0]+DataNode2.Data[0]
        #Store
        OutputNode=self.GetOutput()
        OutputNode.Data[0]=Sum
        #Connection
        InputDataNodes=[DataNode1,DataNode2]
        self.AddDataNodeConnection(OutputNode,InputDataNodes)
        return OutputNode
    def LocalGrad(self,DataNode):
        return 1.0
class Mul(FunctionNode):
    def __init_(self):
        super().__init__()

    def Forward(self,DataNode1,DataNode2):
        #Calculate
        Mul=DataNode1.Data[0]*DataNode2.Data[0]
        
        #Store
        OutputNode=self.GetOutput()
        OutputNode.Data[0]=Mul
        #Connection
        InputDataNodes=[DataNode1,DataNode2]
        self.AddDataNodeConnection(OutputNode,InputDataNodes)
        return OutputNode
    def LocalGrad(self,DataNode):
        Inputs=self.GetInputs()
        if DataNode==Inputs[0]:
            return Inputs[1].Data[0]
        else:
            return Inputs[0].Data[0]

class Relu(FunctionNode):
    def __init__(self):
        super().__init__()
    def Forward(self,DataNode):
        #Calculate
        Result=max(0,DataNode.Data[0])
        
        #Store
        OutputNode=self.GetOutput()
        OutputNode.Data[0]=Result
        
        #Connection
        InputDataNodes=[DataNode]
        self.AddDataNodeConnection(OutputNode,InputDataNodes)
        return OutputNode
    def LocalGrad(self,DataNode):
        if DataNode.Data[0]>0:
            return 1.0
        else:
            return 0.0
def Test():
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
    Node9.Backward()
    PrintDataNode(Node1)
    PrintDataNode(Node2)
    PrintDataNode(Node3)
    PrintDataNode(Node4)
    PrintDataNode(Node5)
    PrintDataNode(Node6)
    PrintDataNode(Node7)
    PrintDataNode(Node8)
    PrintDataNode(Node9)
    PrintFunctionNode(AddNode1)
    PrintFunctionNode(AddNode2)
    PrintFunctionNode(AddNode3)
    PrintFunctionNode(MulNode4)
    PrintFunctionNode(ReluNode)
if __name__=="__main__":
    Test()