import xlrd


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            excel_path = 'E:/code/PyChram_python/aigate_login/config/casedata.xls'
        if index == None:
            index = 0
        # 打开excel
        self.data = xlrd.open_workbook(excel_path)

        self.table = self.data.sheets()[index]
        # 行数
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result


if __name__ == '__main__':
    ec = ExcelUtil()
    print(ec.get_data())

