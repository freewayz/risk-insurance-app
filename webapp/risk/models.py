from django.db import models
from django.utils.timezone import now


FIELD_TYPES = (
    ('TEXT', 'TEXT'),
    ('NUMBER', 'NUMBER'),
    ('DATE', 'DATE'),
    ('OPTIONS', 'OPTIONS')
)


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.date_modified = now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class RiskType(BaseModel):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=False)


    class Meta:
        db_table = 'risk_type'
        

class RiskFormField(BaseModel):
    risk_type = models.ForeignKey(to=RiskType, on_delete=models.CASCADE, null=True)
    label = models.CharField(max_length=200, blank=False)
    field_type = models.CharField(choices=FIELD_TYPES, default="TEXT", max_length=100)

    class Meta:
        db_table = 'risk_form_field'


class RiskFormFieldOption(BaseModel):
    label = models.CharField(max_length=100)
    form_field = models.ForeignKey(to=RiskFormField, 
                            on_delete=models.SET_NULL, 
                            null=True)
    class Meta:
        db_table = 'risk_form_field_option'


