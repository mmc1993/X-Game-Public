# coding=utf-8

def 转化角色(master, output):
    output.append("var self = actor as Role;")
    output.append("var select = self.GetState<Behavior.ParamSelect>();")
    output.append("var attack = new Behavior.ParamAttack() { SelectParam = select };")
