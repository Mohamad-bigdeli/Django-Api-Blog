from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers 
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extera_fields):
        """
        Creates and saves a User with the given email and password and extera data.
        """    
        if not email:
            raise ValueError(_("the Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extera_fields):
        """
        Creates and saves a User with the given email and password and extera data.
        """        
        extera_fields.setdefault("is_staff", True)
        extera_fields.setdefault("is_superuser", True)
        extera_fields.setdefault("is_active", True)
        extera_fields.setdefault("is_verified", True)

        if extera_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is is_staff=True"))
        if extera_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is is_superuser=True"))

        return self.create_user(email, password, **extera_fields) 