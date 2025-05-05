import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import NameData, Window

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)

# 数据处理中心

class DataHandler:
    def __init__(self):
        self.current_data = None
        self.missing = False
        self.missing_log = [] # 储存数据读取失败信息

    # 设计原则：set/add/del 应只出现在回调中，防止存档数据被意外修改

    # region numeric
    def set_stageDefinitionID(self, value:str):
        self.current_data['level']['stageDefinitionID'] = str(value)

    def get_stageDefinitionID(self, default:str = None):
        try:
            return str(self.current_data['level']['stageDefinitionID'])
        except:
            if default != None:
                return str(default)
            self.missing_log.append(get_text('info_missing_param') + 'stageDefinitionID')
            self.missing = True
            return None

    def set_currentFlag(self, value:int):
        self.current_data['level']['currentFlag'] = int(value)

    def get_currentFlag(self, default:int = None):
        try:
            return int(self.current_data['level']['currentFlag'])
        except:
            if default != None:
                return int(default)
            self.missing_log.append(get_text('info_missing_param') + 'currentFlag')
            self.missing = True
            return None

    def set_currentWave(self, value:int):
        self.current_data['level']['currentWave'] = int(value)

    def get_currentWave(self, default:int = None):
        try:
            return int(self.current_data['level']['currentWave'])
        except:
            if default != None:
                return int(default)
            self.missing_log.append(get_text('info_missing_param') + 'currentWave')
            self.missing = True
            return None

    def set_energy(self, value:float):
        self.current_data['level']['energy'] = float(value)

    def get_energy(self, default:float = None):
        try:
            return float(self.current_data['level']['energy'])
        except:
            if default != None:
                return float(default)
            self.missing_log.append(get_text('info_missing_param') + 'energy')
            self.missing = True
            return None

    def set_maxEnergy(self, value:float):
        self.current_data['level']['Option']['maxEnergy'] = float(value)

    def get_maxEnergy(self, default:float = None):
        try:
            return float(self.current_data['level']['Option']['maxEnergy'])
        except:
            if default != None:
                return float(default)
            self.missing_log.append(get_text('info_missing_param') + 'maxEnergy')
            self.missing = True
            return None

    def set_starshardCount(self, value:int):
        self.current_data['level']['properties']['starshardCount'] = int(value)

    def get_starshardCount(self, default:int = None):
        try:
            return int(self.current_data['level']['properties']['starshardCount'])
        except:
            if default != None:
                return int(default)
            self.missing_log.append(get_text('info_missing_param') + 'starshardCount')
            self.missing = True
            return None

    def set_starshardSlotCount(self, value:int):
        self.current_data['level']['properties']['starshardSlotCount'] = int(value)

    def get_starshardSlotCount(self, default:int = None):
        try:
            return int(self.current_data['level']['properties']['starshardSlotCount'])
        except:
            if default != None:
                return int(default)
            self.missing_log.append(get_text('info_missing_param') + 'starshardSlotCount')
            self.missing = True
            return None

    def set_isConveyorMode(self, value:bool):
        self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'] = bool(value)

    def get_isConveyorMode(self, default:bool = None):
        try:
            return bool(self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'isConveyorMode')
            self.missing = True
            return None

    def set_noEnergy(self, value:bool):
        self.current_data['level']['properties']['noEnergy'] = bool(value)

    def get_noEnergy(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['noEnergy'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'noEnergy')
            self.missing = True
            return None

    def set_conveyorSlotCount(self, value:int):
        self.current_data['level']['conveyorSlotCount'] = int(value)

    def get_conveyorSlotCount(self, default:int = None):
        try:
            return int(self.current_data['level']['conveyorSlotCount'])
        except:
            if default != None:
                return int(default)
            self.missing_log.append(get_text('info_missing_param') + 'conveyorSlotCount')
            self.missing = True
            return None

    def set_musicID(self, value:str):
        self.current_data['musicID'] = str(value)

    def get_musicID(self, default:str = None):
        try:
            return str(self.current_data['musicID'])
        except:
            if default != None:
                return str(default)
            self.missing_log.append(get_text('info_missing_param') + 'musicID')
            self.missing = True
            return None

    def set_autoCollect(self, value:bool):
        self.current_data['level']['properties']['autoCollect'] = bool(value)

    def get_autoCollect(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['autoCollect'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'autoCollect')
            self.missing = True
            return None

    def set_rechargeSpeed(self, value:float):
        self.current_data['level']['rechargeSpeed'] = float(value)

    def get_rechargeSpeed(self, default:float = None):
        try:
            return float(self.current_data['level']['rechargeSpeed'])
        except:
            if default != None:
                return float(default)
            self.missing_log.append(get_text('info_missing_param') + 'rechargeSpeed')
            self.missing = True
            return None

    def set_ignoreHugeWaveEvent(self, value:bool):
        self.current_data['level']['properties']['ignoreHugeWaveEvent'] = bool(value)

    def get_ignoreHugeWaveEvent(self, default:bool = None):
        try:
            return bool(self.current_data['level']['properties']['ignoreHugeWaveEvent'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'ignoreHugeWaveEvent')
            self.missing = True
            return None

    def set_energyActive(self, value:bool):
        self.current_data['energyActive'] = bool(value)

    def get_energyActive(self, default:bool = None):
        try:
            return bool(self.current_data['energyActive'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'energyActive')
            self.missing = True
            return None

    def set_blueprintsActive(self, value:bool):
        self.current_data['blueprintsActive'] = bool(value)

    def get_blueprintsActive(self, default:bool = None):
        try:
            return bool(self.current_data['blueprintsActive'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'blueprintsActive')
            self.missing = True
            return None

    def set_pickaxeActive(self, value:bool):
        self.current_data['pickaxeActive'] = bool(value)

    def get_pickaxeActive(self, default:bool = None):
        try:
            return bool(self.current_data['pickaxeActive'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'pickaxeActive')
            self.missing = True
            return None

    def set_starshardActive(self, value:bool):
        self.current_data['starshardActive'] = bool(value)

    def get_starshardActive(self, default:bool = None):
        try:
            return bool(self.current_data['starshardActive'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'starshardActive')
            self.missing = True
            return None

    def set_triggerActive(self, value:bool):
        self.current_data['triggerActive'] = bool(value)

    def get_triggerActive(self, default:bool = None):
        try:
            return bool(self.current_data['triggerActive'])
        except:
            if default != None:
                return bool(default)
            self.missing_log.append(get_text('info_missing_param') + 'triggerActive')
            self.missing = True
            return None
    
    def set_difficulty(self, value:str):
        self.current_data['level']['difficulty'] = str(value)

    def get_difficulty(self, default:str = None):
        try:
            return str(self.current_data['level']['difficulty'])
        except:
            if default != None:
                return str(default)
            self.missing_log.append(get_text('info_missing_param') + 'difficulty')
            self.missing = True
            return None

    # endregion

    # region artifact
    def get_artifact(self):
        """获取制品的原始列表"""
        return list(self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'])

    def add_artifact(self, arti:dict):
        """添加制品"""
        self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'].append(arti)

    def del_artifact(self, enum:int):
        """删除指定项制品"""
        del self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'][enum]

    def new_artifact(self, definitionID:str):
        """返回一个新制品"""
        if definitionID == "None":
            new_artifact = None
        else:
            new_artifact = { "definitionID":definitionID,
            "propertyDict": {"properties": {}},
            "auras": [{"updateTimer":{},"buffs":[]},
                      {"_id":1,"updateTimer":{},"buffs":[]}]}
        return new_artifact
    # 兼容函数
    def get_artifact_definitionID_list(self):
        """获取制品的definitionID列表"""
        definitionID_list = []
        for arti in self.get_artifact():
            try:
                definitionID_list.append(arti["definitionID"])
            except:
                definitionID_list.append("None")
        return definitionID_list

    # endregion

    # region blueprint
    def get_seedPacks(self):
        """返回seedPacks原始列表"""
        return list(self.current_data['level']['seedPacks'])

    def get_classic_blueprint_length(self):
        return len(self.current_data['parts'][0]['classicBlueprints'])

    def get_seedID_list(self):
        seedID_list = []
        for seed in self.get_seedPacks():
            try:
                seedID_list.append(seed['seedID'])
            except:
                seedID_list.append(None)
        return seedID_list
    
    def set_seedID_by_enum(self, enum, seedID):
        """修改 seedID 若为 null 则替换为新 seedPack 同时修改 classicBlueprint"""
        try:
            self.current_data['level']['seedPacks'][enum]['seedID'] = seedID
            self.fix_seed_auras(enum)
        except:
            if (self.current_data['parts'][0]['classicBlueprints'][enum]==None):
                self.current_data['parts'][0]['classicBlueprints'][enum] = self._new_classic_blueprint()
            self.current_data['level']['seedPacks'][enum] = self._new_seedPack_blueprint(seedID)

    def add_seedPack(self):
        """同时添加 seedPack classicBlueprint"""
        self.current_data['level']['seedPacks'].append(None)
        self.current_data['parts'][0]['classicBlueprints'].append(None)

    def del_seedPack(self, enum):
        """同时移除 seedPack classicBlueprint"""
        del self.current_data['level']['seedPacks'][enum]
        del self.current_data['parts'][0]['classicBlueprints'][enum]

    def set_seedPack_cost(self, enum, cost):
        self.current_data['level']['seedPacks'][enum]["properties"]["cost"] = float(cost)

    def get_seedPack_cost(self, enum):
        try:
            return self.current_data['level']['seedPacks'][enum]["properties"]["cost"]
        except:
            return None

    def remove_seedPack_cost(self, enum):
        del self.current_data['level']['seedPacks'][enum]["properties"]["cost"]

    def set_seedPack_rechargeSpeed(self, enum, speed):
        self.current_data['level']['seedPacks'][enum]["properties"]["rechargeSpeed"] = {"_t": "System.Single","_v": str(float(speed)+0.00000000001)}

    def get_seedPack_rechargeSpeed(self, enum):
        try:
            return float(self.current_data['level']['seedPacks'][enum]["properties"]["rechargeSpeed"]["_t"])-0.00000000001
        except:
            return None

    def remove_seedPack_rechargeSpeed(self, enum):
        del self.current_data['level']['seedPacks'][enum]["properties"]["rechargeSpeed"]

    def set_seedPack_rechargeId(self, enum, Id):
        self.current_data['level']['seedPacks'][enum]["properties"]["rechargeId"] = {"_t": "PVZEngine.NamespaceID","_v": Id}

    def get_seedPack_rechargeId(self, enum):
        try:
            return str(self.current_data['level']['seedPacks'][enum]["properties"]["rechargeId"]['_v'])
        except:
            return None

    def remove_seedPack_rechargeId(self, enum):
        del self.current_data['level']['seedPacks'][enum]["properties"]["rechargeId"]

    def get_seedPack_buff_length(self, enum):
        return len(self.current_data['level']['seedPacks'][enum]["buffs"]["buffs"])

    def remove_seedPack_buff(self, enum):
        self.current_data['level']['seedPacks'][enum]["buffs"]["buffs"].clear()
        self.current_data['level']['seedPacks'][enum]["currentBuffID"][1] = 1

    def _new_classic_blueprint(self):
        classicBlueprint = {"_t":"SerializableClassicBlueprintController",
                            "model": {"_t": "SerializableUIModelData","rng": {},
                                "graphicGroup": {"_t": "SerializableModelImageGroup","animators": []},
                                "propertyDict": {},"childModels":[]}}
        return classicBlueprint

    def _new_seedPack_blueprint(self, seedID):
        blueprint = {"seedID": seedID,
                    "currentBuffID": ["NumberLong", 1],
                    "buffs": {"buffs": []},
                    "properties": {},
                    "auras": [{"updateTimer": {},"buffs": []}]}
        return blueprint

    def fix_seed_auras(self, enum):
        """处理紫卡"""
        if len(self.current_data['level']['seedPacks'][enum]['auras'])==0:
            self.current_data['level']['seedPacks'][enum]['auras'].append({"updateTimer": {},"buffs": []})


    # endregion

    # region level_buff
    def get_level_buff(self):
        """返回原始buff列表"""
        return list(self.current_data['level']['buffs']['buffs'])

    def add_level_buff(self, buff:dict):
        """添加buff"""
        self.current_data['level']['buffs']['buffs'].append(buff)

    def del_level_buff_by_enum(self, enum:int):
        """删除buff中指定项"""
        del self.current_data['level']['buffs']['buffs'][enum]

    def new_level_buff(self, definitionID:str):
        """返回一个新buff"""
        new_buff ={"_id": ["NumberLong", self.get_level_buff_next_id()],
                    "definitionID": definitionID,
                    "propertyDict": {"properties": {}},
                    "auras": [{"updateTimer": {},"buffs": []}]}
        return new_buff

    def get_level_buff_definitionID_list(self):
        """返回关卡 buff definitionID 列表"""
        definitionID_list = []
        for buff in self.get_level_buff():
            definitionID_list.append(buff["definitionID"])
        return definitionID_list
    
    def get_level_buff_by_enum(self, enum:int):
        """返回指定序号的buff整体"""
        try:
            return dict(self.get_level_buff()[enum])
        except:
            return None

    def get_level_buff_by_id(self, id:int):
        """返回首个_id匹配的buff整体"""
        for buff in self.get_level_buff():
            if buff["_id"][1] == id:
                return dict(buff)
        else:
            return None
    # 兼容函数
    def get_level_buff_enum_by_id(self, id:int):
        """返回首个_id匹配的buff的enum"""
        enum = 0
        for buff in self.get_level_buff():
            if buff["_id"][1] == id:
                return enum
            else:
                enum += 1
        else:
            return None

    def get_level_buff_next_id(self):
        """返回下一个生成的buff的id"""
        _id = 1
        while (self.get_level_buff_by_id(_id) != None):
            _id += 1
        return _id
    # endregion

    # region gird
    def get_grids(self):
        """返回网格的原始列表"""
        return list(self.current_data['level']['grids'])
    
    def set_grid_definitionID_by_enum(self, enum, definitionID):
        self.current_data['level']['grids'][enum]['definitionID'] = definitionID
    # endregion

    # region EnemyPool
    def get_enemyPool(self):
        """返回出怪种类列表"""
        try:
            return list(self.current_data['level']['properties']['enemyPool']['_v'])
        except:
            return None
    
    def set_enemyPool(self, pool:list):
        """替换出怪种类列表"""
        self.current_data['level']['properties']['enemyPool']['_v'] = list(pool)

    def fix_enemyPool(self):
        """不存在出怪列表时添加出怪列表"""
        self.current_data['level']['properties']['enemyPool'] = {
                "_t": "PVZEngine.NamespaceID[], PVZEngine.Base",
                "_v": []}
        
    def del_enemyPool(self):
        return (self.current_data['level']['properties'].pop('enemyPool'))["_v"]
    # endregion

    def check_missing(self):
        if self.missing:
            misslabel = str()
            for label in self.missing_log:
                misslabel = misslabel + label + "\n"
            messagebox.showinfo(get_text('info_missing'), misslabel)

# 3.0版本实现可视化编辑

# 各个分页
# 准备重做
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
        tk.Button(blueprint_control_frame, text=get_text("btn_modify"), width=8, command=self.modify_blueprint).pack(fill=tk.X, pady=12)

    # region 响应回调
    def add_artifact(self):
        definitionID = NameData.artifacts.get_id(self.artifact_box.get())
        artifact = self.data_handler.new_artifact(definitionID)
        self.data_handler.add_artifact(artifact)
        self.refresh_artifact()

    def remove_artifact(self):
        if not self.artifact_tree.selection():
            return
        enum = self.artifact_tree.item(self.artifact_tree.selection()[0])["values"][0]
        arti = self.data_handler.get_artifact()[enum]
        if arti == None:
            self.data_handler.del_artifact(enum)
            self.refresh_artifact()
            return
        if len(arti['auras'])!=0:
            for auras in arti['auras']:
                for buff in auras['buffs']:
                    if buff['_t']!="BuffReferenceLevel":
                        continue
                    buff_enum = self.data_handler.get_level_buff_enum_by_id(buff['buffId'][1])
                    self.data_handler.del_level_buff_by_enum(buff_enum)
        self.data_handler.del_artifact(enum)
        self.refresh_artifact()

    def modify_blueprint(self):
        if not self.blueprint_tree.selection():
            return
        enum = self.blueprint_tree.item(self.blueprint_tree.selection()[0])["values"][0]
        self.data_handler.set_seedID_by_enum(enum, NameData.blueprints.get_id(self.blueprint_box.get()))
        self.data_handler.fix_seed_auras(enum)
        self.refresh_blueprint()
    # endregion

    # region 刷新
    def refresh(self):
        self.artifact_box.config(state="readonly")
        self.artifact_box.set(NameData.artifacts.name_list[0])
        self.blueprint_box.config(state="readonly")
        self.blueprint_box.set(NameData.blueprints.name_list[0])
        self.refresh_artifact()
        self.refresh_blueprint()

    def refresh_artifact(self):
        """刷新制品列表"""
        data_artifact = self.data_handler.get_artifact_definitionID_list()
        self.artifact_tree.delete(*self.artifact_tree.get_children())
        for i in range(len(data_artifact)):
            if data_artifact[i]:
                self.artifact_tree.insert("", "end", values=(i, NameData.artifacts.get_name(data_artifact[i])))

    def refresh_blueprint(self):
        """刷新蓝图列表"""
        data_blueprint = self.data_handler.get_seedID_list()
        self.blueprint_tree.delete(*self.blueprint_tree.get_children())
        for i in range(len(data_blueprint)):
            if data_blueprint[i]:
                self.blueprint_tree.insert("", "end", values=(i, NameData.blueprints.get_name(data_blueprint[i])))
    # endregion

class Artifact_Editor:
    def __init__(self, master, data_handler:DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack()
        self._setup_ui()

    def _setup_ui(self):
        pass

    def refresh(self):
        pass

class Blueprint_Editor:
    def __init__(self, master, data_handler: DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.blueprint_btn_list = []
        self.empty_img = tk.PhotoImage(width=86, height=90)  # 透明占位图

        self._setup_ui()

    # region UI
    def _setup_ui(self):
        self.canvas = tk.Canvas(self.frame, height=110)
        self.canvas.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.canvas.pack_propagate(False)
        self.blueprint_frame = tk.Frame(self.canvas)
        self.blueprint_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.blueprint_frame, anchor=tk.NW)
        scroll_x = tk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.ui = tk.Frame(self.frame)
        self.ui.pack(side=tk.TOP)
        self.btn_frame = tk.Frame(self.ui)
        self.btn_frame.pack(fill=tk.BOTH, side=tk.TOP)

        self.vars = {}
        self.toggled = 0
        self.change_blueprint_btn = tk.Button(self.btn_frame, text=get_text("btn_modify_blueprint"), command=self.open_blueprint_selector, width=24, state=tk.DISABLED)
        self.change_blueprint_btn.grid(row=0, column=1, sticky="ew", pady=12)
        self.add_blueprint_btn = tk.Button(self.btn_frame, text=get_text("btn_add_blueprint"), command=self.add_blueprint, width=24, state=tk.DISABLED)
        self.add_blueprint_btn.grid(row=0, column=3, sticky="ew", pady=12)
        self.del_blueprint_btn = tk.Button(self.btn_frame, text=get_text("btn_delete_blueprint"), command=self.del_blueprint, width=24, state=tk.DISABLED)
        self.del_blueprint_btn.grid(row=0, column=5, sticky="ew", pady=12)
        self.change_cost_input = add_input(self.btn_frame, get_text("label_cost"), 1, 0, self.master.register(self.change_cost))
        self.change_recharge_time_input = add_input(self.btn_frame, get_text("label_recharge_time"), 1, 1, self.master.register(self.change_recharge_time))
        self.change_charge_id_box = add_box(self.btn_frame, get_text("label_rechargeLevel"), 1, 2, NameData.recharges.name_list, self.change_recharge_id)
        self.remove_buff_btn = tk.Button(self.btn_frame, text=get_text("btn_remove_buff"), command=self.remove_buff, width=24, state=tk.DISABLED)
        self.remove_buff_btn.grid(row=2, column=3, sticky="ew", pady=12)
        self.help_btn = tk.Button(self.btn_frame, text="?", command=self.open_help_window)
        self.help_btn.grid(row=2, column=4, sticky="ew", padx=(0,64))

    def _setup_blueprint(self):
        while(len(self.blueprint_btn_list)>0):
            self.del_btn_blueprint(0)

        length = self.data_handler.get_classic_blueprint_length()
        seed_ID = self.data_handler.get_seedID_list()
        for i in range(length):
            self.add_btn_blueprint(seed_ID[i])

    def add_btn_blueprint(self, seedID=None):
        var = tk.BooleanVar()
        btn = tk.Button(self.blueprint_frame, bg="white",
                        command=lambda enum=len(self.blueprint_btn_list): self.toggle_blueprint(enum))
        img = NameData.assets.get_blueprint(NameData.blueprints.get_name(seedID)) if (seedID != None) else self.empty_img
        btn.config(image=img, width=85, height=90, compound=tk.CENTER)
        btn.pack(side=tk.LEFT)
        self.blueprint_btn_list.append((var, btn))

    def del_btn_blueprint(self, enum):
        self.blueprint_btn_list[enum][1].destroy()
        del self.blueprint_btn_list[enum]

    # endreigon
    # region 响应回调
    def add_blueprint(self):
        self.data_handler.add_seedPack()
        self.add_btn_blueprint()

    def del_blueprint(self):
        for enum in reversed(range(len(self.blueprint_btn_list))):
            if (self.blueprint_btn_list[enum][0].get()):
                self.data_handler.del_seedPack(enum)
                self.del_btn_blueprint(enum)
        for enum in range(len(self.blueprint_btn_list)):
            var, btn = self.blueprint_btn_list[enum]
            btn.config(command=lambda enum=enum:self.toggle_blueprint(enum))

    def change_recharge_time(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.remove_seedPack_rechargeId(self.toggled)
            self.data_handler.remove_seedPack_rechargeSpeed(self.toggled)
            return True
        try:
            self.data_handler.set_seedPack_rechargeId(self.toggled)
            self.data_handler.set_seedPack_rechargeSpeed(self.toggled, float(value))
            return True
        except ValueError:
            return False

    def change_cost(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.data_handler.remove_seedPack_cost(self.toggled)
            return True
        try:
            self.data_handler.set_seedPack_cost(self.toggled, float(value))
            return True
        except ValueError:
            return False

    def open_blueprint_selector(self):
        Window.BlueprintSelector(self.ui, self.change_blueprint_id)

    def change_blueprint_id(self, seedID):
        enum = 0
        for var, btn in self.blueprint_btn_list:
            if (var.get()):
                btn.config(image=NameData.assets.get_blueprint(NameData.blueprints.get_name(seedID, "zh")))
                self.data_handler.set_seedID_by_enum(enum, seedID)
            enum += 1

    def change_recharge_id(self, event):
        pass

    def remove_buff(self):
        pass

    def remove_buff_help(self):
        pass

    def open_help_window(self):
        pass
    # endregion
    # region 刷新
    def toggle_blueprint(self, enum):
        _, enum_btn = self.blueprint_btn_list[enum]
        i=0
        self.toggled=0
        for k in range(len(self.blueprint_btn_list)):
            var, btn=self.blueprint_btn_list[k]
            if (btn == enum_btn):
                var.set(not var.get())
            if (var.get()):
                self.toggled=k
                i+=1
            color = "lightgreen" if var.get() else "white"
            btn.config(bg=color)
        if (i>1):
            self.refresh_component(False)
        elif (i==1):
            self.refresh_component(True, self.toggled)
        elif (i==0):
            self.change_blueprint_btn.config(state=tk.DISABLED)
            self.change_cost_input.config(state=tk.DISABLED)
            self.change_recharge_time_input.config(state=tk.DISABLED)
            self.del_blueprint_btn.config(state=tk.DISABLED)
            self.remove_buff_btn.config(state=tk.DISABLED)
            self.change_charge_id_box.config(state=tk.DISABLED)

    def refresh(self):
        self.add_blueprint_btn.config(state=tk.NORMAL)
        self._setup_blueprint()

    def refresh_component(self, single:bool, enum:int = 0):
        self.change_blueprint_btn.config(state=tk.NORMAL)
        self.del_blueprint_btn.config(state=tk.NORMAL)
        self.remove_buff_btn.config(state=tk.NORMAL)
        if single:
            speed=self.data_handler.get_seedPack_rechargeSpeed(enum)
            self.refresh_input(self.change_recharge_time_input, speed)
            cost=self.data_handler.get_seedPack_cost(enum)
            self.refresh_input(self.change_cost_input, cost)
            self.refresh_box()
        else:
            self.refresh_input(self.change_cost_input)
            self.change_cost_input.config(state=tk.DISABLED)
            self.refresh_input(self.change_recharge_time_input)
            self.change_recharge_time_input.config(state=tk.DISABLED)
            self.change_charge_id_box.config(state=tk.DISABLED)

    def refresh_input(self, input:ttk.Entry, get=None):
        if input not in self.vars:
            var = tk.StringVar()
            input.configure(textvariable=var)
            self.vars[input] = var
        if (get != None):
            self.vars[input].set(str(get))
        else:
            self.vars[input].set("")
        input.config(state="normal")

    def refresh_box(self):
        pass

    # endregion

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

        self.vars = {}
        
        self.stageDefinition_box        =add_box(frame_group,get_text("label_chapter")              , 0, 0, NameData.maps.name_list, self.mix_stageDefinitionID)    # 章节
        self.stageDefinitionID_box      =add_box(frame_group,get_text("label_day")                  , 1, 0, NameData.level_day, self.mix_stageDefinitionID)         # 关卡
        self.musicID_box                =add_box(frame_group,get_text("label_musicID")              , 2, 0, NameData.musics.name_list, self.change_musicID)         # 背景音乐
        self.flag_input                 =add_input(frame_group,get_text("label_flag")               , 3, 0, self.master.register(self.change_flag))                 # 旗帜
        self.wave_input                 =add_input(frame_group,get_text("label_wave")               , 4, 0, self.master.register(self.change_wave))                 # 波数
        self.energy_input               =add_input(frame_group,get_text("label_energy")             , 0, 1, self.master.register(self.change_energy))               # 当前机械能
        self.maxEnergy_input            =add_input(frame_group,get_text("label_maxEnergy")          , 1, 1, self.master.register(self.change_maxEnergy))            # 机械能上限
        self.starshardCount_input       =add_input(frame_group,get_text("label_starshard")          , 2, 1, self.master.register(self.change_starshardCount))       # 星之碎片数
        self.starshardSlotCount_input   =add_input(frame_group,get_text("label_maxStarshard")       , 3, 1, self.master.register(self.change_starshardSlotCount))   # 星之碎片槽
        self.conveyorSlotCount_input    =add_input(frame_group,get_text("label_conveyorslot")       , 4, 1, self.master.register(self.change_conveyorSlotCount))    # 传送带槽数
        self.difficulty_box             =add_box(frame_group,get_text("label_difficulty")           , 0, 2, NameData.difficultys.name_list, self.change_difficulty) # 难度
        self.autoCollect_check          =add_check(frame_group,get_text("label_autoCollect")        , 1, 2, self.change_autoCollect)                                # 自动收集
        self.rechargeSpeed_check        =add_check(frame_group,get_text("label_rechargeSpeed")      , 2, 2, self.change_rechargeSpeed)                              # 蓝图无冷却
        self.ignoreHugeWaveEvent_check  =add_check(frame_group,get_text("label_ignoreHugeWaveEvent"), 3, 2, self.change_ignoreHugeWaveEvent)                        # 忽略大波事件
        self.isConveyorMode_check       =add_check(frame_group,get_text("label_isConveyorMode")     , 4, 2, self.change_isConveyorMode)                             # 启用传送带
        self.energyActive_check         =add_check(frame_group,get_text("label_energyActive")       , 0, 3, self.change_energyActive)                               # 显示机械能
        self.blueprintsActive_check     =add_check(frame_group,get_text("label_blueprintsActive")   , 1, 3, self.change_blueprintsActive)                           # 显示蓝图
        self.pickaxeActive_check        =add_check(frame_group,get_text("label_pickaxeActive")      , 2, 3, self.change_pickaxeActive)                              # 启用镐子
        self.starshardActive_check      =add_check(frame_group,get_text("label_starshardActive")    , 3, 3, self.change_starshardActive)                            # 启用星之碎片
        self.triggerActive_check        =add_check(frame_group,get_text("label_triggerActive")      , 4, 3, self.change_triggerActive)                              # 启用驱动

        # tk.Button(frame_group, text=get_text("btn_about"),command=self.open_about).grid(row=4,column=6,ipadx=48)

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
    
    def change_isConveyorMode(self):
        """是否启用传送带，同时修改生成属性"""
        var = self.vars[self.isConveyorMode_check].get()
        self.data_handler.set_isConveyorMode(var)
        self.data_handler.set_noEnergy(var)
    
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
    
    def change_difficulty(self,event):
        """难度"""
        var = self.difficulty_box.get()
        self.data_handler.set_difficulty(NameData.difficultys.get_id(var))

    def change_autoCollect(self):
        """自动收集"""
        var = self.vars[self.autoCollect_check].get()
        self.data_handler.set_autoCollect(var)
    
    def change_rechargeSpeed(self):
        """蓝图无冷却"""
        var = self.vars[self.rechargeSpeed_check].get()
        if var:
            self.data_handler.set_rechargeSpeed(15532.0)
        else:
            self.data_handler.set_rechargeSpeed(1.0)
    
    def change_ignoreHugeWaveEvent(self):
        """忽略大波事件"""
        var = self.vars[self.ignoreHugeWaveEvent_check].get()
        self.data_handler.set_ignoreHugeWaveEvent(var)
    
    def change_energyActive(self):
        """显示机械能"""
        var = self.vars[self.energyActive_check].get()
        self.data_handler.set_energyActive(var)

    def change_blueprintsActive(self):
        """显示蓝图"""
        var = self.vars[self.blueprintsActive_check].get()
        self.data_handler.set_blueprintsActive(var)

    def change_pickaxeActive(self):
        """启用镐子"""
        var = self.vars[self.pickaxeActive_check].get()
        self.data_handler.set_pickaxeActive(var)

    def change_starshardActive(self):
        """启用星之碎片"""
        var = self.vars[self.starshardActive_check].get()
        self.data_handler.set_starshardActive(var)

    def change_triggerActive(self):
        """启用驱动"""
        var = self.vars[self.triggerActive_check].get()
        self.data_handler.set_triggerActive(var)
    # endregion

    # region 刷新，读取参数
    def refresh(self):
        self.refresh_map_box()
        self.refresh_input( self.flag_input,                self.data_handler.get_currentFlag())
        self.refresh_input( self.wave_input,                self.data_handler.get_currentWave())
        self.refresh_input( self.energy_input,              self.data_handler.get_energy())
        self.refresh_input( self.maxEnergy_input,           self.data_handler.get_maxEnergy())
        self.refresh_input( self.starshardCount_input,      self.data_handler.get_starshardCount(0))
        self.refresh_input( self.starshardSlotCount_input,  self.data_handler.get_starshardSlotCount())
        self.refresh_check( self.isConveyorMode_check,      self.data_handler.get_isConveyorMode())
        self.refresh_input( self.conveyorSlotCount_input,   self.data_handler.get_conveyorSlotCount())
        self.refresh_box(   self.musicID_box,               self.data_handler.get_musicID(), NameData.musics)
        self.refresh_box(   self.difficulty_box,            self.data_handler.get_difficulty(), NameData.difficultys)
        self.refresh_check( self.autoCollect_check,         self.data_handler.get_autoCollect(False))
        self.refresh_check( self.rechargeSpeed_check,       (self.data_handler.get_rechargeSpeed() != 1.0))
        self.refresh_check( self.ignoreHugeWaveEvent_check, self.data_handler.get_ignoreHugeWaveEvent(False))
        self.refresh_check( self.energyActive_check,        self.data_handler.get_energyActive(False))
        self.refresh_check( self.blueprintsActive_check,    self.data_handler.get_blueprintsActive(False))
        self.refresh_check( self.pickaxeActive_check,       self.data_handler.get_pickaxeActive(False))
        self.refresh_check( self.starshardActive_check,     self.data_handler.get_starshardActive(False))
        self.refresh_check( self.triggerActive_check,       self.data_handler.get_triggerActive(False))

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
        if input not in self.vars:
            var = tk.StringVar()
            input.configure(textvariable=var)
            self.vars[input] = var
        if (get != None):
            self.vars[input].set(str(get))
            input.config(state="normal")

    def refresh_box(self, box:ttk.Combobox, get, type:NameData.BilingualDataset):
        if (get != None):
            box.set(type.get_name(get))
            box.config(state="readonly")

    def refresh_check(self, check:ttk.Checkbutton, get:bool):
        if check not in self.vars:
            var = tk.BooleanVar()
            check.configure(variable=var)
            self.vars[check] = var
        if (get != None):
            self.vars[check].set(bool(get))
            check.config(state="normal")
    # endregion

class Grids_Editor:
    def __init__(self, master, data_handler:DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.grids = []
        self._setup_ui()

        self.start_label = tk.Label(self.frame, text=get_text("label_start_grid"))
        self.start_label.pack(pady=90)

    def _setup_ui(self):
        self.ui = tk.Frame(self.frame)
        self.grid_id_box = ttk.Combobox(self.ui, values=NameData.grids.name_list, state="disable")
        self.grid_id_box.pack(pady=(0,12), fill=tk.X)
        self.grid_id_btn = tk.Button(self.ui, text=get_text("btn_modify"), command=self.change_grid, width=24)
        self.grid_id_btn.pack(fill=tk.X)

    def create_grid(self):
        grids = tk.Frame(self.frame)
        grids.pack(side=tk.LEFT, padx=10, expand=True)

        for grid in self.data_handler.get_grids():
            enum = grid['lane']*9 + grid['column']
            var = tk.BooleanVar()
            img = NameData.assets.get_grid(NameData.grids.get_name(grid['definitionID'], "en"))
            btn = tk.Button(grids, width=70, height=70, bg="white", command=lambda enum=enum: self.toggle_grid(enum), image=img)
            btn.grid(row=grid['lane'], column=grid['column'])
            self.grids.append((var, btn))

    # region 回调
    def toggle_grid(self, enum):
        """网格选中"""
        var, btn = self.grids[enum]
        var.set(not var.get())
        color = "lightgreen" if var.get() == 1 else "white"
        btn.config(bg=color)

    def change_grid(self):
        if not self.grid_id_box.get():
            return
        definitionID = NameData.grids.get_id(self.grid_id_box.get())
        for i in range(len(self.grids)):
            var = self.grids[i][0]
            if var.get():
                self.data_handler.set_grid_definitionID_by_enum(i, definitionID)
                img = NameData.assets.get_grid(NameData.grids.get_name(definitionID, "en"))
                self.grids[i][1].config(image=img)

    # endregion

    def refresh(self):
        if len(self.grids) != 0:
            self.grids[0][1].master.destroy()
            self.grids.clear()
        self.create_grid()
        self.ui.pack(side=tk.RIGHT, padx=10, expand=True)
        self.grid_id_box.config(state="readonly")
        self.grid_id_box.set(NameData.grids.name_list[0])
        self.start_label.destroy()

class EnemyPool_Editor:
    def __init__(self, master, data_handler:DataHandler):
        self.master = master
        self.data_handler = data_handler
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.checks = []
        self.vars = {}
        self.pool = []
        self._setup_ui()

    def _setup_ui(self):
        self.enable_enemyPool_check = add_check(self.frame, get_text('check_enemyPool'), 0, 0, self.enable_enemyPool_spawn)
        var = tk.BooleanVar()
        self.enable_enemyPool_check.configure(variable=var)
        self.vars[self.enable_enemyPool_check] = var
        i,j = 1,0
        for id in NameData.spawns:
            check = add_check(self.frame, NameData.blueprints.get_name(id), i, j, self.change_spawn)
            self.checks.append((id, check))
            i+=1
            if i>4:
                i=0
                j+=1

    def change_spawn(self):
        self.pool.clear()
        for id,check in self.checks:
            if self.vars[check].get():
                self.pool.append(id)
        self.data_handler.set_enemyPool(self.pool)

    def enable_enemyPool_spawn(self):
        if self.vars[self.enable_enemyPool_check].get():
            self.data_handler.fix_enemyPool()
            self.data_handler.set_enemyPool(self.pool)
            self.refresh()
        else:
            self.pool = self.data_handler.del_enemyPool()
            self.refresh()

    def refresh(self):
        self.enable_enemyPool_check.config(state="normal")
        for id,check in self.checks:
            if check not in self.vars:
                var = tk.BooleanVar()
                check.configure(variable=var)
                self.vars[check] = var
        
        pool = self.data_handler.get_enemyPool()
        if(pool == None):
            self.vars[self.enable_enemyPool_check].set(False)
            for id,check in self.checks:
                check.config(state="disable")
            return

        self.vars[self.enable_enemyPool_check].set(True)
        for id,check in self.checks:
            self.vars[check].set(bool(pool.count(id) != 0))
            check.config(state="normal")

# region 通用UI组件

def add_box(frame, label:str, row, column, value:list, command):
    tk.Label(frame, text=label).grid(row=row, column=2*column, sticky="e", pady=12)
    box = ttk.Combobox(frame, values=value, state="disable", width=16)
    box.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    box.bind("<<ComboboxSelected>>", command)
    return box

def add_input(frame, label:str, row, column, validatecommand):
    """
    label需使用get_text \n
    validatecommand写法为 <code>self.master.register(self.command)</code> \n
    回调函数参数 <code>(self, action, index, value, prior_value, text, validation_type, trigger_type)</code>
    """
    tk.Label(frame, text=label).grid(row=row, column=2*column, sticky="e", pady=12)
    input = ttk.Entry(frame, state="disable", validate='key',validatecommand=(validatecommand, '%d', '%i', '%P', '%s', '%v', '%V', '%W'),width=16)
    input.grid(row=row, column=2*column+1, sticky="ew", pady=12)
    return input

def add_check(frame, label:str, row, column, command):
    check = ttk.Checkbutton(frame, text=label, state="disable", command=command)
    check.grid(row=row, column=2*column, columnspan=2, sticky="ew", pady=12, padx=64)
    return check


# endregion