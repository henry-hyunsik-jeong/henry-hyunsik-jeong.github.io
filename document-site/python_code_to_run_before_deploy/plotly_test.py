import plotly.express as px
import plotly.io as pio

# Creating the Figure instance

# Data to be plotted
df = px.data.iris()
 
# Plotting the figure
fig = px.scatter_3d(df, x = 'sepal_width',
                    y = 'sepal_length',
                    z = 'petal_width',
                    color = 'species')
 

pio.write_html(fig, file='public/plotly.html')#, auto_open=True)
