from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from sys import maxsize

def positive_int_type(value):
    if isinstance(value, str):
        raise ValidationError(
            _('This is type error, %(value) is string type'),
            params={'value': value},
        )
    if value < 0:
        raise ValidationError(
            _('%(value) is lower than 0'),
            params={'value': value},
        )
    if value > maxsize:
        raise ValidationError(
            _('%(value) is over the scope of system'),
            params={'value': value},
        )

def type_in_range(value):
  lst = [1, 2, 3]
  if value not in lst:
    raise ValidationError(
      _('%(value) is out of scope'),
      params={'value': value},
    )



