# 🚀 Lightweight Upscaler

极简的图像放大工具，无需完整 Stable Diffusion WebUI，直接使用 ESRGAN 模型进行批量放大。

## ✨ 特性

- **轻量依赖** - 仅需 `spandrel` + `torch`，无需加载完整 SD 模型
- **快速启动** - 只加载 upscale 模型，秒级启动
- **分块处理** - Tiled upscale 避免显存爆炸
- **多倍放大** - 支持 8x/16x 迭代放大
- **保留文件名** - 输出保留原文件名
- **Colab 友好** - 一键运行

## 📦 支持的模型

- 4x-UltraSharp (默认)
- 任意 ESRGAN 架构的 `.pth` 模型

## 🚀 快速开始

### Colab (推荐)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/lightweight-upscaler/blob/main/colab_upscale.ipynb)

1. 点击上方按钮打开 Colab
2. 运行所有 cell
3. 上传图片
4. 下载结果

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

## 📊 显存建议

| GPU | TILE_SIZE |
|-----|-----------|
| T4 (16GB) | 512 |
| V100/A100 | 768 |
| 显存不足 | 256 |

## 📝 License

MIT
