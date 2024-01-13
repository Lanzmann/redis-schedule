from datetime import datetime
from django.apps import apps
from scheduler.celery import app

@app.task
def process_agenda_item(agenda_item_id):
    AgendaItem = apps.get_model('agenda', 'AgendaItem')
    agenda_item = AgendaItem.objects.get(id=agenda_item_id)
    
    # Processing logic goes here
    print(f"Processing {agenda_item.title}...")

    # Schedule the next run
    next_run = datetime.now() + agenda_item.interval
    process_agenda_item.apply_async((agenda_item.id,), eta=next_run)