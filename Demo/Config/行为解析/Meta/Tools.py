# coding=utf-8

def BuildArgs(master, sort, defs, fmt, output):
    args = []
    for _, port in enumerate(sort):
        assert port in master.Ins or port in defs, "[{0}]未定义且无默认值.".format(port)
        if not port in master.Ins:
            args.append(defs[port])
        else:
            args.append(master.Ins[port].Data)
    # print(master.Name, fmt.format(*args))
    output.append(fmt.format(*args))

_MapName = {
#   打击数值
    "范围": "Area",
    "标识": "Flags",
    "血量": "Attack",
    "硬直": "Stable",
    "推力时长": "ForceDuration",
    "推力距离": "ForceDistance",
    "停顿时长": "StopMotionTime",

#   Buff
    "Buff值": "BuffValue",
    "Buff开关": "BuffEnabled",
    "Buff时长": "BuffDuration",
    "Buff间隔": "BuffInterval",

#   筛选标志
    "任意阵营": "Const.BehaviorFlag.kSelectAny",
    "不同阵营": "Const.BehaviorFlag.kSelectXor",
    "相同阵营": "Const.BehaviorFlag.kSelectAnd",
    "包含自己": "Const.BehaviorFlag.kSelectSelf",
    "包含已死": "Const.BehaviorFlag.kSelectDead",
    "不能穿透": "Const.BehaviorFlag.kSelectOnlyOne",

    "攻方不停顿": "Const.BehaviorFlag.kStopMotionNotSender",
    "守方不停顿": "Const.BehaviorFlag.kStopMotionNotTarget",

    "向前推": "Const.BehaviorFlag.kForceForawrd",
    "扩散推": "Const.BehaviorFlag.kForceExplode",
    "向上推": "Const.BehaviorFlag.kForceUpward",

    "I": "|",
}

def MapName(name):
    if type(name) != str: return name
    if name in _MapName: return _MapName[name]
    for _, k in enumerate(_MapName):
        name = name.replace(k, _MapName[k])
    return name

def Tools():
    pass