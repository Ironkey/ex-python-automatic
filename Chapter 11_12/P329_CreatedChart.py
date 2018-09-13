import openpyxl
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
for i in range(1, 11):
    sheet['A' + str(i)] = i
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
charObj = openpyxl.chart.BarChart()
charObj.append(seriesObj)

sheet.add_chart(charObj)
wb.save('sampleChart.xlsx')