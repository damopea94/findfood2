import xlrd


def read_data(name):

    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_index(0)
    return sheet


def show_values():
    day=1;
    data= read_data("assign11-1-catering_sale_all.xls")
    for i in range(data.nrows):
        max = 0
        index=-1;
        for j in range(data.ncols):
            if j!=0 and i!=0:
                if data.cell_value(i,j) != "" and int(data.cell_value(i,j)) > max:
                    max = int(data.cell_value(i,j))
                    index=j

        print(day ,":" , data.cell_value(0, index))
        day=day+1;


show_values()