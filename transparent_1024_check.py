# -*- coding: utf-8 -*-

import torch
import numpy as np

class Transparent1024Check:
    """
    检测输入图片是否为 1024x1024 的纯透明图
    如果是，则直接抛出错误；否则，原样输出
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "check"
    CATEGORY = "图像处理☕️"

    def check(self, image):
        """
        image: torch.Tensor
        shape: (B, H, W, C)
        value range: [0, 1]
        """

        # 取 batch 中第一张（ComfyUI 标准做法）
        img = image[0]

        if img.ndim != 3:
            return (image,)

        h, w, c = img.shape

        # 只关心 1024x1024 + RGBA
        if h == 1024 and w == 1024 and c == 4:
            # Alpha 通道
            alpha = img[:, :, 3]

            # 判断是否全透明（浮点安全写法）
            if torch.all(alpha <= 0.0):
                raise RuntimeError(
                    "！！！检测到1024×1024的纯透明RGBA图片，流程已中断！！！"
                )

        return (image,)
