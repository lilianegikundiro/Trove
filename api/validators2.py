from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

username_validator = RegexValidator(
    regex=r'^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$',
    message='Username must start with a letter, and can contain letters, numbers, or underscores. It cannot start or end with an underscore.',
    code='invalid_username'
)

# Add minimum and maximum length validators
min_length_validator = MinLengthValidator(limit_value=3, message='Username must be at least 3 characters long.')
max_length_validator = MaxLengthValidator(limit_value=30, message='Username cannot exceed 30 characters.')


import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def password_validator(password):
    if (
        len(password) < 8 or
        not re.search(r'[a-zA-Z]', password) or
        not re.search(r'\d', password) or
        not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password)
    ):
        raise ValidationError(
            _("Password must be at least 8 characters long and include at least one letter, one number, and one special character."),
            code='invalid_password'
        )
