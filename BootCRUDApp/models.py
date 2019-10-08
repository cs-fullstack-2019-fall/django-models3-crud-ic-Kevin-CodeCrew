from django.db import models


# Model class for an item for sale
class ItemModel(models.Model):
    itm_picture = models.CharField(max_length=255)
    itm_name = models.CharField(max_length=255)
    itm_description = models.TextField(max_length=255)
    itm_price = models.IntegerField(default=0)

    # Override toString()
    def __str__(self):
        return self.itm_name
