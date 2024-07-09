import os

import OlivOS

# 事件文档：https://doc.olivos.wiki/DevPlugin/Event/

class Event(object):
    """OlivOS 框架事件"""
    # 初始化事件
    def init(plugin_event: OlivOS.API.Event, Proc: OlivOS.pluginAPI.shallow):
        pass

    # 私聊消息事件
    def private_message(plugin_event: OlivOS.API.Event, Proc: OlivOS.pluginAPI.shallow):
        test_reply(plugin_event, Proc, "private")

    # 群聊消息事件
    def group_message(plugin_event: OlivOS.API.Event, Proc: OlivOS.pluginAPI.shallow):
        test_reply(plugin_event, Proc, "group")

def test_reply(plugin_event: OlivOS.API.Event, Proc: OlivOS.pluginAPI.shallow, message_type):
    data = plugin_event.data
    if data.message == '/ping':
        plugin_event.reply(f"这是一条 {message_type} 消息")
