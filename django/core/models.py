from django.db import models

class Stock(models.Model):
    """
    Stock Model to store all the basic information
    """
    symbol = models.CharField(verbose_name="Symbol", max_length=10)
    name = models.CharField(verbose_name="Name", max_length=100)
    is_owned = models.BooleanField(verbose_name="Owned", default=False)
    is_desired = models.BooleanField(verbose_name="Desired", default=True)

    class Meta:
        verbose_name = "stock"
        verbose_name_plural = "stocks"

    def __str__(self):
        return f'{self.symbol} - {self.name}'


class StockInfo(models.Model):
    """
    StockInfo Model to store all de values of the day.
    """
    stock = models.ForeignKey("core.Stock", verbose_name="Stock", on_delete=models.CASCADE)
    open_value = models.FloatField(verbose_name="Open")
    close_value = models.FloatField(verbose_name="Close")
    high_value = models.FloatField(verbose_name="High")
    low_value = models.FloatField(verbose_name="Low")
    adjust_open_value = models.FloatField(verbose_name="Adjust Open")
    adjust_close_value = models.FloatField(verbose_name="Adjust Close")
    adjust_high_value = models.FloatField(verbose_name="Adjust High")
    adjust_low_value = models.FloatField(verbose_name="Adjust Low")
    dividend = models.FloatField(verbose_name="Dividend")
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)

    class Meta:
        verbose_name = "stock info"
        verbose_name_plural = "stock infos"

    def __str__(self):
        return f'{self.stock.symbol} - {self.stock.name} - {self.close_value} - {self.created_at}'
