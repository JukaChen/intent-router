"""组装图、编译，并导出 app。"""

from langgraph.graph import END, START, StateGraph

from .nodes import classify_node, handle_query, handle_refund
from .routing import route_by_intent
from .state import SupportState

graph = StateGraph(SupportState)
graph.add_node("classify", classify_node)
graph.add_node("handle_query", handle_query)
graph.add_node("handle_refund", handle_refund)

graph.add_edge(START, "classify")
# 条件边：classify 运行完后，由 route_by_intent 决定下一步
graph.add_conditional_edges(
    "classify",
    route_by_intent,
    {
        "handle_query": "handle_query",
        "handle_refund": "handle_refund",
    },
)
graph.add_edge("handle_query", END)
graph.add_edge("handle_refund", END)

app = graph.compile()


if __name__ == "__main__":
    print(app.invoke({"user_input": "我的订单到哪了？"}))
    print(app.invoke({"user_input": "这个我要退款"}))
