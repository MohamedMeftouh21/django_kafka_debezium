import faust
import json
from channels.layers import get_channel_layer
import os
import sys
import django
from asgiref.sync import sync_to_async
from django.core.mail import send_mail

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_saas.settings")

# Set PYTHONPATH before calling django.setup()
os.environ['PYTHONPATH'] = BASE_DIR

django.setup()
from django.conf import settings
from django_saas.urls import urlpatterns

app = faust.App('myapp',  broker='kafka:9092')
orders_topic = app.topic('source.public.base_customuser', value_serializer='raw', value_type=str)

@sync_to_async
def _do_something(event):
    print("event",event)

    send_mail(
    "Subject here",
    "Here is the message.",
    settings.EMAIL_HOST_USER,
    [event],
    fail_silently=False,
)
   

@app.agent(orders_topic)
async def send_data(stream):
    async for event_str in stream:
        try:
            event = json.loads(event_str)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            continue  

        sales_order_number = event.get('email', '')
        print("Before group_send")

        await _do_something(sales_order_number)


        print("L'instance de notifications a été mise à jour.")

# Define a periodic task to be executed every 60 seconds
@app.timer(interval=60.0)
async def periodic_task(app):
    print("Executing periodic task")
   # await _do_something("Periodic Task Event")

# Keep the Faust worker running
if __name__ == '__main__':
    app.main()
