from .models import Company

def create_company(*, user, **validated_data):
    return Company.objects.create(owner=user, **validated_data)