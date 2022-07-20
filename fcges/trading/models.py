from django.db import models

STOCKS = (
    ('Jollibee', 'JFC'),
    ('Ayala Corporation', 'AC'),
    ('AllDay Mart', 'ALLDY'),
)

class Stocks(models.Model):
    stock_name = models.CharField(max_length=50, choices=STOCKS, null=True, blank=True)
    price = models.IntegerField()
    
    class Meta:
        db_table = 'stocks'
        verbose_name = 'Stocks'


class OrderBlock(models.Model):
    user_id = models.IntegerField()
    stock_id = models.ForeignKey('stocks', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'order_block'
        verbose_name = 'OrderBlock'
