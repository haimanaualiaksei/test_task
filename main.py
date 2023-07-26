# Task 1

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreditApplication(TimeStampedModel):
    contract = models.OneToOneField(
        'app.Contract',
        on_delete=models.SET_NULL,
        null=True,
        related_name='credit_application'
    )


class Contract(TimeStampedModel):
    pass


class Product(TimeStampedModel):
    name = models.TextField()
    manufacturer = models.ForeignKey(
        'app.Manufacturer',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    credit_application = models.ForeignKey(
        'app.CreditApplication',
        on_delete=models.CASCADE,
        related_name='products'
    )


class Manufacturer(TimeStampedModel):
    name = models.TextField()


# Task 2

contract_id = 32812
manufacturer_ids = CreditApplication.objects.filter(
    contract_id=contract_id
).values_list(
    'products__manufacturer_id',
    flat=True
).distinct()
