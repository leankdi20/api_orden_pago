import os
from celery import Celery

# Cambia 'app.settings' por 'api_orden_pago.settings' si ese es el nombre de tu proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_orden_pago.settings')
app = Celery('api_orden_pago')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    task_routes={
        # 'oktoquote.tasks.Desc_list_product': {'queue': 'default'},
        # 'oktoquote.tasks.comb_excels': {'queue': 'default'},
    }
)
