from django.db.models import manager

def filter_by_params(model:manager.Manager, kwarg: dict):
    return model.filter(**kwarg)