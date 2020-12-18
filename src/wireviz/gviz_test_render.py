from graphviz import Digraph

dot = Digraph(format='png')
# フォント設定
dot.attr('node', fontname="MS Gothic")
# ノード作成
dot.node("項目1")
dot.node("項目2")
dot.node("項目3")
dot.node("項目4")
# エッジ作成
dot.edge("項目1", "項目2")
dot.edge("項目2", "項目3")
dot.edge("項目2", "項目4")
dot.render("test1")