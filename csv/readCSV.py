import csv

# csv.field_size_limit-返回解析器允许的当前最大字段大小。
# csv.get_dialect-返回与名称关联的方言。
# csv.list_dialects-返回所有已注册方言的名称。
# csv.reader-从csv文件读取数据
# csv.register_dialect-将方言与名称相关联。名称必须是字符串或Unicode对象。
# csv.writer-将数据写入csv文件
# csv.unregister_dialect-它从方言注册表中删除与该名称关联的方言。如果名称不是注册的方言名称，则将引发错误。
# csv.QUOTE_ALL-指示编写器对象引用所有字段。csv.QUOTE_MINIMAL-它指示编写器对象仅引用那些包含特殊字符（如quotechar，delimiter等）的字段。
# csv.QUOTE_NONNUMERIC-它指示编写器对象引用所有非数字字段。
# csv.QUOTE_NONE-它指示writer对象从不引用字段。

with open('python.txt') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    # print(csv_reader)
    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
            # print(f'Column names are {",".join(row)}')
            # line_count += 1
        # print(row)
        print(f'每行的数据为：{",".join(row)}')
