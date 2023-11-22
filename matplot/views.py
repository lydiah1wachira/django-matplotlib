from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  # Import plt from Matplotlib
from io import BytesIO
import base64
from .models import Editors

def line_chart_view(request):
    editors_data = Editors.objects.all()

    labels = [editor_data.editor_name for editor_data in editors_data]
    data = [editor_data.num_users for editor_data in editors_data]

    # Create a line chart using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(labels, data, label='# of Users', marker='o', color='b')
    ax.set_xlabel('Editor Name')
    ax.set_ylabel('# of Users')
    ax.set_title('Line Graph')
    ax.legend()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    # Embed the image in the HTML response
    data_uri = base64.b64encode(buf.read()).decode('utf-8')
    img_tag = f'<img src="data:image/png;base64,{data_uri}" alt="Line Graph">'

    return HttpResponse(img_tag)



def bar_chart_view(request):
    editors_data = Editors.objects.all()

    labels = [editor_data.editor_name for editor_data in editors_data]
    data = [editor_data.num_users for editor_data in editors_data]

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(labels, data, color='blue', alpha=0.7)
    ax.set_xlabel('Editor Name')
    ax.set_ylabel('# of Users')
    ax.set_title('Bar Chart')

    # Save the figure to a BytesIO object
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    # Return the image directly in the HTTP response
    response = HttpResponse(content_type='image/png')
    response.write(buf.read())
    
    return response   
  

    