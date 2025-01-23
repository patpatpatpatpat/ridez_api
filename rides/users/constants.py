from django.db.models import TextChoices


class RideStatus(TextChoices):
    EN_ROUTE = "EN_ROUTE"
    PICK_UP = "PICK_UP"
    DROP_OFF = "DROP_OFF"
