#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：2018/1/30
#模块描述：告警策略
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/alarm_configuration/")
from test_alarm import AlarmConfig

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class TestAlarmSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.alarmCase = AlarmConfig(self.browser)
        self.initDriver = initDriver()
        #前置条件
        self.commonSuite.alarm_strategy_module_prefix_condition()
        
    def test_alarm(self):
        #为用户添加邮箱
        self.alarmCase.mod_user_mail_008()
        #运行状态告警校验
        self.alarmCase.default_alarm_level_checkout_003()
        #配置高危运维
        self.alarmCase.command_alarm_level_config_001()
        #配置运行状态告警
        self.alarmCase.default_alarm_level_config_002()
        #配置认证失败告警
        self.alarmCase.auth_alarm_level_config_004()
        #告警归纳类型检索
        self.alarmCase.search_by_type_005()
        #告警归纳级别检索
        self.alarmCase.search_by_level_006()
        
    def tearDown(self):
        #后置条件
        self.commonSuite.alarm_strategy_module_post_condition()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)


if __name__ == "__main__":
    unittest.main()
