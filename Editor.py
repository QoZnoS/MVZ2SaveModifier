import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import gzip,shutil,os,json,winreg,subprocess
import CustonJson,Window,NameData

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)

# 数据处理中心

class DataHandler:
    def __init__(self):
        self.current_data = None
        self.missing = False
        self.missing_log = [] # 储存数据读取失败信息

    # 设计原则：set应只出现在回调中，防止存档数据被意外修改

    # region numeric
    def set_stageDefinitionID(self, value:str):
        self.current_data['level']['stageDefinitionID'] = value

    def get_stageDefinitionID(self, default:str = None):
        try:
            return str(self.current_data['level']['stageDefinitionID'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'stageDefinitionID')
            self.missing = True
            return None

    def set_currentFlag(self, value:int):
        self.current_data['level']['currentFlag'] = value

    def get_currentFlag(self, default:int = None):
        try:
            return int(self.current_data['level']['currentFlag'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'currentFlag')
            self.missing = True
            return None

    def set_currentWave(self, value:int):
        self.current_data['level']['currentWave'] = value

    def get_currentWave(self, default:int = None):
        try:
            return int(self.current_data['level']['currentWave'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'currentWave')
            self.missing = True
            return None

    def set_energy(self, value:float):
        self.current_data['level']['energy'] = value

    def get_energy(self, default:float = None):
        try:
            return float(self.current_data['level']['energy'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'energy')
            self.missing = True
            return None

    def set_maxEnergy(self, value:float):
        self.current_data['level']['Option']['maxEnergy'] = value

    def get_maxEnergy(self, default:float = None):
        try:
            return float(self.current_data['level']['Option']['maxEnergy'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'maxEnergy')
            self.missing = True
            return None

    def set_starshardCount(self, value:int):
        self.current_data['level']['properties']['starshardCount'] = value

    def get_starshardCount(self, default:int = None):
        try:
            return int(self.current_data['level']['properties']['starshardCount'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'starshardCount')
            self.missing = True
            return None

    def set_starshardSlotCount(self, value:int):
        self.current_data['level']['properties']['starshardSlotCount'] = value

    def get_starshardSlotCount(self, default:int = None):
        try:
            return int(self.current_data['level']['properties']['starshardSlotCount'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'starshardSlotCount')
            self.missing = True
            return None

    def set_isConveyorMode(self, value:bool):
        self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'] = value

    def get_isConveyorMode(self, default:bool = None):
        try:
            return bool(self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'isConveyorMode')
            self.missing = True
            return None

    def set_noEnergy(self, value:bool):
        self.current_data['level']['properties']['noEnergy'] = value

    def get_noEnergy(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['noEnergy'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'noEnergy')
            self.missing = True
            return None

    def set_conveyorSlotCount(self, value:int):
        self.current_data['level']['conveyorSlotCount'] = value

    def get_conveyorSlotCount(self, default:int = None):
        try:
            return int(self.current_data['level']['conveyorSlotCount'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'conveyorSlotCount')
            self.missing = True
            return None

    def set_musicID(self, value:str):
        self.current_data['musicID'] = value

    def get_musicID(self, default:str = None):
        try:
            return str(self.current_data['musicID'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'musicID')
            self.missing = True
            return None

    def set_aotuCollect(self, value:bool):
        self.current_data['level']['properties']['autoCollect'] = value

    def get_aotuCollect(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['autoCollect'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'autoCollect')
            self.missing = True
            return None

    def set_rechargeSpeed(self, value:float):
        self.current_data['level']['rechargeSpeed'] = value

    def get_rechargeSpeed(self, default:float = None):
        try:
            return float(self.current_data['level']['rechargeSpeed'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'rechargeSpeed')
            self.missing = True
            return None

    def set_ignoreHugeWaveEvent(self, value:bool):
        self.current_data['level']['properties']['ignoreHugeWaveEvent'] = value

    def get_ignoreHugeWaveEvent(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['ignoreHugeWaveEvent'])
        except:
            if default != None:
                return default
            self.missing_log.append(get_text('info_missing_param') + 'ignoreHugeWaveEvent')
            self.missing = True
            return None

    # endregion

    def check_missing(self):
        if self.missing:
            misslabel = str()
            for label in self.missing_log:
                misslabel = misslabel + label + "\n"
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
        
        self.stageDefinition_box        = add_box(frame_group, "label_chapter"          , 0, 0, NameData.maps.name_list, self.mix_stageDefinitionID)        # 章节
        self.stageDefinitionID_box      = add_box(frame_group, "label_day"              , 1, 0, NameData.level_day, self.mix_stageDefinitionID)             # 关卡
        self.flag_input                 = add_input(frame_group, "label_flag"           , 2, 0, self.master.register(self.change_flag))                     # 旗帜
        self.wave_input                 = add_input(frame_group, "label_wave"           , 3, 0, self.master.register(self.change_wave))                     # 波数
        self.energy_input               = add_input(frame_group, "label_energy"         , 0, 1, self.master.register(self.change_energy))                   # 当前机械能
        self.maxEnergy_input            = add_input(frame_group, "label_maxEnergy"      , 1, 1, self.master.register(self.change_maxEnergy))                # 机械能上限
        self.starshardCount_input       = add_input(frame_group, "label_starshard"      , 2, 1, self.master.register(self.change_starshardCount))           # 星之碎片数
        self.starshardSlotCount_input   = add_input(frame_group, "label_maxStarshard"   , 3, 1, self.master.register(self.change_starshardSlotCount))       # 星之碎片槽
        self.isConveyorMode_box         = add_box(frame_group, "label_conveyor"         , 0, 2, [get_text("True"),get_text("False")], self.is_ConveyorMode) # 启用传送带
        self.conveyorSlotCount_input    = add_input(frame_group, "label_conveyorslot"   , 1, 2, self.master.register(self.change_conveyorSlotCount))        # 传送带槽数
        self.musicID_box                = add_box(frame_group, "label_bgm"              , 2, 2, NameData.musics.name_list, self.change_musicID)             # 背景音乐
        self.autoCollect_box            = add_box(frame_group, "label_autoCollect"      , 0, 3, [get_text("True"),get_text("False")], self.is_aotuCollect)  # 自动收集
        self.recharge_box               = add_box(frame_group, "label_recharge"         , 1, 3, [get_text("True"),get_text("False")], self.change_rechargeSpeed) # 蓝图无冷却
        self.ignoreHugeWaveEvent_box    = add_box(frame_group, "label_ignoreHugeWaveEvent", 2, 3, [get_text("True"),get_text("False")], self.is_ignoreHugeWaveEvent) # 忽略大波事件

        tk.Button(frame_group, text=get_text("btn_about"),command=self.open_about).grid(row=3,column=4,columnspan=4,ipadx=64)

    # region 响应回调
    def mix_stageDefinitionID(self,event):
        """混乱"""
        mapID = NameData.maps.get_id(self.stageDefinition_box.get())
        level = self.stageDefinitionID_box.get()
        isSpecial = (NameData.level_day.count(level)==0)
        if (mapID != "another"):
            if isSpecial:
                self.stageDefinitionID_box.config(values=NameData.level_day)
                self.stageDefinitionID_box.set(NameData.level_day[0])
            self.data_handler.set_stageDefinitionID(mapID + "_" + level)
        else:
            if not isSpecial:
                self.stageDefinitionID_box.config(values=NameData.levels.name_list)
                self.stageDefinitionID_box.set(NameData.levels.name_list[0])
            self.data_handler.set_stageDefinitionID(NameData.levels.get_id(level))
    
    def change_flag(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """旗数"""
        if value=="":
            self.data_handler.set_currentFlag(0)
            return True
        if value.isdigit():
            self.data_handler.set_currentFlag(int(value))
            return True
        return False
    
    def change_wave(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """波数"""
        if value=="":
            self.data_handler.set_currentWave(0)
            return True
        if value.isdigit():
            self.data_handler.set_currentWave(int(value))
            return True
        return False
    
    def change_energy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """当前机械能"""
        if value=="":
            self.data_handler.set_energy(0)
            return True
        try:
            self.data_handler.set_energy(float(value))
            return True
        except ValueError:
            return False
    
    def change_maxEnergy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """机械能上限"""
        if value=="":
            self.data_handler.set_maxEnergy(0)
            return True
        try:
            self.data_handler.set_maxEnergy(float(value))
            return True
        except ValueError:
            return False
    
    def change_starshardCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """星之碎片数"""
        if value=="":
            self.data_handler.set_starshardCount(0)
            return True
        try:
            self.data_handler.set_starshardCount(int(value))
            return True
        except ValueError:
            return False
    
    def change_starshardSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """星之碎片槽"""
        if value=="":
            self.data_handler.set_starshardSlotCount(0)
            return True
        try:
            self.data_handler.set_starshardSlotCount(int(value))
            return True
        except ValueError:
            return False
    
    def is_ConveyorMode(self,event):
        """是否启用传送带"""
        var = self.isConveyorMode_box.get()
        self.data_handler.set_isConveyorMode(NameData.bools.get_id(var))
    
    def change_conveyorSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        """传送带槽数"""
        if value=="":
            self.data_handler.set_conveyorSlotCount(0)
            return True
        try:
            self.data_handler.set_conveyorSlotCount(int(value))
            return True
        except ValueError:
            return False
    
    def change_musicID(self,event):
        """背景音乐"""
        var = self.musicID_box.get()
        self.data_handler.set_musicID(NameData.musics.get_id(var))
    
    def is_aotuCollect(self,event):
        """自动收集"""
        var = self.autoCollect_box.get()
        self.data_handler.set_aotuCollect(NameData.bools.get_id(var))
    
    def change_rechargeSpeed(self,event):
        """蓝图无冷却"""
        var = self.recharge_box.get()
        if NameData.bools.get_id(var):
            self.data_handler.set_rechargeSpeed(15532.0)
        else:
            self.data_handler.set_rechargeSpeed(1.0)
    
    def is_ignoreHugeWaveEvent(self,event):
        """忽略大波事件"""
        var = self.ignoreHugeWaveEvent_box.get()
        self.data_handler.set_ignoreHugeWaveEvent(NameData.bools.get_id(var))
    
    def open_about(self):
        """关于"""
        Window.AboutWindow(self.master)

    # endregion

    # region 刷新，读取参数
    def refresh(self):
        self.refresh_map_box()
        self.refresh_input(self.flag_input, self.data_handler.get_currentFlag())
        self.refresh_input(self.wave_input, self.data_handler.get_currentWave())
        self.refresh_input(self.energy_input, self.data_handler.get_energy())
        self.refresh_input(self.maxEnergy_input, self.data_handler.get_maxEnergy())
        self.refresh_input(self.starshardCount_input, self.data_handler.get_starshardCount(0))
        self.refresh_input(self.starshardSlotCount_input, self.data_handler.get_starshardSlotCount())
        self.refresh_box(self.isConveyorMode_box, self.data_handler.get_isConveyorMode(), NameData.bools)
        self.refresh_input(self.conveyorSlotCount_input, self.data_handler.get_conveyorSlotCount())
        self.refresh_box(self.musicID_box, self.data_handler.get_musicID(), NameData.musics)
        self.refresh_box(self.autoCollect_box, self.data_handler.get_aotuCollect(False), NameData.bools)
        self.refresh_box(self.recharge_box, (self.data_handler.get_rechargeSpeed() != 1.0), NameData.bools)
        self.refresh_box(self.ignoreHugeWaveEvent_box, self.data_handler.get_ignoreHugeWaveEvent(False), NameData.bools)

        self.data_handler.check_missing()

    def refresh_map_box(self):
        stageDefinitionID = self.data_handler.get_stageDefinitionID()
        if stageDefinitionID == None:
            return
        try:
            if (NameData.levels.id_list.count(stageDefinitionID)!=0):
                self.stageDefinitionID_box.config(values=NameData.levels.name_list)
                self.stageDefinitionID_box.set(NameData.levels.get_name(stageDefinitionID))
                self.stageDefinition_box.set("another")
            else:
                self.stageDefinition_box.set(NameData.maps.get_name(stageDefinitionID.split("_")[0]))
                self.stageDefinitionID_box.set(stageDefinitionID.split("_")[1])
            self.stageDefinition_box.config(state="readonly")
            self.stageDefinitionID_box.config(state="readonly")
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

    def refresh_box(self, box:ttk.Combobox, get, type:NameData.BilingualDataset):
        if (get != None):
            box.set(type.get_name(get))
            box.config(state="readonly")

    def refresh_boolean_box(self, box:ttk.Combobox, get):
        box.config(state="readonly")
        if get:
            box.set(get_text("True"))
        else:
            box.set(get_text("False"))

    def refresh_check(self, check:ttk.Checkbutton, get:bool):
        if check not in self.entry_vars:
            var = tk.BooleanVar()
            check.configure(variable=var)
            self.entry_vars[check] = var
        if (get != None):
            self.entry_vars[check].set(get)
            check.config(state="normal")
    # endregion

# region 通用UI组件

def add_box(frame, label:str, row, column, value:list, command):
    tk.Label(frame, text=get_text(label)).grid(row=row, column=2*column, sticky="e", pady=12)
    box = ttk.Combobox(frame, values=value, state="disable", width=16)
    box.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    box.bind("<<ComboboxSelected>>", command)
    return box

def add_input(frame, label:str, row, column, validatecommand):
    tk.Label(frame, text=get_text(label)).grid(row=row, column=2*column, sticky="e", pady=12)
    input = ttk.Entry(frame, state="disable", validate='key',validatecommand=(validatecommand, '%d', '%i', '%P', '%s', '%v', '%V', '%W'),width=16)
    input.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    return input

def add_check(frame, label:str, row, column, command):
    check = ttk.Checkbutton(frame, text=get_text(label), state="disable")
    check.grid(row=row, column=2*column, columnspan=2, sticky="ew", pady=12)
    check.bind("<<CheckbuttonSelected>>", command)


# endregion