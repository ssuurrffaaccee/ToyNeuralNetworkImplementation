from Operators import *
from Tensor import ParameterTensor,InputTensor
def TestAdd():
    Tensor1=InputTensor(np.ones((10,10)))
    Tensor2=InputTensor(np.ones((10,10)))
    Result1=OAdd().RegisteForward()(Tensor1,Tensor2)
    Tensor3=ParameterTensor(np.ones((10,10)))
    Result2=OAdd().RegisteForward()(Tensor1,Tensor3)
    Result3=OAdd().RegisteForward()(Result2,Result1)
    Forward()
    Backward()
    print(Result3.Data)
    print(Result3.Grad)
    print(Tensor3.Grad)
    print(Tensor3.Grad)
    print(Tensor1.Grad)
    print(Tensor2.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestMinus():
    Tensor1=ParameterTensor(np.ones((10,10)))
    Tensor2=ParameterTensor(np.ones((10,10)))
    Result=OMinus().RegisteForward()(Tensor1,Tensor2)
    Tensor3=ParameterTensor(np.ones((10,10)))
    Result2=OMinus().RegisteForward()(Result,Tensor3)
    Forward()
    Backward()
    #print(Result.Data)
    #print(Result.Grad)
    print(Tensor1.Grad)
    print(Tensor2.Grad)
    print(Result.Grad)
    print(Tensor3.Grad)
    print(Result2.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestMul():
    Tensor1=ParameterTensor(np.random.randn(10,10))
    Tensor2=ParameterTensor(np.ones((10,10)))
    Result=OMul().RegisteForward()(Tensor1,Tensor2)
    #Tensor3=ParameterTensor(np.ones((10,10)))
    #Result2=OMinus().RegisteForward()(Result,Tensor3)
    Forward()
    Backward()
    #print(Result.Data)
    #print(Result.Grad)
    print(Tensor1.Grad)
    print(Tensor2.Grad)
    #print(Result.Grad)
    #print(Tensor3.Grad)
    #print(Result2.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestMatMul():
    Tensor1=ParameterTensor(np.ones((10,10)))
    Tensor2=ParameterTensor(np.ones((10)))
    Result=OMatMul().RegisteForward()(Tensor1,Tensor2)
    Result1=OMatMul().RegisteForward()(Tensor1,Result)
    Forward()
    Backward()
    print(Result1.Data)
    print(Result1.Grad)
    print(Tensor1.Grad)
    print(Tensor2.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestSelect():
    Tensor1=ParameterTensor(np.ones((10,10)))
    Result1=OSelect("CNN").RegisteForward()(Tensor1,[2,6,3,7])
    Result2=OSelect("CNN").RegisteForward()(Tensor1,[3,7,2,6])
    Result=OAdd().RegisteForward()(Result1,Result2)
    Forward()
    Backward()
    print(Tensor1.Grad)
    print(Result1.Data)
    print(Result1.Grad)
    print(Result2.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestRelu():
    Tensor1=ParameterTensor(np.random.randn(10,10))
    Tensor2=ParameterTensor(np.ones([10,10]))
    Result=OMul().RegisteForward()(Tensor1,Tensor2)

    Result1=ORelu().RegisteForward()(Result)
    Forward()
    Backward()
    print(Tensor1.Data)
    print(Result1.Data)
    print(Result1.Grad)
    print(Result.Grad)
    print(Tensor2.Grad)
    #print(Result.Data)
    #print(Result1.Grad)
    #print(Result1.Data)
    #print(Result.Grad)
    #print(Tensor1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestSigmoid():
    Tensor1=ParameterTensor(np.zeros((10,10)))
    Result=OSigmoid().RegisteForward()(Tensor1)
    Forward()
    Backward()
    print(Result.Data)
    print(Result.Grad)
    print(Tensor1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestDropout():
    Tensor1=ParameterTensor(np.random.randn(10,10))
    Result=ODropout().RegisteForward()(Tensor1)
    Forward()
    Backward()
    print(Result.Data)
    print(Result.Grad)
    print(Tensor1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestSum():
    Tensor1=ParameterTensor(np.random.randn(10,10))
    Result=OAdd().RegisteForward()(Tensor1,Tensor1)
    Result1=OSum().RegisteForward()(Result)
    Forward()
    Backward()
    print(Tensor1.Data)
    print(Tensor1.Grad)
    print(Result.Data)
    print(Result.Grad)
    print(Result1.Data)
    print(Result1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestConcat():
    Tensor1=ParameterTensor(np.random.randn(2,5))
    Tensor2=ParameterTensor(np.random.randn(1,5))
    Tensor3=ParameterTensor(np.random.randn(3,5))
    Result=OConcat().RegisteForward()([Tensor1,Tensor2,Tensor3])
    Tensor4=ParameterTensor(np.random.randn(6,5))
    Result1=OMul().RegisteForward()(Result,Tensor4)
    Forward()
    Backward()
    print(Tensor4.Data)
    print(Tensor1.Grad)
    print(Tensor2.Grad)
    print(Tensor3.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestTrans():
    Tensor1=ParameterTensor(np.random.randn(2,5))
    Result=OTranspose().RegisteForward()(Tensor1)
    Tensor2=ParameterTensor(np.random.randn(5,2))
    Result1=OMul().RegisteForward()(Result,Tensor2)
    Forward()
    Backward()
    print(Tensor2.Data)
    print(Result.Grad)
    print(Tensor1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestSoftmax():
    Tensor1=ParameterTensor(np.array([1,2,3]))
    Result=OSoftmaxForEval().RegisteForward()(Tensor1)
    Forward()
    print(Result.Data)
    Backward()
    print(Result.Grad)
    print(Tensor1.Grad)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestSoftmaxEntropy():
    Tensor1=ParameterTensor(np.array([100,1,150]))
    LabelOneHot=InputTensor(np.array([0,0,1]))
    Result=OSoftmaxEntropy().RegisteForward()(Tensor1,LabelOneHot)
    Forward()
    Backward()
    print(Result.Grad)
    print(Result.Data)
    print(LabelOneHot.Grad)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestMaxPool():
    Tensor1=ParameterTensor(np.random.randn(8,8))
    Result=OMaxPool().RegisteForward()(Tensor1,[4,4])
    Forward()
    Backward()
    print(Result.Grad)
    print(Result.Data)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestFlatten():
    Tensor1=ParameterTensor(np.random.randn(2,2))
    Result=OFlatten().RegisteForward()(Tensor1)
    Forward()
    Backward()
    print(Result.Grad)
    print(Result.Data)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestMaxSoft():
    Tensor1=ParameterTensor(np.random.randn(3,1))
    Result=OSoftmax().RegisteForward()(Tensor1)
    Forward()
    Backward()
    print(Result.Grad)
    print(Result.Data)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestEntropy():
    Tensor1=ParameterTensor(np.array([0.9,0.1]))
    Tensor2=ParameterTensor(np.array([0.1,0.9]))
    Result=OEntropy().RegisteForward()(Tensor1,Tensor2)
    Forward()
    Backward()
    print(np.sum(np.array([0.1,0.9])*np.log(np.array([0.9,0.1]))))
    print(Result.Grad)
    print(Result.Data)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    print(Tensor2.Grad)
    print(Tensor2.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
def TestTanh():
    Tensor1=ParameterTensor(np.ones([10,1])*10)
    Result=OTanh().RegisteForward()(Tensor1)
    Forward()
    Backward()
    print(Result.Grad)
    print(Result.Data)
    print(Tensor1.Grad)
    print(Tensor1.Data)
    GOperatorManager.Clear()
    GDataNodeManager.Clear()
#TestAdd()
#TestMinus()
#TestMul()
#TestMatMul()
#TestSelect()
#
# TestRelu()
#TestSum()
#TestConcat()
#TestTrans()
#TestSigmoid()
#TestDropout()
#TestSoftmax()
#TestSoftmaxEntropy()
#TestNormal()
#TestMaxPool()
#TestFlatten()
#TestMaxSoft()
#TestEntropy()
TestTanh()