# coding: gb2312

"""
����Excelģ��

Version:0.1
Authon:������
Date:20190604
"""
import xlsxwriter

#������һ��Excel �ļ�
workbook = xlsxwriter.Workbook('deo1.xlsx')
#������һ�����������
worksheet = workbook.add_worksheet()
#���õ�һ�У�A�����Ϊ20����
worksheet.set_column('A:A', 20)
#����һ���Ӵֵĸ�ʽ����
bold = workbook.add_format({'bold': True})
#A1��Ԫ��д��'Hello'
worksheet.write('A1','Hello')
#A2��Ԫ��д��'World'�����üӴָ�ʽ����bold
worksheet.write('A2','World',bold)
#B2��Ԫ��д�����Ĳ����üӴָ�ʽ����bold
worksheet.write('B2',u'���Ĳ���','bold')

#�����б�ʾ��д������'32'�롮35.5��
worksheet.write(2,0,32)
# #���б�ʾ���ĵ�Ԫ���±���0��Ϊ��ʼֵ����3,0���ȼ��ڡ�A3��
# worksheet.write(3,0,35.5)
# #��A3:A4�ĺͣ��������д��'4,0',����A5��
# worksheet.write(4,0, '=SUM(A3:A4)')

#��B5��Ԫ�����ͼƬ
# worksheet.insert_image('B5','img/python-logo.png')
#�ر�Excel�ļ�
workbook.close()