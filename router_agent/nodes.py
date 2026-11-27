"""图中的各个节点。"""

from .state import SupportState


def classify_node(state: SupportState) -> dict:
    """意图识别（模拟，实际可调 LLM）。"""
    text = state["user_input"]
    if "退" in text or "退款" in text:
        return {"intent": "refund"}
    return {"intent": "query"}


def handle_query(state: SupportState) -> dict:
    return {"response": "正在为您查询订单状态..."}


def handle_refund(state: SupportState) -> dict:
    return {"response": "已为您转接退款专员，请稍候。"}
