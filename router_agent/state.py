"""客服会话状态定义。"""

from typing import TypedDict


class SupportState(TypedDict):
    """整张图共享的状态。"""

    user_input: str
    intent: str      # 识别出的意图：query / refund
    response: str    # 最终回复
