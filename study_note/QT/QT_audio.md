# 在QT中调用麦克风

## QT支持的多媒体功能
备注：要在QT中使用多媒体功能，现在.pro配置文件中加上'QT += multimedia'  
1. 访问原始音频设备进行输入和输出
2. 低延迟播放音频文件，如WAV文件
3. 使用播放列表播放压缩的音频和视频文件，如mp3、wmv等
4. 录制声音并压制文件
5. 音频文件解码到内存进行处理
6. 使用摄像头进行预览、拍照和视频录制
7. 录制音频或视频时，访问其视频帧或音频缓冲区


## PCM音频数据
1. 基本概念
PCM(Pulse Code Modulation，脉冲编码调制)音频数据是未经压缩的音频采样数据裸流  
它是由模拟信号经过采样、量化、编码转换成的标准数字音频数据  
在windows中的文件格式是以.pcm为后缀  
2. PCM数据的6个参数
ample Rate : 采样频率  
Sample Size : 量化位数  
Number of Channels : 通道个数  
Sign : 表示样本数据是否是有符号位  
Byte Ordering : 字节序  
Integer Or Floating Point : 整形或浮点型  


## QAudioInput
QAudioInput类提供了接口用来访问音频输入设备中的原始音频输入数据  
QAudioInput是低层次的实现，直接控制音频输入设备的参数，并将音频录制数据写入一个流设备  
**QAudio参数含义**
QAudio的各种参数值及含义，详见帮助中的'QAudio Namespace'  
**常用函数**
1. QAudioInput::QAudioInput(const QAudioDeviceInfo &audioDevice, const QAudioFormat &format = QAudioFormat(), QObject \*parent = nullptr)
用QAudioInput的构造函数创建一个QAudioInput对象实例  
第一个参数是一个QAudioDeviceInfo对象，一般可以用default函数返回的对象  
第二个参数是一个已经设置好参数的QAudioFormat对象  
```
myinput = new QAudioInput(myinfo, myformat, this);
```
2. int QAudioInput::bufferSize() const
查询缓冲区的大小，如果没有设置，则返回当前平台的默认值  
3. void setBufferSize(int value)
设置缓冲区的大小()，只能在start()函数调用之前进行设置，之后就没用了  
4. void QAudioInput::start(QIODevice \*device)
开始从系统的音频输入中向一个设备传输音频数据  
注意：这个设备必须是已打开的，且是以WriteOnly、Append、ReadWrite这三个模式打开的  
```
myinput -> start(&myfile);//参数是一个QIODevice对象，包括QFile对象
```
5. void QAudioInput::stop()
停止录音，释放系统资源  
6. QAudio::State QAudioInput::state() const
返回当前音频录入的状态码，其中0代表录音正常，1代表录音暂停、2代表录音停止  
参数的具体含义，详见QT帮助的QAudio Namespace  
7. QAudio::Error QAudioInput::error() const
返回音频录入的错误码，其中0代表没有错误  
参数的具体含义，详见QT帮助的QAudio Namespace  


## QAudioRecorder
QAudioRecorder类用来录制编码的音频数据  
QAudioRecorder是高层次的实现，输入的音频数据直接保存为文件  


## QAudioInput和QAudioRecorder的不同
1. QAudioInput创建时指定的QAudioFormat将直接作用于音频输入设备  
即音频输入的数据将直接按照设置的参数进行采样  
而QAudioRecorder不能直接控制采样字长、采样点类型等底层参数  
2. QAudioInput::start(QIODevice \*device)函数会指定一个QIODevice设备作为数据输出对象，可以是文件，也可以是从QIODevice继承的类  
而QAudioRecorder只能指定文件来作为保存对象，不能进行底层的音频输入控制  


## QAudioDeviceInfo
QAudioDeviceInfo类提供了接口用来查询音频输入和输出设备及其相关功能  
通过查询可以得到当前设备的格式，排序，通道，编码器，频率，采样率等等  
**常用函数**
1. bool QAudioDeviceInfo::isNull() const
检查QAudioDeviceInfo对象是否有合法的设备定义  
2. QList<QAudioDeviceInfo> QAudioDeviceInfo::availableDevices(QAudio::Mode mode)
返回支持mode的音频设备列表，列表中都是QAudioDeviceInfo对象，例如：  
```
device_list = QAudioDeviceInfo::availableDevices(QAudio::AudioInput);
```
3. QString QAudioDeviceInfo::deviceName() const
返回一个人类可读的音频设备名  
4. QString QAudioDeviceInfo::realm() const
返回代表音频控件的key  
5. QStringList QAudioDeviceInfo::supportedCodecs() const
返回设置支持的编码列表(所有平台和控件都应该支持'audio/pcm')  
6. QList<int> supportedChannelCounts() const
返回支持通道数的列表(一般列表长度就代表设备支持的最大通道数)  
7. [static] QAudioDeviceInfo QAudioDeviceInfo::defaultInputDevice()
返回一个QAudioDeviceInfo对象，里面包含默认音频输入设备的信息  
8. [static] QAudioDeviceInfo QAudioDeviceInfo::defaultOutputDevice()
返回一个QAudioDeviceInfo对象，里面包含默认音频输出设备的信息  
9. bool QAudioDeviceInfo::isFormatSupported(const QAudioFormat &settings) const
判断当前的音频输入设备是否支持QAudioFormat对象的设置  
```
myinfo = QAudioDeviceInfo::defaultInputDevice();
bool mybool = myinfo.isFormatSupported(myformat);
```
10. QAudioFormat QAudioDeviceInfo::nearestFormat(const QAudioFormat &settings) const
返回一个最接近系统支持格式的QAudioFormat对象  
```
myformat = info.nearestFormat(myformat);
```


## QAudioFormat
QAudioFormat类存储了音频流的参数信息，可以查看和设置这些参数  
**常用参数**
QAudioFormat类主要是关于编码格式的，另外还有其他参数来描述音频流：  
Sample Rate：每秒的采样频率(一般是8000或16000)  
Number of channels：通道的数量(一般单声道是一个通道，立体声是两个通道)  
Sample size：音频数据的位长(一般8位或16位)  
Sample type：音频的数字表示(一般signed integer、unsigned integer、float)  
Byte order：音频的字节顺序(一般little endian低位优先、big endian高位优先)  
big endian是指低地址存放最高有效字节（MSB，Most Significant Bit）  
little endian则是低地址存放最低有效字节（LSB，Least Significant Bit）  
**常用函数**
1. void setChannelCount(int channels)
设置通道数量  
2. void setSampleRate(int samplerate)
设置采样频率  
3. void setSampleSize(int sampleSize)
设置音频位长
4. void setSampleType(QAudioFormat::SampleType sampleType)
设置音频的数字表示形式，可用参数包括：  
QAudioFormat::Unknown  
QAudioFormat::SignedInt  
QAudioFormat::UnSignedInt  
QAudioFormat::Float  
```
myformat.setSampleType(QAudioFormat::UnSignedInt);
```
5. QAudioFormat::SampleType sampleType() const
查询当前音频的数字表示形式，返回值包括：  
0：表示未设置  
1：表示SignedInt  
2：表示UnSignedInt  
3：表示Float  
6. void setCodec(const QString &codec)
设置编码形式  
```
myformat.setCodec("audio/pcm");
```



