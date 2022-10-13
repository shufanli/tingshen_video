from moviepy.editor import AudioFileClip
import os

def main():

    mp4 = AudioFileClip("m3u8_mp4/yJUxvg.mp4")
    mp4.write_audiofile("m3u8_mp3/p1.mp3")
    print("导入完成")

if __name__ == "__main__":  # 当程序执行时
    main()
