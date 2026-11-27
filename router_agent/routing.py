"""条件边的路由函数。"""

from typing import Literal

from .state import SupportState


def route_by_intent(state: SupportState) -> Literal["handle_query", "handle_refund"]:
    """根据 classify 写入的 intent 决定走哪个节点。"""
    if state["intent"] == "refund":
        return "handle_refund"
    return "handle_query"
