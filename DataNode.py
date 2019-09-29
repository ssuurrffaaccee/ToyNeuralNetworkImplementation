class DataNode:
    def __init__(self):
        self.Data=[]
        self.Grad=[]
        self.Generator=[]
        self.Const=True
        self.ParentDataNode=[]
    def Backward(self):
        self.Grad.append(1.0)
        print(self)
        self.Generator[0].Backward()
class ConstDataNode(DataNode):
    def __init__(self,FloatNum):
        super().__init__()
        self.Const=True
        self.Data.append(FloatNum)
    
class GradDataNode(DataNode):
    def __init__(self,FloatNum):
        super().__init__()
        self.Const=False
        self.Data.append(FloatNum)

def PrintDataNode(DataNode):
    print("---------------------")
    print("--Data:")
    print(DataNode.Data)
    print("--Grad:")
    print(DataNode.Grad)
    print("--Generator:")
    print(DataNode.Generator)
    print("--ParentDatNode:")
    print(DataNode.ParentDataNode)