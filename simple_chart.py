from openpyxl.chart import BarChart,Reference, Series
from openpyxl import Workbook

simple_chart_excel = Workbook()

sheet_1 = simple_chart_excel.active

for i in range(1,21):
    sheet_1.append([i])

values = Reference(sheet_1, min_col = 1, min_row = 1,
                            max_col = 1, max_row = 20)
series = Series(values = values, title = "Numbers_Tabel")

simple_chart = BarChart()
simple_chart.series.append(series)
simple_chart.title = "My First Chart"
simple_chart.x_axis.title = "Growth"
simple_chart.y_axis.title = "Numbers"
sheet_1.add_chart(simple_chart, "C3")

simple_chart_excel.save("simple_chart_excel.xlsx")
