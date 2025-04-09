import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import gzip,shutil,os,json,winreg,subprocess
import CustonJson,Window,NameData

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)


class Artifact_Blueprint_Editor:
    def __init__(self, master, data_handler):
        self.master = master
        self.data_handler = data_handler  # 数据操作接口
        self.frame = tk.Frame(master)
        self.frame.pack()
        self._setup_ui()

    def _setup_ui(self):
        # 初始化制品和蓝图UI（同之前）
        frame_artifact = tk.Frame(self.frame)
        frame_artifact.pack(side=tk.LEFT, padx=10, expand=True)
        # 制品列表
        self.artifact_tree = ttk.Treeview(frame_artifact,columns=("id","name"),show="headings",selectmode="browse")
        self.artifact_tree.heading("id",text="ID")
        self.artifact_tree.column("id",width=28)
        self.artifact_tree.heading("name",text=get_text("tree_artifact"))
        self.artifact_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 相关控件
        artifact_control_frame = tk.Frame(frame_artifact)
        artifact_control_frame.pack(side=tk.RIGHT, padx=10)
        self.artifact_box = ttk.Combobox(artifact_control_frame, values=NameData.artifacts.name_list, state="disabled", width=18)
        self.artifact_box.pack(pady=(0, 12))
        tk.Button(artifact_control_frame, text=get_text("btn_add"), width=8, command=self.add_artifact).pack(fill=tk.X, pady=12)
        tk.Button(artifact_control_frame, text=get_text("btn_delete"), width=8, command=self.remove_artifact).pack(fill=tk.X, pady=12)

        frame_blueprint = tk.Frame(self.frame)
        frame_blueprint.pack(side=tk.LEFT, padx=10, expand=True)
        # 蓝图列表
        self.blueprint_tree = ttk.Treeview(frame_blueprint,columns=("id","name"),show="headings",selectmode="browse")
        self.blueprint_tree.heading("id",text="ID")
        self.blueprint_tree.column("id",width=28)
        self.blueprint_tree.heading("name",text=get_text("tree_blueprint"))
        self.blueprint_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 相关控件
        blueprint_control_frame = tk.Frame(frame_blueprint)
        blueprint_control_frame.pack(side=tk.RIGHT, padx=10)
        self.blueprint_box = ttk.Combobox(blueprint_control_frame, values=NameData.blueprints.name_list, state="disabled", width=20)
        self.blueprint_box.pack(pady=(0, 12))
        # tk.Button(blueprint_control_frame, text="添加", width=8).pack(fill=tk.X, pady=12)
        tk.Button(blueprint_control_frame, text=get_text("btn_modify"), width=8, command=self.modify_blueprint).pack(fill=tk.X, pady=12)
        # tk.Button(blueprint_control_frame, text="删除", width=8).pack(fill=tk.X, pady=12)

    def add_artifact(self):
        print("1")

    def remove_artifact(self):
        print("2")

    def modify_blueprint(self):
        print("2")


    def refresh(self):
        self.data_handler

class Numeric_Editor:
    def __init__(self, master, data_handler):
        self.master = master
        self.data_handler = data_handler  # 数据操作接口
        self.frame = tk.Frame(master)
        self.frame.pack()
        self._setup_ui()

    def _setup_ui(self):
        frame_group = tk.Frame(self.frame)
        frame_group.pack(side=tk.LEFT, padx=10, expand=True)
        # 章节
        tk.Label(frame_group, text=get_text("label_chapter")).grid(row=0, column=0, sticky="e", pady=12)
        self.numeric_stageDefinition_box = ttk.Combobox(frame_group,values=NameData.maps.name_list,state="disable",width=16)
        self.numeric_stageDefinition_box.grid(row=0, column=1, sticky="ew", pady=12)
        self.numeric_stageDefinition_box.bind("<<ComboboxSelected>>",self.mix_stageDefinitionID)
        # 关卡
        tk.Label(frame_group, text=get_text("label_day")).grid(row=1, column=0, sticky="e", pady=12)
        self.numeric_stageDefinitionID_box = ttk.Combobox(frame_group,values=NameData.level_day,state="disable",width=16)
        self.numeric_stageDefinitionID_box.grid(row=1, column=1, sticky="ew", pady=12)
        self.numeric_stageDefinitionID_box.bind("<<ComboboxSelected>>",self.mix_stageDefinitionID)
        # 旗帜
        tk.Label(frame_group, text=get_text("label_flag")).grid(row=2, column=0, sticky="e", pady=12)
        self.numeric_flag_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_flag), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_flag_input.grid(row=2, column=1, sticky="ew", pady=12)
        # 波数
        tk.Label(frame_group, text=get_text("label_wave")).grid(row=3, column=0, sticky="e", pady=12)
        self.numeric_wave_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_wave), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_wave_input.grid(row=3, column=1, sticky="ew", pady=12)
        # 当前机械能
        tk.Label(frame_group, text=get_text("label_energy")).grid(row=0, column=2, sticky="e", pady=12)
        self.numeric_energy_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_energy), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_energy_input.grid(row=0, column=3, sticky="ew", pady=12)
        # 机械能上限
        tk.Label(frame_group, text=get_text("label_maxEnergy")).grid(row=1, column=2, sticky="e", pady=12)
        self.numeric_maxEnergy_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_maxEnergy), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_maxEnergy_input.grid(row=1, column=3, sticky="ew", pady=12)
        # 星之碎片数
        tk.Label(frame_group, text=get_text("label_starshard")).grid(row=2, column=2, sticky="e", pady=12)
        self.numeric_starshardCount_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_starshardCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_starshardCount_input.grid(row=2, column=3, sticky="ew", pady=12)
        # 星之碎片槽
        tk.Label(frame_group, text=get_text("label_maxStarshard")).grid(row=3, column=2, sticky="e", pady=12)
        self.numeric_starshardSlotCount_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_starshardSlotCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_starshardSlotCount_input.grid(row=3, column=3, sticky="ew", pady=12)
        # 启用传送带
        tk.Label(frame_group, text=get_text("label_conveyor")).grid(row=0, column=4, sticky="e", pady=12)
        self.numeric_isConveyorMode_box = ttk.Combobox(frame_group,values=[get_text("True"),get_text("False")],state="disable",width=16)
        self.numeric_isConveyorMode_box.grid(row=0, column=5, sticky="ew", pady=12)
        self.numeric_isConveyorMode_box.bind("<<ComboboxSelected>>",self.is_ConveyorMode)
        # 传送带槽数
        tk.Label(frame_group, text=get_text("label_conveyorslot")).grid(row=1, column=4, sticky="e", pady=12)
        self.numeric_conveyorSlotCount_input = ttk.Entry(frame_group, state="disable", textvariable=0, validate='key',validatecommand=(self.master.register(self.change_conveyorSlotCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_conveyorSlotCount_input.grid(row=1, column=5, sticky="ew", pady=12)
        # 背景音乐
        tk.Label(frame_group, text=get_text("label_bgm")).grid(row=2, column=4, sticky="e", pady=12)
        self.numeric_musicID_box = ttk.Combobox(frame_group,values=NameData.musics.name_list,state="disable",width=16)
        self.numeric_musicID_box.grid(row=2, column=5, sticky="ew", pady=12)
        self.numeric_musicID_box.bind("<<ComboboxSelected>>",self.change_musicID)
        # 自动收集
        tk.Label(frame_group, text=get_text("label_autoCollect")).grid(row=0, column=6, sticky="e", pady=12)
        self.numeric_autoCollect_box = ttk.Combobox(frame_group,values=[get_text("True"),get_text("False")],state="disable",width=16)
        self.numeric_autoCollect_box.grid(row=0, column=7, sticky="ew", pady=12)
        self.numeric_autoCollect_box.bind("<<ComboboxSelected>>",self.is_aotuCollect)
        # 蓝图无冷却
        tk.Label(frame_group, text=get_text("label_recharge")).grid(row=1, column=6, sticky="e", pady=12)
        self.numeric_recharge_box = ttk.Combobox(frame_group,values=[get_text("True"),get_text("False")],state="disable",width=16)
        self.numeric_recharge_box.grid(row=1, column=7, sticky="ew", pady=12)
        self.numeric_recharge_box.bind("<<ComboboxSelected>>",self.change_rechargeSpeed)
        # 忽略大波事件
        tk.Label(frame_group, text=get_text("label_ignoreHugeWaveEvent")).grid(row=2, column=6, sticky="e", pady=12)
        self.numeric_ignoreHugeWaveEvent_box = ttk.Combobox(frame_group,values=[get_text("True"),get_text("False")],state="disable",width=16)
        self.numeric_ignoreHugeWaveEvent_box.grid(row=2, column=7, sticky="ew", pady=12)
        self.numeric_ignoreHugeWaveEvent_box.bind("<<ComboboxSelected>>",self.is_ignoreHugeWaveEvent)

        tk.Button(frame_group, text=get_text("btn_about"),command=self.open_about).grid(row=3,column=4,columnspan=4,ipadx=64)

    # region 响应回调
    # 混乱
    def mix_stageDefinitionID(self,event):
        print("3")
    # 旗数
    def change_flag(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 波数
    def change_wave(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 当前机械能
    def change_energy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 机械能上限
    def change_maxEnergy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 星之碎片数
    def change_starshardCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 星之碎片槽
    def change_starshardSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 是否启用传送带
    def is_ConveyorMode(self,event):
        print("3")
    # 传送带槽数
    def change_conveyorSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        print("3")
    # 背景音乐
    def change_musicID(self,event):
        print("3")
    # 自动收集
    def is_aotuCollect(self,event):
        print("3")
    # 蓝图无冷却
    def change_rechargeSpeed(self,event):
        print("3")
    # 忽略大波事件
    def is_ignoreHugeWaveEvent(self,event):
        print("3")
    # 关于
    def open_about(self):
        Window.AboutWindow(self.master)
    # endregion

# 数据处理器（解耦核心逻辑）
class DataHandler:
    def __init__(self):
        self.current_data = None
    
    def add_artifact(self, artifact):
        self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'].append(artifact)
    
    def set_flag(self, value):
        self.current_data['level']['currentFlag'] = value

