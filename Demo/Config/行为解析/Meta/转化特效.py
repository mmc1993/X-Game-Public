# coding=utf-8

def 转化特效(output, args):
    output.append("var self = actor as Effect;")
    output.append("var attack = self.GetState<Behavior.ParamAttack>();")
    output.append("var select = attack.SelectParam;")

