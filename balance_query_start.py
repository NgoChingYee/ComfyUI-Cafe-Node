# -*- coding: utf-8 -*-
import requests
import json

class BalanceQueryStartNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "trigger_image": ("IMAGE",),
            },
            "required": {
                "seed": ("INT", {
                    "default": 114514,
                    "min": 0,
                    "max": 2147483647
                }),
                "api_key": ("STRING", {
                    "default": "请输入API密钥",
                    "multiline": False
                }),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT",)
    RETURN_NAMES = ("balance_text", "balance_float")

    FUNCTION = "query_balance"
    CATEGORY = "Cafe_Nodes/查询余额☕️"

    def query_balance(self, trigger_image=None, seed=0, api_key=""):
        """
        trigger_image 现在是可选的：仅作为触发，不参与逻辑。
        seed 仍然可以作为输入，供工作流控制使用。
        """

        url = "https://api.comfy.org/customers/balance"
        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
        except Exception as e:
            return (f"请求失败: {str(e)}", 0.0)

        try:
            data = resp.json()
        except:
            return ("返回内容不是 JSON", 0.0)

        if "amount_micros" not in data:
            return ("JSON 中未找到 amount_micros", 0.0)

        try:
            amount = float(data["amount_micros"]) / 100
            balance_str = f"{amount:.2f}"
        except:
            return ("解析失败", 0.0)

        return (balance_str, amount)
