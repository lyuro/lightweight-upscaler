# 🚀 Lightweight Upscaler

> 版本：6

极简的图像放大工具，无需完整 Stable Diffusion WebUI，直接使用 ESRGAN 模型进行批量放大。

## ✨ 特性

- **轻量依赖** - 仅需 `spandrel` + `torch`，无需加载完整 SD 模型
- **快速启动** - 只加载 upscale 模型，秒级启动
- **分块处理** - Tiled upscale 避免显存爆炸
- **多倍放大** - 支持 8x/16x 迭代放大
- **保留文件名** - 输出保留原文件名
- **Colab 友好** - 一键运行

## 📦 支持的模型

| 模型 | 架构/大小 | 特点 | 推荐场景 |
|------|-----------|------|----------|
| **4x-UltraSharp** (默认) | ESRGAN / ~67 MB | 通用锐化型，速度快、显存友好，细节和纹理更强 | AI 图、插画、压缩图、不确定用哪个时 |
| **4x-Nomos8kDAT** | DAT / ~295 MB | 照片修复型，质量潜力更高，但更慢、更吃显存，使用 FP32 | 真实照片、JPEG 压缩、轻微模糊、resize 退化 |
| **4x-Nomos8kSC** | ESRGAN / ~67 MB | 照片均衡型，基于 Nomos8k_sfw 真实照片训练，处理 JPG 压缩和轻微模糊更稳 | 真实照片修复，想要比 UltraSharp 更偏照片取向时 |

简单选择：不确定先用 **4x-UltraSharp**；照片优先试 **4x-Nomos8kSC**；显存够且能接受慢一些，再试 **4x-Nomos8kDAT**。

## 🚀 快速开始

### Colab (推荐)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/lightweight-upscaler/blob/main/colab_upscale.ipynb)

1. 点击上方按钮打开 Colab
2. 运行所有 cell
3. 上传图片
4. 下载结果

如果 Google Drive 挂载失败，notebook 会自动改用 `/content/upscale` 临时目录继续运行。临时目录会在 Colab 运行时断开或重启后清空，请及时下载输出文件；这种模式下最后的断开 cell 不会自动断开运行时。

### 本地运行

```bash
pip install spandrel torch pillow numpy tqdm

# 然后运行 notebook 或转换为 .py 脚本
```

## ⚙️ 配置

在 notebook 中修改：

```python
TARGET_SCALE = 8       # 目标放大倍数 (4/8/16)
MAX_SIDE_LENGTH = 8192 # 最大边长限制
TILE_SIZE = 512        # 分块大小 (显存不足可降低)
```

## 🔖 版本

版本号存放在 `VERSION`，并显示在 README 和 notebook 顶部。本仓库已配置 `.githooks/pre-commit`，每次提交前自动 `+1`；如果换机器或重新 clone，运行 `git config core.hooksPath .githooks` 启用 hook。

## 📊 显存建议

| GPU | TILE_SIZE |
|-----|-----------|
| T4 (16GB) | 512 |
| V100/A100 | 768 |
| 显存不足 | 256 |

## 📝 License

MIT
