from gradio_client import Client
import shutil
import sys,os

sys.path.append(os.path.split(sys.path[0])[0])
path = os.path.split(sys.path[0])[0]
print(os.path.split(sys.path[0])[0])

def text2voice(text):
    client = Client("https://www.modelscope.cn/api/v1/studio/MiDd1Eye/DZ-Bert-VITS2/gradio/")
    result = client.predict(
        text,  # str in 'Text' Textbox component
        "Speaker",  # str (Option from: ['Speaker']) in 'Speaker' Dropdown component
        0.1,  # int | float (numeric value between 0.1 and 1) in 'SDP/DP混合比' Slider component
        0.2,  # int | float (numeric value between 0.1 and 1) in '感情调节' Slider component
        0.1,  # int | float (numeric value between 0.1 and 1) in '音素长度' Slider component
        0.8,  # int | float (numeric value between 0.1 and 2) in '生成长度' Slider component
        fn_index=0
    )

    # API返回的文件路径
    audio_file_path = result[1]

    # 保存音频的目标路径
    destination_path = path + '/my_game/sound/audio.wav'

    # 复制文件到新位置
    shutil.copy(audio_file_path, destination_path)
