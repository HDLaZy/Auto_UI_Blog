"""
工具类:
"""
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import openpyxl

class Util(object):

    #获取excel内容
    @staticmethod
    def get_excel(bookname,sheetname):
        workbook=openpyxl.load_workbook(bookname)
        worksheet=workbook[sheetname]
        result=[]
        for row in worksheet:
            t=[]
            for cell in row:
                t.append(cell.value)
            result.append(tuple(t))
        #返回内容，不包含数据说明行
        return result[1:]

    #日志
    @staticmethod
    def get_log(filename,level=logging.DEBUG):
        # 创建日志对象
        logger = logging.getLogger()
        #设置日志等级
        logger.setLevel(level)
        # 设置日志格式
        formatter = logging.Formatter('[%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)s]')
        # 创建文件处理器对象 设置文件名，写策略，编码格式
        fh = logging.FileHandler(filename, mode='a', encoding='utf-8')
        #设置输出格式
        fh.setFormatter(formatter)
        #添加文件处理器对象
        logger.addHandler(fh)
        #返回日志对象
        return logger


    #邮件
    @staticmethod
    def send_email(filename,sender,code,receiver):
        server = 'smtp.163.com'
        port = 25
        mail = MIMEMultipart()
        mail['from'] = sender
        mail['to'] = receiver
        mail['subject'] = 'ranzhi自动化测试报告第一期!!!'
        with open(filename, 'rb')as file:
            report = file.read()
        attachment = MIMEText(report, 'base64', 'utf-8')
        attachment['Content-Type'] = 'application/octet-stream'
        attachment['Content-Disposition'] = 'attachment;filename=%s' % filename.split('\\')[-1]
        mail.attach(attachment)
        content = """
        <p>&nbsp;&nbsp;&nbsp;&nbsp;ranzhi项目的自动化测试报告以及完成请过目!</p>
        """
        body = MIMEText(content, 'html', 'utf-8')
        mail.attach(body)
        smtp = smtplib.SMTP()
        smtp.connect(server, port)
        smtp.login(sender, code)
        smtp.sendmail(sender, receiver.split(';'), mail.as_string())
        smtp.close()
        print('邮件发送完毕')





