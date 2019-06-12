#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time        : 2019/1/17 19:57
# @Author      : Spareribs
# @File        : 06_group_member.py
# @Software    : PyCharm
# @Description :
"""

from wxpy import *

bot = Bot(cache_path=True)

# 机器人账号自身z
myself = bot.self

# 给机器人自己发送消息
bot.self.send(u'Hello World!')

group_fzr = bot.groups().search(u'农工院40年院庆篮球筹备群')[0]
group_zj = bot.groups().search(u'农工院40年院庆篮球筹备群')[0]
group_zzj = bot.groups().search(u'农工院40年院庆篮球筹备群')[0]
print(group_fzr, group_zj, group_zzj)

members_list = []
for fzr in group_fzr.members:
    members_list.append(fzr)
    print(type(group_fzr.members))
    # print fzr.is_friend, fzr.name, fzr.nick_name
# for zj in group_zj.members:
#     members_list.append(zj)
    # print zj.is_friend, zj.name, zj.nick_name
# for zzj in group_zzj.members:
#     members_list.append(zzj)
    # print zzj.is_friend, zzj.name, zzj.nick_name

print(len(members_list))
members_set = set(members_list)
print(len(members_set))
for mem in members_set:
    # print mem.is_friend, mem.name, mem.nick_name
    print(mem.name)
    # print(mem.nick_name)
    # print(mem.display_name)

