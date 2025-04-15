# MVZ2SaveModifier/MVZ2存档修改器

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

一个用于编辑《MinecraftVSZombies2》游戏存档的图形化工具，支持修改数值、管理制品/蓝图、切换用户等功能。  
A graphical tool for editing *MinecraftVSZombies2* game saves, supporting numeric modifications, artifact/blueprint management, and user switching.


## 使用说明 / Usage

### 依赖项 / Dependencies
- Python 3.7+
- 必需库：`tkinter`, `gzip`, `shutil`, `json`  
  Required Libraries: `tkinter`, `gzip`, `shutil`, `json`

### 运行步骤 / Steps
1. **克隆仓库**  
   ```bash
   git clone https://github.com/QoZnoS/MVZ2SaveModifier.git
   cd MVZ2SaveModifier
   ```

2. **启动编辑器**  
   ```bash
   python MainEditor.py
   ```

### 适配 Pydroid 3 运行及修改方法
1. **克隆仓库**

2. **添加 setting.json**
新建一个 setting.json 文件，并向其中添加存档读取路径，比如：
   ```json
   {
    "base_path": "/storage/emulated/0/MVZ2/userdata"
   }
   ```

3. **修改相关代码**
- 在 Start.py 中，取消第5行，第12行和第13行的注释
- 替换 Start.py 中所有双重反斜杠(\\)为正斜杠(/)
- 在 NameData.py 中，删除"语言选择窗口"的全部内容（2.0版本为94~182行）

4. **运行脚本**
在 Pydroid 3 中运行 Start.py
---

## 免责声明 / Disclaimer

此工具仅供学习和测试使用，开发者不对因滥用或操作失误导致的存档损坏负责。  
**This tool is for educational and testing purposes only. The developer is not responsible for any save file corruption caused by misuse.**

---

## 开源协议 / License

本项目基于 [MIT License](LICENSE) 开源。  
This project is open-source under the [MIT License](LICENSE).
