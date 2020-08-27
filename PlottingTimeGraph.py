from Motion_Detector import df  
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool, ColumnDataSource

"""To convert the date time in string format"""
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d  %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d  %H:%M:%S") 

cds = ColumnDataSource(df)   #To extract the column data from the source file

p=figure(x_axis_type="datetime",height="100",width="500",responsive=True,title="Motion Graph")
p.yaxis.minor_tick_line_color=None  
p.ygrid[0].ticker.desired_num_ticks=1

"""HoverTool is used to display the information on any graph simply as a popup window"""
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])

q=p.quad(left=["Start"],right=["End"],bottom=0,top=1,color="green")

output_file("Motion_Graph.html")
show(p)
