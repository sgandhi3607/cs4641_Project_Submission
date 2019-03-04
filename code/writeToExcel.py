import xlsxwriter


def write(train, test, name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for i in range(len(train)):
        worksheet.write(row, col, train[i][0])
        worksheet.write(row, col + 1, train[i][1])
        worksheet.write(row, col + 2, test[i][1])
        worksheet.write(row, col + 3, test[i][2])
        row += 1
    workbook.close()


def writeOptimzationProblem(rhc, sa, ga, mimic, name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for i in range(len(rhc)):
        worksheet.write(row, col, rhc[i][0])
        worksheet.write(row, col + 1, rhc[i][1])
        worksheet.write(row, col + 2, rhc[i][2])
        col = col + 3

        worksheet.write(row, col + 1, sa[i][1])
        worksheet.write(row, col + 2, sa[i][2])
        col = col + 3
        worksheet.write(row, col + 1, ga[i][1])
        worksheet.write(row, col + 2, ga[i][2])
        col = col + 3
        worksheet.write(row, col + 1, mimic[i][1])
        worksheet.write(row, col + 2, mimic[i][2])
        row += 1
        col = 0
    workbook.close()




