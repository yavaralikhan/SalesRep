import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox, ttk

df = pd.read_csv('companies.csv')

X = df[['R&DSpend', 'MarketingSpend']]
Y = df['Profit']

model = LinearRegression()
model.fit(X, Y)


# GUI
root = Tk()

# Menubar
menubar = Menu(root)

fyle = Menu(menubar, tearoff=0)
fyle.add_separator()
fyle.add_command(label='Close', command=root.quit)
menubar.add_cascade(label='File', menu=fyle)

def about():
    messagebox.showinfo('About', 'Sales forecast')

help = Menu(menubar, tearoff=0)
help.add_command(label='About', command=about)
menubar.add_cascade(label='Help', menu=help)


root.geometry('800x600')
# Frames
content = ttk.Frame(root, padding=(5, 5, 5, 5))
frame = ttk.Frame(content, borderwidth=5)#, width=200, height=200)
frame_chart = ttk.Frame(content, borderwidth=5)#, width=200, height=200)
frame_chart_buttons = ttk.Frame(frame_chart)
frame_buttons = ttk.Frame(frame, borderwidth=5)#, relief="sunken", width=200, height=200)

# Frame Grid
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, sticky=(N, S, E, W))
frame_chart.grid(column=1, row=0, sticky=(N, S, E, W))
frame_chart_buttons.grid(column=0, row=0, sticky=(N, S, E, W))
frame_buttons.grid(column=1, row=6, sticky=(N, S, E, W))


# Predict Button
def onClick():
    # if entry_RnD.get() or entry_MK.get() == 0:
    #     messagebox.showwarning('Warning', 'Please enter variables to predict')
    RDSpend = float(entry_RnD.get())
    MKSpend = float(entry_MK.get())
    predictedProfit = model.predict([[RDSpend, MKSpend]])
    ttk.Label(frame, text='Prediciton:').grid(column=0, row=5, sticky=(N, W), padx=5)
    ttk.Label(frame, text=predictedProfit[0]).grid(column=1, row=5, sticky=(N, W), padx=5)


# Labels
label_RnD = ttk.Label(frame, text='R&D Spend: ')
label_MK = ttk.Label(frame, text='Marketing Spend: ')
label_intercept = ttk.Label(frame, text='Interceptor: ')
label_coefficient = ttk.Label(frame, text='Coefficient: ')
label_intercept_data = ttk.Label(frame, text=model.intercept_).grid(column=1, row=2, sticky=(N, W), padx=5)
label_coefficient_data = ttk.Label(frame, text=model.coef_).grid(column=1, row=3, sticky=(N, W), padx=5)

# Label Grid
label_RnD.grid(column=0, row=0, sticky=(N, W), padx=5)
label_MK.grid(column=0, row=1, sticky=(N, W), padx=5)
label_intercept.grid(column=0, row=2, sticky=(N, W), padx=5)
label_coefficient.grid(column=0, row=3, sticky=(N, W), padx=5)

# Entry
entry_RnD = ttk.Entry(frame)
entry_MK = ttk.Entry(frame)

# Grid Entry
entry_RnD.grid(column=1, row=0, sticky=(N, W), padx=5)
entry_MK.grid(column=1, row=1, sticky=(N, W), padx=5)

# Buttons
ok = ttk.Button(frame_buttons, text="Predict Profit")
cancel = ttk.Button(frame_buttons, text="Exit")

# Grid Buttons
ok.grid(column=0, row=4)
ok.configure(command=onClick)
cancel.grid(column=1, row=4)
cancel.configure(command=quit)

# Config.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)


# Graph
figure1 = plt.Figure(figsize=(7, 5), dpi=70)
subPlot1 = figure1.add_subplot(111)
subPlot1.scatter(df['R&DSpend'].astype(float), df['Profit'].astype(float), color='red')
subPlot1.set_xlabel("R&DSpend")
subPlot1.set_ylabel("Profit")
scatterGraph1 = FigureCanvasTkAgg(figure1, frame_chart)
scatterGraph1.get_tk_widget().grid(column=0, row=1)

# Plot 1st Scatter Graph - R&DSpend VS Profit
def graph_1():
    figure1 = plt.Figure(figsize=(7, 5), dpi=70)
    subPlot1 = figure1.add_subplot(111)
    subPlot1.scatter(df['R&DSpend'].astype(float), df['Profit'].astype(float), color='red')
    subPlot1.set_xlabel("R&DSpend")
    subPlot1.set_ylabel("Profit")
    scatterGraph1 = FigureCanvasTkAgg(figure1, frame_chart)
    scatterGraph1.get_tk_widget().grid(column=0, row=1)


# Plot 2nd Scatter Graph - MarketingSpend VS Profit
def graph_2():
    figure2 = plt.Figure(figsize=(7, 5), dpi=70)
    subPlot2 = figure2.add_subplot(111)
    subPlot2.scatter(df['MarketingSpend'].astype(float), df['Profit'].astype(float), color='green')
    subPlot2.set_xlabel("MarketingSpend")
    subPlot2.set_ylabel("Profit")
    scatterGraph2 = FigureCanvasTkAgg(figure2, frame_chart)
    scatterGraph2.get_tk_widget().grid(column=0, row=1)


rnd = ttk.Button(frame_chart_buttons, text='R&D Spend Graph')
rnd.grid(column=0, row=0, sticky=(N, W))
rnd.configure(command=graph_1)

mk = ttk.Button(frame_chart_buttons, text='Marketing Spend Graph')
mk.grid(column=1, row=0, sticky=(N, W))
mk.configure(command=graph_2)

root.config(menu=menubar)
root.mainloop()
