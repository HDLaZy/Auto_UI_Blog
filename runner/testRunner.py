"""
生成测试报告
"""
import unittest
from HTMLTestRunner import HTMLTestRunner
from datetime import time, datetime




class TestRunner:

    sender = ''
    code = ''
    receiver = ''

    def run_self(self):
        #创建一个测试套件对象，测试套件理解为容器
        suite=unittest.TestSuite()
        #将测试用来放入容器  测试用例必须基础为unittesst.TestCase  测试用例类的路径  测试用例名
        suite.addTests(unittest.TestLoader().discover(start_dir='../test', pattern='login_fail_test.py'))
        suite.addTests(unittest.TestLoader().discover(start_dir='../test', pattern='login_success_test.py'))
        suite.addTests(unittest.TestLoader().discover(start_dir='../test', pattern='list_blog_test.py'))
        suite.addTests(unittest.TestLoader().discover(start_dir='../test', pattern='add_blog_success_test.py'))
        #生成的测试报告为html类型的文件
        dt=datetime.now()
        timestamp=dt.strftime('%Y-%m-%d %H-%M-%S')
        filename=f'../report/report{timestamp}.html'
        report=open(f'{filename}',mode='wb')
        #创建用例运行器 将report以流的方式放入，设置标题，设置描述
        runner=HTMLTestRunner(stream=report,title='博客测试报告',description='测试报告')
        #执行用例，生成报告
        runner.run(suite)
        #Util.send_email(f'{filename}', TestRunner.sender, TestRunner.code, TestRunner.receiver)

if __name__=='__main__':
    TestRunner().run_self()