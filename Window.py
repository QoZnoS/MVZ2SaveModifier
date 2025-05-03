import tkinter as tk
from tkinter import ttk
import os
import webbrowser
import NameData

def get_text(id):
    """获取文本"""
    return NameData.texts.get_name(id)

_window_size = "600x400"
# 存档选择窗口
class SaveFileSelector(tk.Toplevel):
    def __init__(self, parent, save_dir, on_select):
        super().__init__(parent)
        self.parent = parent
        self.save_dir = save_dir
        self.on_select = on_select
        
        # 窗口设置
        self.title("SelectorLevel")
        self.geometry("600x400")
        self.transient(parent)  # 设置为父窗口的临时窗口
        self.grab_set()  # 设置为模态窗口
        
        # 创建组件
        self.create_widgets()
        self.refresh_list()
        
    def create_widgets(self):
        """创建界面组件"""
        # 文件列表
        self.tree = ttk.Treeview(
            self,
            columns=("name", "size", "modified"),
            show="headings",
            selectmode="browse"
        )
        self.tree.heading("name", text="存档名称/Level name")
        self.tree.heading("size", text="大小/Level size")
        self.tree.heading("modified", text="修改时间/Modified Date")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 操作按钮
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(
            btn_frame,
            text="取消/Cancel",
            command=self.destroy
        ).pack(side=tk.RIGHT, padx=3)
        
        ttk.Button(
            btn_frame,
            text="选择/Choose",
            command=self.confirm_selection
        ).pack(side=tk.RIGHT, padx=3)
        
        ttk.Button(
            btn_frame,
            text="刷新/Refresh",
            command=self.refresh_list
        ).pack(side=tk.LEFT)
        
    def refresh_list(self):
        """刷新文件列表"""
        self.tree.delete(*self.tree.get_children())
        for f in os.listdir(self.save_dir):
            if f.endswith((".lvl")):
                path = os.path.join(self.save_dir, f)
                stat = os.stat(path)
                self.tree.insert("", "end",
                    values=(
                        f,
                        f"{stat.st_size/1024:.1f} KB",
                        self.format_time(stat.st_mtime)
                    ))
                    
    def format_time(self, timestamp):
        """格式化时间戳"""
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime("%m-%d %H:%M")
        
    def confirm_selection(self):
        """确认选择"""
        selected = self.tree.selection()
        if not selected:
            return
            
        selected_file = os.path.join(
            self.save_dir,
            self.tree.item(selected[0])["values"][0]
        )
            
        # 执行回调并关闭窗口
        self.on_select(selected_file)
        self.destroy()

# 用户选择窗口
class UserSelector(tk.Toplevel):
    def __init__(self, parent, metas, on_select):
        super().__init__(parent)
        self.parent = parent
        self.metas = metas
        self.on_select = on_select

        # 窗口设置
        self.title("Selector User")
        self.geometry("600x400")
        self.transient(parent)  # 设置为父窗口的临时窗口
        self.grab_set()  # 设置为模态窗口
        
        # 用户列表
        self.tree = ttk.Treeview(
            self,
            columns=("id", "name"),
            show="headings",
            selectmode="browse"
        )
        self.tree.heading("id", text="用户存档路径id/User save path id")
        self.tree.heading("name", text="用户昵称/User name")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for user in self.metas:
            if user == None:
                continue
            self.tree.insert("", "end", values=(metas.index(user),user['username']))

        # 操作按钮
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(btn_frame, text="取消/Cancel", command=self.destroy).pack(side=tk.RIGHT, padx=3)
        ttk.Button(btn_frame, text="选择/Choose", command=self.confirm_selection).pack(side=tk.RIGHT, padx=3)
                
    def confirm_selection(self):
        """确认选择"""
        selected = self.tree.selection()
        if not selected:
            return
            
        selected_user = self.tree.item(selected[0])["values"][0]
            
        # 执行回调并关闭窗口
        self.on_select(selected_user)
        self.destroy()

class BlueprintSelector(tk.Toplevel):
    def __init__(self, parent, on_select):
        super().__init__(parent)
        self.parent = parent
        self.on_select = on_select

        # 窗口设置
        self.title("Selector Blueprint")
        self.geometry(_window_size)
        self.resizable(True, True)
        self.transient(parent)
        self.grab_set()

        # 主容器布局
        main_container = ttk.Frame(self)
        main_container.pack(fill=tk.BOTH, expand=True)

        # 创建滚动系统
        self.canvas = tk.Canvas(main_container)
        self.scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        # 关键修复：同步Canvas和滚动区域的宽度
        self.canvas.bind("<Configure>", 
            lambda e: self.scrollable_frame.config(width=e.width-20))  # 留出滚动条宽度

        # 配置Canvas
        self.scrollable_frame.bind("<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 布局滚动区域
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 底部操作按钮（独立于滚动区域）
        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        self.seed_text = tk.Label(self.btn_frame)
        self.seed_text.pack(side=tk.LEFT)
        ttk.Button(self.btn_frame, text="取消/Cancel", command=self.destroy).pack(side=tk.RIGHT, padx=3)
        ttk.Button(self.btn_frame, text="选择/Choose", command=self.confirm_selection).pack(side=tk.RIGHT, padx=3)

        # 按钮容器
        self.btn_container = ttk.Frame(self.scrollable_frame)
        self.btn_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.btn_list = []
        self.create_btn_list()
        
        self.last_size = (0, 0)
        self.bind("<Configure>", self.on_window_resize)
        
        # 初始布局
        self.setup_btn()

    def create_btn_list(self):
        for idx, seedID in enumerate(NameData.blueprints.zh_names):
            var = tk.BooleanVar()
            btn = tk.Button(self.btn_container, bg="white", 
                          command=lambda e=idx: self.toggle_btn(e))
            img = NameData.assets.get_blueprint(seedID)
            btn.config(image=img, width=85, height=85, compound=tk.CENTER)
            
            self.btn_list.append((var, btn, seedID, idx))

    def setup_btn(self):
        # 强制更新布局获取真实宽度
        self.update_idletasks()
        container_width = self.winfo_width()
        
        # 计算列数（最小1列）
        btn_size = 85
        columns = max(1, container_width // (btn_size + 5)) if container_width > 10 else 1

        for _, btn, _, idx in self.btn_list:
            row, col = divmod(idx, columns)
            btn.grid(row=row, column=col, sticky="nsew")

        # 配置网格列权重
        for col in range(columns):
            self.btn_container.columnconfigure(col, weight=1)

    def on_window_resize(self, event):
        global _window_size
        """改进的事件处理："""
        # 只处理顶层窗口事件
        if event.widget != self:
            return
        
        # 获取当前实际尺寸
        new_width = self.winfo_width()
        new_height = self.winfo_height()
        
        # 尺寸变化阈值检测（5像素容差）
        if (abs(new_width - self.last_size[0])) < 5 :
            return
        self.last_size = (new_width, new_height)
        _window_size = str(new_width) + "x" + str(new_height)

        self.setup_btn()

    def toggle_btn(self, enum):
        _, enum_btn, _, _ = self.btn_list[enum]
        for var, btn, seedID, _ in self.btn_list:
            if btn == enum_btn:
                if var.get():
                    self.confirm_selection()
                    return
                else:
                    var.set(True)
                    self.seed_text.config(text=NameData.blueprints.get_name(NameData.blueprints.get_id(seedID)))
            else:
                var.set(False)
            color = "lightgreen" if var.get() else "white"
            btn.config(bg=color)

    def confirm_selection(self):
        # 原有逻辑保持不变
        selected = None
        for var, btn, seedID, _ in self.btn_list:
            if var.get():
                selected = NameData.blueprints.get_id(seedID)
        if not selected:
            return
        self.on_select(selected)
        self.destroy()

# 关于
class HelpWindow:
    def __init__(self, parent):
        # 创建顶级窗口
        self.window = tk.Toplevel(parent)
        self.window.title("About")
        self.window.geometry("600x400")
        
        # 设置窗口图标（可选）
        # self.window.iconbitmap("icon.ico")
        
        # 主容器
        container = ttk.Frame(self.window)
        container.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # 文字信息
        text_content = get_text('help_1') + get_text('help_2') + get_text('help_3') + get_text('help_4') + get_text('help_5') + get_text('help_6')
        
        lbl_info = ttk.Label(
            container,
            text=text_content,
            justify="center",
            wraplength=600
        )
        lbl_info.pack(pady=10)
        
        # 链接按钮容器
        link_frame = tk.Frame(container)
        link_frame.pack(pady=15)
        
        # 创建链接按钮
        links = [
            (get_text('help_link1'), "https://space.bilibili.com/348514"),
            (get_text('help_link2'), "https://space.bilibili.com/404359179"),
            (get_text('help_link3'), "https://github.com/QoZnoS/MVZ2SaveModifier")
        ]
        
        for text, url in links:
            btn = tk.Button(
                link_frame,
                text=text,
                width=48,
                command=lambda u=url: self.open_link(u)  # 使用 lambda 绑定参数
            )
            btn.pack(side="top", pady=5)
        
    def open_link(self, url):
        """打开外部链接"""
        webbrowser.open_new(url)

