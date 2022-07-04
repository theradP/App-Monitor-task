import pandas as pd
from .models import InstallDetails
from celery import shared_task


@shared_task(name="update_installs")
def update_installs():
    file = "static/csv/installs - installs.csv"
    df = pd.read_csv(file)
    data = []
    for i in df.to_dict('records'):
        data.append(InstallDetails(**i))
    InstallDetails.objects.bulk_create(data)
