## 怎么使用icefall训练模型？


1、环境要求
### 2、操作步骤
使用yesno数据集，有两个原因
- 非常小，12分钟的数据
- CPU上训练只需要20秒
注：除数据准备在Linux和Mac上运行，其它能在linux、mac、windows上运行。
#### 配置环境
1. 创建虚拟环境
2. 安装依赖
3. 安装icefall
#### 数据准备
```
cd /tmp/icefall
export PYTHONPATH=/tmp/icefall:$PYTHONPATH
cd egs/yesno/ASR
./prepare.sh
```

怎么准备自己的数据集。
参考：lhotse - 语音数据处理工具集
https://github.com/lhotse-speech/lhotse/tree/master/lhotse/recipes
生成目录说明：
download：包含下载的数据集文件
data/manifests:包含清单,用于在data/fbank中生成文件。
data/fbank:包含从数据/清单的所有内容。此外，它还包含用于训练的功能。
data/lang：包含词典
data/lm：语言模型
#### 训练
```
export PYTHONPATH=/tmp/icefall:$PYTHONPATH
cd egs/yesno/ASR
# We use CPU for training by setting the following environment variable
export CUDA_VISIBLE_DEVICES=""
./tdnn/train.py
```
#### 编码
```
cd /tmp/icefall
export PYTHONPATH=/tmp/icefall:$PYTHONPATH
cd egs/yesno/ASR

# We use CPU for decoding by setting the following environment variable
export CUDA_VISIBLE_DEVICES=""

./tdnn/decode.py
```
例如，您可以指定：
- --epoch哪个检查点用于解码
- --avg 模型平均的检查点数量
您通常尝试--epoch和--avg的不同组合，然后选择一个导致最低WER的组合
#### 导出模型
三种方式导出
- model.state_dict()导出模型参数
- torchscript导出：torc.jit.script()或torc.jit.trace()
- torc.ONNX.Export()导出到ONNX

安装适用于GPU的icefall
3、怎么去训练自己的数据集？
怎么调优？
看了icefall没有一个通用的方法。
需要懂原理，才能训练数据集。
开源的模型一般会把训练方法、数据都给出来，要跑起来其实还好。只要有自己的数据和明确的优化目的，都好说。
4、内部原理

1. 请下载模型
2. 解压
3. 阅读里面的 readme.md 
4. 找到 icefall 里的 pull request, 然后自己看代码

参数说明
https://github.com/k2-fsa/icefall/issues/1542

so库接口onnx和ncnn有个别方法不一样，可以考虑设计成一样方便切换。
原因是先有的ncnn，后面有的onnx onnx支持batch（ONNX支持batch操作，即可以对一批数据进行推理，这在实际应用中非常有用，因为可以提高推理效率）。