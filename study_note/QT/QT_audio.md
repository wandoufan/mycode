# 在QT中调用麦克风

## QT支持的多媒体功能
备注：要在QT中使用多媒体功能，现在.pro配置文件中加上'QT += multimedia'  
1. 访问原始音频设备进行输入和输出
2. 低延迟播放音频文件，如WAV文件
3. 使用播放列表播放压缩的音频和视频文件，如mp3、wmv等
4. 录制声音并压制文件
5. 音频文件解码到内存进行处理
6. 使用摄像头进行预览、拍照和视频录制


## QAudioInput
QAudioInput类用来访问原始音频输入数据  
QAudioInput是低层次的实现，直接控制音频输入设备的参数，并将音频录制数据写入一个流设备  

## QAudioRecorder
QAudioRecorder类用来录制编码的音频数据  
QAudioRecorder是高层次的实现，输入的音频数据直接保存为文件  

## QAudioDeviceInfo
QAudioDeviceInfo类用来发现音频设备  
