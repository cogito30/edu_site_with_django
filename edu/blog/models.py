from django.db import models

"""
class ModelName(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.TextField()
    field3 = models.ForeignKey(ModelName,
                               related_name='model_related',
                               on_delete=models.CASCADE)
    class Meta:
        ordering = ['field1']

    def __str__(self):
        return self.field1
"""