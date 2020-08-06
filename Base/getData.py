import json,os

class GetData:
    @classmethod
    def get_json_data(cls, file_name):
        """
        读取json文件
        :param file_name: 待读取data目录下json文件全名
        :return:
        """
        with open('data' + os.sep + file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data