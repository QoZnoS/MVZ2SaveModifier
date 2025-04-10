import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import gzip,shutil,os,json,winreg,subprocess
import CustonJson,Window,NameData

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)

class DataHandler:
    def __init__(self):
        self.current_data = None
        self.missing = False
        self.missing_log = [] # 储存数据读取失败信息

    # 设计原则：set应只出现在回调中，防止存档数据被意外修改

    # region numeric
    def set_stageDefinitionID(self, value):
        self.current_data['level']['stageDefinitionID'] = str(value)

    def get_stageDefinitionID(self, default = None):
        try:
            return self.current_data['level']['stageDefinitionID']
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_stageDefinitionID'))
            self.missing = True
            return None

    def set_currentFlag(self, value):
        self.current_data['level']['currentFlag'] = int(value)

    def get_currentFlag(self, default = None):
        try:
            return self.current_data['level']['currentFlag']
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_currentFlag'))
            self.missing = True
            return None

    def set_currentWave(self, value):
        self.current_data['level']['currentWave'] = int(value)

    def get_currentWave(self, default = None):
        try:
            return self.current_data['level']['currentWave']
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_currentWave'))
            self.missing = True
            return None

    def set_energy(self, value):
        self.current_data['level']['energy'] = float(value)

    def get_energy(self, default = None):
        try:
            return self.current_data['level']['energy']
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_energy'))
            self.missing = True
            return None

    def set_maxEnergy(self, value):
        self.current_data['level']['Option']['maxEnergy'] = float(value)

    def get_maxEnergy(self, default = None):
        try:
            return self.current_data['level']['Option']['maxEnergy']
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_maxEnergy'))
            self.missing = True
            return None

    # endregion

    def check_missing(self):
        if self.missing:
            for label in self.missing_log:
                misslabel = label + "\n"
            messagebox.showinfo(get_text('info_missing'), misslabel)

# 各个分页

class Artifact_Blueprint_Editor:
    def __init__(self, master, data_handler:DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack()
        self._setup_ui()

    def _setup_ui(self):
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
    def __init__(self, master, data_handler:DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack()
        self._setup_ui()

    def _setup_ui(self):
        frame_group = tk.Frame(self.frame)
        frame_group.pack(side=tk.LEFT, padx=10, expand=True)

        self.entry_vars = {}
        # 章节
        self.numeric_stageDefinition_box = add_box(frame_group, "label_chapter", 0, 0, NameData.maps.name_list, self.mix_stageDefinitionID)
        # 关卡
        self.numeric_stageDefinitionID_box = add_box(frame_group, "label_day", 1, 0, NameData.level_day, self.mix_stageDefinitionID)
        # 旗帜
        self.numeric_flag_input = add_input(frame_group, "label_flag", 2, 0, self.master.register(self.change_flag))
        # 波数
        self.numeric_wave_input = add_input(frame_group, "label_wave", 3, 0, self.master.register(self.change_wave))
        # 当前机械能
        self.numeric_energy_input = add_input(frame_group, "label_energy", 0, 1, self.master.register(self.change_energy))
        # 机械能上限
        self.numeric_maxEnergy_input = add_input(frame_group, "label_maxEnergy", 1, 1, self.master.register(self.change_maxEnergy))
        # 星之碎片数
        self.numeric_starshardCount_input = add_input(frame_group, "label_starshard", 2, 1, self.master.register(self.change_starshardCount))
        # 星之碎片槽
        self.numeric_starshardSlotCount_input = add_input(frame_group, "label_maxStarshard", 3, 1, self.master.register(self.change_starshardSlotCount))
        # 启用传送带
        self.numeric_isConveyorMode_box = add_box(frame_group, "label_conveyor", 0, 2, [get_text("True"),get_text("False")], self.is_ConveyorMode)
        # 传送带槽数
        self.numeric_conveyorSlotCount_input = add_input(frame_group, "label_conveyorslot", 1, 2, self.master.register(self.change_conveyorSlotCount))
        # 背景音乐
        self.numeric_musicID_box = add_box(frame_group, "label_bgm", 2, 2, NameData.musics.name_list, self.change_musicID)
        # 自动收集
        self.numeric_autoCollect_box = add_box(frame_group, "label_autoCollect", 0, 3, [get_text("True"),get_text("False")], self.is_aotuCollect)
        # 蓝图无冷却
        self.numeric_recharge_box = add_box(frame_group, "label_recharge", 1, 3, [get_text("True"),get_text("False")], self.change_rechargeSpeed)
        # 忽略大波事件
        self.numeric_ignoreHugeWaveEvent_box = add_box(frame_group, "label_ignoreHugeWaveEvent", 2, 3, [get_text("True"),get_text("False")], self.is_ignoreHugeWaveEvent)

        tk.Button(frame_group, text=get_text("btn_about"),command=self.open_about).grid(row=3,column=4,columnspan=4,ipadx=64)

    # region 响应回调
    # 混乱
    def mix_stageDefinitionID(self,event):
        mapID = NameData.maps.get_id(self.numeric_stageDefinition_box.get())
        level = self.numeric_stageDefinitionID_box.get()
        isSpecial = (NameData.level_day.count(level)==0)
        if (mapID != "another"):
            if isSpecial:
                self.numeric_stageDefinitionID_box.config(values=NameData.level_day)
                self.numeric_stageDefinitionID_box.set(NameData.level_day[0])
            self.data_handler.set_stageDefinitionID(mapID + "_" + level)
        else:
            if not isSpecial:
                self.numeric_stageDefinitionID_box.config(values=NameData.levels.name_list)
                self.numeric_stageDefinitionID_box.set(NameData.levels.name_list[0])
            self.data_handler.set_stageDefinitionID(NameData.levels.get_id(level))
    # 旗数
    def change_flag(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.set_currentFlag(0)
            return True
        if value.isdigit():
            self.data_handler.set_currentFlag(value)
            return True
        return False
    # 波数
    def change_wave(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.set_currentWave(0)
            return True
        if value.isdigit():
            self.data_handler.set_currentWave(value)
            return True
        return False
    # 当前机械能
    def change_energy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.set_energy(0)
            return True
        try:
            self.data_handler.set_energy(value)
            return True
        except ValueError:
            return False
    # 机械能上限
    def change_maxEnergy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.set_maxEnergy(0)
            return True
        try:
            self.data_handler.set_maxEnergy(value)
            return True
        except ValueError:
            return False
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

    # region 刷新，读取参数
    def refresh(self):
        self.refresh_map_box()
        self.refresh_input(self.numeric_flag_input, self.data_handler.get_currentFlag())
        self.refresh_input(self.numeric_wave_input, self.data_handler.get_currentWave())
        self.refresh_input(self.numeric_energy_input, self.data_handler.get_energy())
        self.refresh_input(self.numeric_maxEnergy_input, self.data_handler.get_maxEnergy())
        # self.numeric_starshardCount_input.config(state="normal")
        # if not ('starshardCount' in self.current_data['level']['properties']):
        #     self.current_data['level']['properties']['starshardCount']=0
        # self.data_starshardCount.set(self.current_data['level']['properties']['starshardCount'])
        # self.numeric_starshardSlotCount_input.config(state="normal")
        # self.data_starshardSlotCount.set(self.current_data['level']['properties']['starshardSlotCount'])
        # self.refresh_boolean_box(self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'], self.numeric_isConveyorMode_box)
        # self.numeric_conveyorSlotCount_input.config(state="normal")
        # self.data_conveyorSlotCount.set(self.current_data['level']['conveyorSlotCount'])
        # self.numeric_musicID_box.config(state="readonly")
        # self.numeric_musicID_box.set(NameData.musics.get_name(self.current_data['musicID']))
        # if not ('autoCollect' in self.current_data['level']['properties']):
        #     self.current_data['level']['properties']['autoCollect']=False
        # self.refresh_boolean_box(self.current_data['level']['properties']['autoCollect'], self.numeric_autoCollect_box)
        # self.refresh_boolean_box((self.current_data['level']['rechargeSpeed'] != 1.0), self.numeric_recharge_box)
        # if not ('ignoreHugeWaveEvent' in self.current_data['level']['properties']):
        #     self.current_data['level']['properties']['ignoreHugeWaveEvent']=False
        # self.refresh_boolean_box(self.current_data['level']['properties']['ignoreHugeWaveEvent'], self.numeric_ignoreHugeWaveEvent_box)

    def refresh_map_box(self):
        stageDefinitionID = self.data_handler.get_stageDefinitionID()
        if stageDefinitionID == None:
            return
        try:
            if (NameData.levels.id_list.count(stageDefinitionID)!=0):
                self.numeric_stageDefinitionID_box.config(values=NameData.levels.name_list)
                self.numeric_stageDefinitionID_box.set(NameData.levels.get_name(stageDefinitionID))
                self.numeric_stageDefinition_box.set("another")
            else:
                self.numeric_stageDefinition_box.set(NameData.maps.get_name(stageDefinitionID.split("_")[0]))
                self.numeric_stageDefinitionID_box.set(stageDefinitionID.split("_")[1])
            self.numeric_stageDefinition_box.config(state="readonly")
            self.numeric_stageDefinitionID_box.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read stageDefinitionID: {str(e)}")

    def refresh_input(self, input:ttk.Entry, get):
        if input not in self.entry_vars:
            var = tk.StringVar()
            input.configure(textvariable=var)
            self.entry_vars[input] = var
        if (get != None):
            self.entry_vars[input].set(str(get))
            input.config(state="normal")

    def refresh_boolean_box(self, data, box:ttk.Combobox):
        box.config(state="readonly")
        if data:
            box.set(get_text("True"))
        else:
            box.set(get_text("False"))
    # endregion

def add_box(frame, label, row, column, value, command):
    tk.Label(frame, text=get_text(label)).grid(row=row, column=2*column, sticky="e", pady=12)
    box = ttk.Combobox(frame, values=value, state="disable", width=16)
    box.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    box.bind("<<ComboboxSelected>>", command)
    return box

def add_input(frame, label, row, column, validatecommand):
    tk.Label(frame, text=get_text(label)).grid(row=row, column=2*column, sticky="e", pady=12)
    input = ttk.Entry(frame, state="disable", validate='key',validatecommand=(validatecommand, '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
    input.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    return input
