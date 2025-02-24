from django.core.exceptions import ValidationError


# Defining a validator to check image size
def validate_image_size(image):
    max_size_mb = 2

    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Images cannot be larger than {max_size_mb}MB.")
