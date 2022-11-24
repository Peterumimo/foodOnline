from django.core.exceptions import ValidationError
import os

def allow_only_image_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extention = ['jpg','png','jpeg']
    if not ext.lower() in valid_extention:
        raise ValidationError('Unsupported file format. Allowed format:' +str(valid_extention))