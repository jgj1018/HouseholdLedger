from django.db.models import manager

def filter_by_user_id(model:manager.Manager, kwarg: dict):
    return model.filter(**kwarg)