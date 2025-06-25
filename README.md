# Real-Time AI Object Detection Web App (YOLOv8 + FastAPI)

这是一个基于 **YOLOv8**、**FastAPI** 和 **WebSockets** 构建的实时 AI 目标检测 Web 应用。它能够捕获你的摄像头视频流，通过 AI 模型实时识别画面中的物体，并在浏览器上展示标注后的视频。

---

## ✨ 功能特性

- **实时检测**: 使用高效的 YOLOv8n 模型进行实时目标检测。
- **Web 界面**: 通过浏览器即可访问，无需安装桌面应用。
- **高性能后端**: 基于 FastAPI 构建，采用异步处理，性能卓越。
- **实时视频流**: 使用 WebSockets 实现低延迟的视频帧传输。
- **跨平台**: 只要有 Python 和浏览器，就可以在 Windows, macOS, Linux 上运行。

## 🛠️ 技术栈

- **后端**: Python 3.8+, FastAPI, Uvicorn
- **AI 模型**: YOLOv8 (Ultralytics)
- **计算机视觉**: OpenCV-Python
- **前端**: HTML, CSS, JavaScript (WebSocket API)
- **环境管理**: venv

## 🚀 快速开始

请按照以下步骤在你的本地机器上运行本项目。

### 1. 克隆仓库

```bash
git clone https://github.com/Elsaakksh/ai-object-detection-web-app.git
cd ai-object-detection-web-app


2. 创建并激活虚拟环境
Generated bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


3. 安装依赖
项目的所有依赖都记录在 requirements.txt 文件中。
Generated bash
pip install -r requirements.txt


4. 运行应用
Generated bash
uvicorn main:app --reload

服务器启动后，你会在终端看到类似 Uvicorn running on http://127.0.0.1:8000 的信息。


5. 访问应用
打开你的浏览器，访问 **http://127.0.0.1:8000**。应用会自动请求摄像头权限，然后开始实时检测！


📝 项目结构

.
├── main.py             # FastAPI应用主文件
├── templates/
│   └── index.html      # 前端页面
├── .gitignore          # Git忽略文件配置
├── README.md           # 项目说明
└── requirements.txt    # Python依赖列表


致谢
感谢 Ultralytics 提供了强大的YOLOv8模型。
感谢 FastAPI 的开发者们。


```
