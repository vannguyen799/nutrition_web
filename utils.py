from django.utils import timezone


def prepared_file(file):
    if file:
        file.name = f'{timezone.now()}.{file.name}'