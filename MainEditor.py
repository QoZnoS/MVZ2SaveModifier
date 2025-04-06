import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import gzip,shutil,os,json,winreg,subprocess
import platform
import CustonJson,Window,NameData

#region 全局函数
def get_save_path():
    '''根据系统返回userdata路径'''
    system = platform.system()
    if system == "Windows":
        return os.path.expandvars(r"%HOMEPATH%/AppData/LocalLow/Cuerzor/MinecraftVSZombies2/userdata")
    elif system == "Darwin":  # macOS
        return os.path.expanduser("~/Library/Application Support/Cuerzor/MinecraftVSZombies2/userdata")
    else:  # Linux
        return os.path.expanduser("~/.config/unity3d/Cuerzor/MinecraftVSZombies2/userdata")

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)

def decompress(path):
    '''根据给定路径解压文件，返回解压后的文件'''
    try:
        with gzip.open(path, "rb") as file:
            return file.read()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decompress: {str(e)}")

def compress(path,file):
    '''压缩文件到给定路径'''
    with gzip.open(path, "wb") as out:
        out.write(file)
#endregion

class ArchiveEditor:
    def __init__(self, root):
        self.root = root
        self.root.title(get_text("title"))

        self.current_file = ""  # 当前操作的文件路径
        self.current_data = None # 当前操作的文件JSON数据
        self.page = 1 # 界面，0为数值编辑器，1为蓝图/制品编辑器


        self.data_wave = tk.StringVar(value="0")
        self.data_flag = tk.StringVar(value="0")
        self.data_energy = tk.StringVar(value="50")
        self.data_maxEnergy = tk.StringVar(value="9990.0")
        self.data_starshardCount = tk.StringVar(value="2")
        self.data_starshardSlotCount = tk.StringVar(value="5")
        self.data_conveyorSlotCount = tk.StringVar(value="10")


        self.get_usersdata() # 自动读取存档
        self.setup_ui() # 创建UI
        self.switch_frame()
 
    # region 创建UI
    def setup_ui(self):
        self.setup_user_frame()
        self.setup_file_frame()
        self.frame_tree = tk.Frame(self.root)
        self.frame_numeric = tk.Frame(self.root)
        self.setup_tree_artifact_frame()
        self.setup_tree_blueprint_frame()
        self.setup_numeric_group_frame()

        # 状态栏
        self.status = tk.StringVar()
        self.status.set(get_text("status_ready"))
        tk.Label(self.root, textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W).pack(fill=tk.X,side=tk.BOTTOM)

        # 保存
        self.output_btn=tk.Button(self.root, text=get_text("btn_save"),command=self.output_file,state="disabled")
        self.output_btn.pack(fill=tk.X,side=tk.BOTTOM)
    # 创建制品/蓝图修改器UI
    def setup_tree_frame(self):
        self.frame_tree.pack(padx=10, fill=tk.BOTH, expand=True)
    # 创建数值修改器UI
    def setup_numeric_frame(self):
        self.frame_numeric.pack(padx=10, fill=tk.BOTH, expand=True)

    def setup_user_frame(self):
        """选择用户，单文件解压缩"""
        self.frame_user = tk.Frame(self.root)
        self.frame_user.pack(pady=10)
        self.username_label = tk.Label(self.frame_user, text=get_text("label_user") + self.username)
        self.username_label.pack(side=tk.LEFT)
        tk.Button(self.frame_user, text=get_text("btn_switch"), command=self.open_user_selector).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_user, text=get_text("btn_unzip"), command=self.decompress).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_user, text=get_text("btn_zip"), command=self.compress).pack(side=tk.LEFT, padx=5)

    def setup_file_frame(self):
        """存档选择，切换界面"""
        self.frame_file = tk.Frame(self.root)
        self.frame_file.pack(pady=10)
        self.filename_label = tk.Label(self.frame_file, text=get_text("label_lvl_null"))
        self.filename_label.pack(side=tk.LEFT)
        tk.Button(self.frame_file, text=get_text("btn_lvl"), command=self.open_save_selector).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_file, text=get_text("btn_open_explorer"), command=self.open_save_explorer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_file, text=get_text("btn_page"), command=self.switch_frame).pack(side=tk.LEFT, padx=10)
        # 混乱选项
        
    def setup_tree_artifact_frame(self):
        """制品"""
        frame_artifact = tk.Frame(self.frame_tree)
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

    def setup_tree_blueprint_frame(self):
        """蓝图"""
        frame_blueprint = tk.Frame(self.frame_tree)
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

    def setup_numeric_group_frame(self):
        frame_group = tk.Frame(self.frame_numeric)
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
        self.numeric_flag_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_flag, validate='key',validatecommand=(self.root.register(self.change_flag), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_flag_input.grid(row=2, column=1, sticky="ew", pady=12)
        # 波数
        tk.Label(frame_group, text=get_text("label_wave")).grid(row=3, column=0, sticky="e", pady=12)
        self.numeric_wave_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_wave, validate='key',validatecommand=(self.root.register(self.change_wave), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_wave_input.grid(row=3, column=1, sticky="ew", pady=12)
        # 当前机械能
        tk.Label(frame_group, text=get_text("label_energy")).grid(row=0, column=2, sticky="e", pady=12)
        self.numeric_energy_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_energy, validate='key',validatecommand=(self.root.register(self.change_energy), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_energy_input.grid(row=0, column=3, sticky="ew", pady=12)
        # 机械能上限
        tk.Label(frame_group, text=get_text("label_maxEnergy")).grid(row=1, column=2, sticky="e", pady=12)
        self.numeric_maxEnergy_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_maxEnergy, validate='key',validatecommand=(self.root.register(self.change_maxEnergy), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_maxEnergy_input.grid(row=1, column=3, sticky="ew", pady=12)
        # 星之碎片数
        tk.Label(frame_group, text=get_text("label_starshard")).grid(row=2, column=2, sticky="e", pady=12)
        self.numeric_starshardCount_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_starshardCount, validate='key',validatecommand=(self.root.register(self.change_starshardCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_starshardCount_input.grid(row=2, column=3, sticky="ew", pady=12)
        # 星之碎片槽
        tk.Label(frame_group, text=get_text("label_maxStarshard")).grid(row=3, column=2, sticky="e", pady=12)
        self.numeric_starshardSlotCount_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_starshardSlotCount, validate='key',validatecommand=(self.root.register(self.change_starshardSlotCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
        self.numeric_starshardSlotCount_input.grid(row=3, column=3, sticky="ew", pady=12)
        # 启用传送带
        tk.Label(frame_group, text=get_text("label_conveyor")).grid(row=0, column=4, sticky="e", pady=12)
        self.numeric_isConveyorMode_box = ttk.Combobox(frame_group,values=[get_text("True"),get_text("False")],state="disable",width=16)
        self.numeric_isConveyorMode_box.grid(row=0, column=5, sticky="ew", pady=12)
        self.numeric_isConveyorMode_box.bind("<<ComboboxSelected>>",self.is_ConveyorMode)
        # 传送带槽数
        tk.Label(frame_group, text=get_text("label_conveyorslot")).grid(row=1, column=4, sticky="e", pady=12)
        self.numeric_conveyorSlotCount_input = ttk.Entry(frame_group, state="disable", textvariable=self.data_conveyorSlotCount, validate='key',validatecommand=(self.root.register(self.change_conveyorSlotCount), '%d', '%i', '%P', '%s', '%v', '%V', '%W'))
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

    # endregion

    # region 窗口
    # 处理文件窗口
    def open_save_selector(self):
        """打开存档选择窗口"""
        Window.SaveFileSelector(
            parent=self.root,
            save_dir=get_save_path() + ("/user%d/mvz2/level"%(self.currentUserIndex)),
            on_select=self.handle_save_selected  # 关键：选择后的回调
        )
        
    def handle_save_selected(self, selected_path):
        """处理选择的存档"""
        try:
            self.current_file = selected_path
            self.current_data = json.loads(decompress(self.current_file).decode("utf-8"),cls=CustonJson.CustomDecoder)
            self.filename_label.config(text=get_text("label_lvl") + os.path.basename(self.current_file))
            self.refresh()
            # print(self.current_data)
            # print(json.dumps(self.current_data,cls=CustonJson.CustomEncoder))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")
    # 处理用户窗口
    def open_user_selector(self):
        """打开用户选择窗口"""
        Window.UserSelector(
            parent=self.root,
            metas=self.users['metas'],
            on_select=self.handle_user_selected
        )

    def handle_user_selected(self, selected_user):
        """处理选择的用户"""
        self.currentUserIndex = selected_user
        self.username = self.users['metas'][self.currentUserIndex]['username']
        self.username_label.config(text=get_text("label_user") + self.username)
    # endregion

    # region 响应回调
    # region user/file frame
    # 保存文件
    def output_file(self):
        save_dir=get_save_path() + "/user%d/mvz2/level/"%(self.currentUserIndex) + os.path.basename(self.current_file)
        output=json.dumps(self.current_data,cls=CustonJson.CustomEncoder).encode("utf-8")
        self.status.set(get_text("status_save") + save_dir)
        compress(save_dir,output)
    # 切换界面
    def switch_frame(self):
        if self.page:
            self.page=0
            self.frame_tree.pack_forget()
            self.setup_numeric_frame()
        else:
            self.page=1
            self.frame_numeric.pack_forget()
            self.setup_tree_frame()
            # self.refresh()
    # 打开存档文件夹
    def open_save_explorer(self):
        save_dir=get_save_path() + ("/user%d/mvz2/level"%(self.currentUserIndex))
        subprocess.run(f'explorer "{os.path.normpath(save_dir)}"', shell=True)
    # endregion
    # region tree_frame
    # 添加制品
    def add_artifact(self):
        if not self.artifact_box.get():
            return
        # 制品模板
        new_artifact = { 
            "definitionID":NameData.artifacts.get_id(self.artifact_box.get()),
            "propertyDict": {
                "properties": {}
            },
            "auras": [
                {
                "updateTimer":{},
                "buffs":[]
                },
                {
                "_id":1,
                "updateTimer":{},
                "buffs":[]
                }
            ]
        }
        # print(new_artifact)
        self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'].append(new_artifact)
        self.refresh_artifact()
    # 移除制品
    def remove_artifact(self):
        if not self.artifact_tree.selection():
            return
        selected = self.artifact_tree.item(self.artifact_tree.selection()[0])["values"][0]
        # 先删对应关卡buff
        selected_artifact = self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'][selected]
        if not len(selected_artifact['auras'])==0:
            for auras in selected_artifact['auras']:
                for buff_artifact in auras['buffs']:
                    if not buff_artifact['_t']=="BuffReferenceLevel":
                        continue
                    for buff_level in list(self.current_data['level']['buffs']['buffs']):
                        if buff_level["_id"][1]==buff_artifact['buffId'][1]:
                            self.current_data['level']['buffs']['buffs'].remove(buff_level)
        # 再删制品
        self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts'].pop(selected)
        # 刷新列表
        self.refresh_artifact()
    # 添加蓝图

    # 修改蓝图
    def modify_blueprint(self):
        if not self.blueprint_tree.selection():
            return
        selected = self.blueprint_tree.item(self.blueprint_tree.selection()[0])["values"][0]
        self.current_data['level']['seedPacks'][selected]['seedID']=NameData.blueprints.get_id(self.blueprint_box.get())
        if len(self.current_data['level']['seedPacks'][selected]['auras'])==0:
            self.current_data['level']['seedPacks'][selected]['auras'].append(
                    {
                        "updateTimer": {
                            "maxFrame": 1,
                            "lastFrame": 1,
                            "lastFrameFraction": 0,
                            "frame": 1,
                            "frameFraction": 0,
                            "precision": 2048
                        },
                        "buffs": []
                    }
            )
        self.refresh_blueprint()
    # 移除蓝图

    # endregion
    # region numeric_frame
    # 混乱
    def mix_stageDefinitionID(self,event):
        """处理混乱"""
        mapID = NameData.maps.get_id(self.numeric_stageDefinition_box.get())
        level = self.numeric_stageDefinitionID_box.get()
        isSpecial = (NameData.level_day.count(level)==0)
        if (mapID != "another"):
            if isSpecial:
                self.numeric_stageDefinitionID_box.config(values=NameData.level_day)
                self.numeric_stageDefinitionID_box.set(NameData.level_day[0])
            self.current_data['level']['stageDefinitionID'] = mapID + "_" + level
        else:
            if not isSpecial:
                self.numeric_stageDefinitionID_box.config(values=NameData.levels.name_list)
                self.numeric_stageDefinitionID_box.set(NameData.levels.name_list[0])
            self.current_data['level']['stageDefinitionID'] = NameData.levels.get_id(level)
    # 旗数
    def change_flag(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['currentFlag']=0
            return True
        if value.isdigit():
            self.current_data['level']['currentFlag']=int(value)
            return True
        return False
    # 波数
    def change_wave(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['currentWave']=0
            return True
        if value.isdigit():
            self.current_data['level']['currentWave']=int(value)
            return True
        return False
    # 当前机械能
    def change_energy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['energy']=0
            return True
        try:
            self.current_data['level']['energy']=float(value)  # 检查浮点数
            return True
        except ValueError:
            return False
    # 机械能上限
    def change_maxEnergy(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['Option']['maxEnergy']=0
            return True
        try:
            self.current_data['level']['Option']['maxEnergy']=float(value)  # 检查浮点数
            return True
        except ValueError:
            return False
    # 星之碎片数
    def change_starshardCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['properties']['starshardCount']=0
            return True
        if value.isdigit():
            self.current_data['level']['properties']['starshardCount']=int(value)
            return True
        return False
    # 星之碎片槽
    def change_starshardSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['properties']['starshardSlotCount']=0
            return True
        if value.isdigit():
            self.current_data['level']['properties']['starshardSlotCount']=int(value)
            return True
        return False
    # 是否启用传送带
    def is_ConveyorMode(self,event):
        if self.numeric_isConveyorMode_box.get()==get_text("True"):
            self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'] = True
            self.current_data['level']['properties']['noEnergy'] = True
        else:
            self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'] = False
            self.current_data['level']['properties']['noEnergy'] = False
    # 传送带槽数
    def change_conveyorSlotCount(self, action, index, value, prior_value, text, validation_type, trigger_type):
        if value=="":
            self.current_data['level']['conveyorSlotCount']=0
            return True
        if value.isdigit():
            self.current_data['level']['conveyorSlotCount']=int(value)
            return True
        return False
    # 背景音乐
    def change_musicID(self,event):
        self.current_data['musicID'] = NameData.musics.get_id(self.numeric_musicID_box.get())
    # 自动收集
    def is_aotuCollect(self,event):
        self.current_data['level']['properties']['autoCollect'] = (self.numeric_autoCollect_box.get()==get_text("True"))
    # 蓝图无冷却
    def change_rechargeSpeed(self,event):
        if (self.numeric_recharge_box.get()==get_text("True")):
            self.current_data['level']['rechargeSpeed'] = 15532.0
        else:
            self.current_data['level']['rechargeSpeed'] = 1.0
    # 忽略大波事件
    def is_ignoreHugeWaveEvent(self,event):
        self.current_data['level']['properties']['ignoreHugeWaveEvent'] = (self.numeric_ignoreHugeWaveEvent_box.get()==get_text("True"))
    # 关于
    def open_about(self):
        Window.AboutWindow(self.root)
    # endregion
    # endregion

    # region 工具
    def get_usersdata(self):
        '''获取用户数据'''
        users_path = get_save_path() + "/users.dat"
        self.users = json.loads(decompress(users_path),cls=CustonJson.CustomDecoder)
        self.currentUserIndex = self.users['currentUserIndex']
        self.username = self.users['metas'][self.currentUserIndex]['username']
    
    def decompress(self):
        '''单文件解压'''
        file_path = filedialog.askopenfilename(
            title="Choose file",
            filetypes=[("Save file", ["*.dat", "*.lvl"])]
        )
        if not file_path:
            return
        try:
            with gzip.open(file_path, "rb") as fin:
                with open(file_path + ".json", "wb") as fout:
                    fout.write(fin.read())
            self.status.set(f"Output: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decompress: {str(e)}")

    def compress(self):
        '''单文件压缩'''
        file_path = filedialog.askopenfilename(
            title="Choose file",
            filetypes=[("JSON file", "*.json"), ("Any file", "*")]
        )
        if not file_path:
            return
        try:
            with open(file_path, "rb") as fin:
                with gzip.open(file_path + ".lvl", "wb") as fout:
                    shutil.copyfileobj(fin, fout)
            self.status.set(f"Output: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to compress: {str(e)}")
    # endregion

    # region 刷新，获取关卡数据
    def refresh(self):
        """刷新界面"""
        self.artifact_box.config(state="readonly")
        self.artifact_box.set(NameData.artifacts.name_list[0])
        self.blueprint_box.config(state="readonly")
        self.blueprint_box.set(NameData.blueprints.name_list[0])
        self.output_btn.config(state="normal")
        self.refresh_artifact()
        self.refresh_blueprint()
        self.refresh_numeric()

    def refresh_artifact(self):
        """刷新制品列表"""
        data_artifact = self.current_data['level']['components']['mvz2:artifact']['artifacts']['artifacts']
        self.artifact_tree.delete(*self.artifact_tree.get_children())
        for i in range(len(data_artifact)):
            if data_artifact[i]:
                self.artifact_tree.insert("", "end", values=(i, NameData.artifacts.get_name(data_artifact[i]['definitionID'])))

    def refresh_blueprint(self):
        """刷新蓝图列表"""
        data_blueprint = self.current_data['level']['seedPacks']
        self.blueprint_tree.delete(*self.blueprint_tree.get_children())
        for i in range(len(data_blueprint)):
            if data_blueprint[i]:
                self.blueprint_tree.insert("", "end", values=(i, NameData.blueprints.get_name(data_blueprint[i]['seedID'])))

    def refresh_numeric(self):
        self.refresh_numeric_map_box()
        self.numeric_flag_input.config(state="normal")
        self.data_flag.set(self.current_data['level']['currentFlag'])
        self.numeric_wave_input.config(state="normal")
        self.data_wave.set(self.current_data['level']['currentWave'])
        self.numeric_energy_input.config(state="normal")
        self.data_energy.set(self.current_data['level']['energy'])
        self.numeric_maxEnergy_input.config(state="normal")
        self.data_maxEnergy.set(self.current_data['level']['Option']['maxEnergy'])
        self.numeric_starshardCount_input.config(state="normal")
        if not ('starshardCount' in self.current_data['level']['properties']):
            self.current_data['level']['properties']['starshardCount']=0
        self.data_starshardCount.set(self.current_data['level']['properties']['starshardCount'])
        self.numeric_starshardSlotCount_input.config(state="normal")
        self.data_starshardSlotCount.set(self.current_data['level']['properties']['starshardSlotCount'])
        self.refresh_boolean_box(self.current_data['level']['components']['mvz2:blueprints']['isConveyorMode'], self.numeric_isConveyorMode_box)
        self.numeric_conveyorSlotCount_input.config(state="normal")
        self.data_conveyorSlotCount.set(self.current_data['level']['conveyorSlotCount'])
        self.numeric_musicID_box.config(state="readonly")
        self.numeric_musicID_box.set(NameData.musics.get_name(self.current_data['musicID']))
        if not ('autoCollect' in self.current_data['level']['properties']):
            self.current_data['level']['properties']['autoCollect']=False
        self.refresh_boolean_box(self.current_data['level']['properties']['autoCollect'], self.numeric_autoCollect_box)
        self.refresh_boolean_box((self.current_data['level']['rechargeSpeed'] == 1.0), self.numeric_recharge_box)
        if not ('ignoreHugeWaveEvent' in self.current_data['level']['properties']):
            self.current_data['level']['properties']['ignoreHugeWaveEvent']=False
        self.refresh_boolean_box(self.current_data['level']['properties']['ignoreHugeWaveEvent'], self.numeric_ignoreHugeWaveEvent_box)

    def refresh_numeric_map_box(self):
        self.numeric_stageDefinition_box.config(state="readonly")
        self.numeric_stageDefinitionID_box.config(state="readonly")
        stageDefinitionID = self.current_data['level']['stageDefinitionID']
        if (NameData.levels.id_list.count(stageDefinitionID)!=0):
            self.numeric_stageDefinitionID_box.config(values=NameData.levels.name_list)
            self.numeric_stageDefinitionID_box.set(NameData.levels.get_name(stageDefinitionID))
            self.numeric_stageDefinition_box.set("another")
        else:
            self.numeric_stageDefinition_box.set(NameData.maps.get_name(stageDefinitionID.split("_")[0]))
            self.numeric_stageDefinitionID_box.set(stageDefinitionID.split("_")[1])

    def refresh_boolean_box(self, data, box):
        box.config(state="readonly")
        if data:
            box.set(get_text("True"))
        else:
            box.set(get_text("False"))
    # endregion

if __name__ == "__main__":
    # messagebox.showinfo("免责声明",f"使用该软件造成的文件损坏，本人一概不负责")
    root = tk.Tk()
    app = ArchiveEditor(root)
    root.mainloop()
