from .mask_frame_cafe import maskframecafe   
from .RGBA2RGB import RGBA2RGB
from .get_pic_name import GPICNAME
from .load_img_from_path_1by1 import load_images_from_the_path_one_by_one
from .pixian_rmbg import PixianRMBG
from .randomly_delete_noncore_prompt import RandomlyDeleteNoncorePrompt
from .loadimg import LoadImg
from .cafetextsave import CafeSaveText
from .balance_query_start import BalanceQueryStartNode
from .balance_query_end import BalanceQueryEndNode
from .transparent_1024_check import Transparent1024Check

WEB_DIRECTORY = "./js"

NODE_CLASS_MAPPINGS = {
    "自定义蒙版外框☕️": maskframecafe,
    "RGBA转为RGB☕️": RGBA2RGB,
    "获取图片名称☕️": GPICNAME,
    "从路径依次加载图片☕️": load_images_from_the_path_one_by_one,
    "Pixian RMBG☕️": PixianRMBG,
    "随机删除非核心提示词☕️": RandomlyDeleteNoncorePrompt,
    "加载图像（✅透明通道✅文件名）☕️": LoadImg,
    "保存文本文件☕️": CafeSaveText,
    "任务开始时查询余额☕️": BalanceQueryStartNode,
    "任务结束时查询余额☕️": BalanceQueryEndNode,
    "🍌Nano空图判别器☕️": Transparent1024Check
    }