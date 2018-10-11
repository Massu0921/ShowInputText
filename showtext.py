# coding: utf-8
import tkinter as tk
import threading,time

# テキスト入力クラス
class InputText():
    # コンストラクタ
    def __init__(self):
        # 入力・表示テキスト
        self.text = 'init'

    # テキスト入力用
    def txt_input(self):
        # 無限
        while 1:
            # CUIからの入力
            self.text = input('Input Text:')

# GUIクラス 上のクラスを継承
class GUI(InputText):
    # コンストラクタ
    def __init__(self):
        # InputTextクラスのコンストラクタ呼び出し
        super().__init__()

        # スレッドの設定
        th_input = threading.Thread(target=self.txt_input) # スレッド用の関数をtargetで指定
        th_input.setDaemon(True) # メインスレッド(GUI)が終了するとこのスレッドも終了するように
        th_input.start() # スレッド(CUIからの入力)開始

        # tkinter
        self.root = tk.Tk()
        self.root.title('Test') # タイトル
        self.root.geometry('300x300') # ウインドウサイズ

        self.label = tk.Label(text='',font=("",40)) # ラベル設定 font=("フォント",フォントサイズ)
        self.label.pack() # ラベル配置

    # ウインドウ更新
    def window(self):
        # 念のためtry文使用
        try:
            # 無限ループ
            while 1:
                self.label.configure(text = self.text) # ラベルの内容更新
                self.root.update() # 表示更新
                time.sleep(0.1) # 待機(外してもよし)

        except:
            pass

if __name__ == '__main__':
    # インスタンス生成
    gui = GUI()
    # ウインドウ更新開始
    gui.window()
