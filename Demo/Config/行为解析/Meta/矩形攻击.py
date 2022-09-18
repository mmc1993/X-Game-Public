# coding=utf-8

import Meta.Tools as Tools

def 矩形攻击(master, output):
    if len(master.Ins) == 0:
        sort = []
        defs = {}
        fmt = "{{                                                        \n\
                    var __ret__ = Behavior.MetaAttackQuad(attack);       \n\
                    if (__ret__.HasFlag(Const.MetaAttackResult.kAbort))  \n\
                    {{                                                   \n\
                        yield break;                                     \n\
                    }}                                                   \n\
                    if (__ret__.HasFlag(Const.MetaAttackResult.kStop))   \n\
                    {{                                                   \n\
                        yield return 1;                                  \n\
                    }}                                                   \n\
                }}"
        Tools.BuildArgs(master, sort, defs, fmt, output)
    else:
        sort = [ "命中特效" ]
        defs = {}
        fmt1 = "{{                                                                           \n\
                    var __ret__ = Behavior.MetaAttackQuad(attack, config.ID * 10 + {0});     \n\
                    if (__ret__.HasFlag(Const.MetaAttackResult.kAbort))                      \n\
                    {{                                                                       \n\
                        yield break;                                                         \n\
                    }}                                                                       \n\
                    if (__ret__.HasFlag(Const.MetaAttackResult.kStop))                       \n\
                    {{                                                                       \n\
                        yield return 1;                                                      \n\
                    }}                                                                       \n\
                }}"
        Tools.BuildArgs(master, sort, defs, fmt1, output)