import codecs
import pandas as pd
import os
import xlrd
plot = """
 <!DOCTYPE html>
<html lang="ru">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Title</title>
</head>
<body>
%s
</body>
</html>
"""
plot1 = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.js" charset="utf-8"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" charset="utf-8">

  <title>Document</title>
</head>
<body>
  <div class="container">
    <canvas id="myChart"></canvas>
</div>

<script>
  let myChart = document.getElementById('myChart').getContext('2d');

  let lineChart = new Chart(myChart,{ type: 'line', data: {labels: %s, datasets:
                [
                    {data: %s, label: "Температура", borderColor: "#009494", fill: false},
                    {data: %s, label: "Wetness", borderColor: "#76116d", fill: false},
                    {data: %s, label: "Q GazGen", borderColor: "#4a2339", fill: false},
                    {data: %s, label: "Q Kotelnaya", borderColor: "#542323", fill: false},
                    {data: %s, label: "Gkkal Kotelnaya", borderColor: "#584b3a", fill: false},
                    {data: %s, label: "Temperature 1", borderColor: "#937d62", fill: false},
                    {data: %s, label: "Temperature 2", borderColor: "#800000", fill: false},
                    {data: %s, label: "Temperature 1+2", borderColor: "#bc8f8f", fill: false},
                    {data: %s, label: "Temperature Obratka", borderColor: "#8382ff", fill: false},


                ]},
            options: {title: {display: true, text: 'Parametri v vide gradicov'}}});
</script>
</body>
</html>
"""
for i in os.scandir("xls"):
    filexls = "xls/" + i.name
    filehtml = "html/" + i.name[0:10]+".html"
    filegraph = "graph/" + i.name[0:10]+".html"

    wb = pd.read_excel(filexls, keep_default_na=False, header=None, encoding='UTF-8') # This reads in your excel doc as a pandas DataFrame
    wb.to_html(filehtml)

    f= open(filehtml, 'r')
    file=[]
    for line in f: file.append(line)

    f  = open(filehtml, 'w')
    f.write(plot % (' '.join(file)))
    f.close()

    f = codecs.open(filehtml, 'r', 'cp1251')
    u = f.read()   # now the contents have been transformed to a Unicode string
    out = codecs.open(filehtml, 'w', 'utf-8')
    out.write(u)   # and now the contents have been output as UTF-8
# _____________________________________________________________________________________________________
    def read_xls(name, id):
        name1=[]
        name1 = pd.read_excel(name, keep_default_na=False, header=None,encoding='UTF-8').values.tolist()[id][2:-1]
        [*name1] = map(str, name1)
        return name1
        # Ф-я - считывает данные из .xls переводит их list.Значение находится в [0] а первые 2 пустых поэтому [2:-1]
        # аргументы - название и номер строки
    f = open(filegraph, 'w')
    f.write(
        plot1 % (read_xls(filexls, 0), read_xls(filexls, 2), read_xls(filexls, 3), read_xls(filexls, 4),
                 read_xls(filexls, 5), read_xls(filexls, 6), read_xls(filexls, 9), read_xls(filexls, 10),
                 read_xls(filexls, 11), read_xls(filexls, 12)))
    f.close()


# # f = open('index2.html', 'w')
# # ################Считывание инфы для графиков
# # tempw, vlajw, qgazgen, qkot, gkalkot, t1, t2, tob, tpod, hour = [], [], [], [], [], [], [], [], [], []
# #
# # def read(name, id):
# #     for i in range(m): name.append(
# #         xlrd.open_workbook(filename, formatting_info=True).sheet_by_index(0).cell(id, i + 2).value)  # Энергоцентр
# #     [*name] = map(str, name)
# #     return name
#tempw, vlajw, qgazgen, qkot, gkalkot, t1, t2, tob, tpod, hour = [], [], [], [], [], [], [], [], [], []

#print(pd.read_excel("xls/2019.02.19.xls", keep_default_na=False, header=None, encoding='UTF-8').values.tolist()[2][2:-1])


