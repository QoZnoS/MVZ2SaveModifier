import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import gzip,shutil,os,json,winreg,subprocess
import CustonJson,Window,NameData

class Artifact_Blueprint_Editor:
    def __init__(self, master, data_handler):
        self.master = master
        self.data_handler = data_handler  # 数据操作接口
        self.frame = tk.Frame(master)
        self._setup_ui()

    def _setup_ui(self):
        # 初始化制品和蓝图UI（同之前）
        print("setup ui")



# 数据处理器（解耦核心逻辑）
class DataHandler:
    def __init__(self):
        self.current_data = None
    
    def add_artifact(self, artifact):
        self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'].append(artifact)
    
    def set_flag(self, value):
        self.current_data['level']['currentFlag'] = value

