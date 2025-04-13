import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import gzip,shutil,os,json,subprocess,platform
import CustonJson,Window,NameData,Editor

#region 全局函数
def get_save_path():
    '''根据系统返回userdata路径'''
    system = platform.system()
    if system == "Windows":
        return os.path.expandvars("C:\\" + r"%HOMEPATH%\\AppData\\LocalLow\\Cuerzor\\MinecraftVSZombies2\\userdata")
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

        self.archive = ttk.Notebook(self.root)
        self.datahandler = Editor.DataHandler()

        self.get_usersdata() # 自动读取存档
        self.setup_ui() # 创建UI
 
    def setup_ui(self):
        self.setup_user_frame()
        self.setup_file_frame()

        self.archive.pack(fill='both', expand=True)

        self.page = []
        page = [('page_Numeric_Editor', Editor.Numeric_Editor), 
                ('page_Artifact_Blueprint_Editor', Editor.Artifact_Blueprint_Editor), 
                ('page_Grids_Editor', Editor.Grids_Editor), 
                ('page_EnemyPool_Editor', Editor.EnemyPool_Editor)]
        for lbl,cls in page:
            new_page = cls(self.archive, self.datahandler)
            self.archive.add(new_page.frame, text = get_text(lbl))
            self.page.append(new_page)

        # 状态栏
        self.status = tk.StringVar()
        self.status.set(get_text("status_ready"))
        tk.Label(self.root, textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W).pack(fill=tk.X,side=tk.BOTTOM)

        # 保存
        self.output_btn=tk.Button(self.root, text=get_text("btn_save"),command=self.output_file,state="disabled")
        self.output_btn.pack(fill=tk.X,side=tk.BOTTOM)

    def setup_user_frame(self):
        """选择用户，单文件解压缩"""
        self.frame_user = tk.Frame(self.root)
        self.frame_user.pack(pady=10)
        self.username_label = tk.Label(self.frame_user, text=get_text("label_user") + self.username)
        self.username_label.pack(side=tk.LEFT)
        tk.Button(self.frame_user, text=get_text("btn_switch"), command=self.open_user_selector).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_user, text=get_text("btn_unzip"), command=self.single_decompress).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_user, text=get_text("btn_zip"), command=self.single_compress).pack(side=tk.LEFT, padx=5)

    def setup_file_frame(self):
        """存档选择，切换界面"""
        self.frame_file = tk.Frame(self.root)
        self.frame_file.pack(pady=10)
        self.filename_label = tk.Label(self.frame_file, text=get_text("label_lvl_null"))
        self.filename_label.pack(side=tk.LEFT)
        tk.Button(self.frame_file, text=get_text("btn_lvl"), command=self.open_save_selector).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_file, text=get_text("btn_open_explorer"), command=self.open_save_explorer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_file, text=get_text("btn_help"),command=self.open_help).pack(side=tk.LEFT, padx=10)
        # 混乱选项
        
    # 处理文件窗口
    def open_save_selector(self):
        """打开存档选择窗口"""
        Window.SaveFileSelector(
            parent=self.root,
            save_dir=get_save_path() + (f"\\user{self.currentUserIndex}\\mvz2\\level"),
            on_select=self.handle_save_selected  # 关键：选择后的回调
        )
        
    def handle_save_selected(self, selected_path):
        """处理选择的存档"""
        try:
            self.current_file = selected_path
            self.datahandler.current_data = json.loads(decompress(selected_path).decode("utf-8"),cls=CustonJson.CustomDecoder)
            self.filename_label.config(text=get_text("label_lvl") + os.path.basename(selected_path))
            self.output_btn.config(state="normal")
            self.refresh()
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
    # 帮助窗口
    def open_help(self):
        Window.HelpWindow(self.root)
    # 保存文件
    def output_file(self):
        save_dir=get_save_path() + f"\\user{self.currentUserIndex}\\mvz2\\level\\" + os.path.basename(self.current_file)
        output=json.dumps(self.datahandler.current_data,cls=CustonJson.CustomEncoder).encode("utf-8")
        self.status.set(get_text("status_save") + save_dir)
        compress(save_dir,output)
    # 打开存档文件夹
    def open_save_explorer(self):
        save_dir=get_save_path() + ("\\user%d\\mvz2\\level"%(self.currentUserIndex))
        subprocess.run(f'explorer "{os.path.normpath(save_dir)}"', shell=True)
    # 获取用户数据
    def get_usersdata(self):
        '''获取用户数据'''
        users_path = get_save_path() + "\\users.dat"
        self.users = json.loads(decompress(users_path),cls=CustonJson.CustomDecoder)
        self.currentUserIndex = self.users['currentUserIndex']
        self.username = self.users['metas'][self.currentUserIndex]['username']
    # 单文件解压
    def single_decompress(self):
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
    # 单文件压缩
    def single_compress(self):
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
    # 刷新
    def refresh(self):
        for page in self.page:
            page.refresh()

if __name__ == "__main__":
    # messagebox.showinfo("免责声明",f"使用该软件造成的文件损坏，本人一概不负责")
    root = tk.Tk()
    app = ArchiveEditor(root)
    root.mainloop()
