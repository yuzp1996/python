from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
#    year Month predi  high low
    (2007, 8, 113.2, 114.2, 112.2),
    (2007, 9, 110.2, 113.2, 100.2),
    (2007, 10, 103.2, 107.2, 98.2),
    (2007, 11, 100.2, 102.2, 88.2),
    (2007, 12, 98.2, 100.2, 68.2),
    (2008, 1, 95.2, 98.2, 58.2),
    (2008, 2, 93.2, 95.2, 57.2),
    (2008, 3, 89.2, 92.2, 56.2),
    (2008, 4, 86.2, 88.2, 55.2),
    (2008, 5, 83.2, 82.2, 51.2),
]

drawing = Drawing(200, 150)

pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [200*((row[0] + row[1]/12.0)-2007)-110 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
