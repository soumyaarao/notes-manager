from django.db import models
from bcrypt import checkpw, gensalt, hashpw

class CustomUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.username

    @staticmethod
    def generate_password_hash(password):
        password_bytes = password.encode('utf-8')
        generated_salt = gensalt()
        password_hash = hashpw(password_bytes, generated_salt)
        return password_hash

    def set_password(self, password):
        password_hash = self.generate_password_hash(password)
        self.password = password_hash.decode('utf-8')

    def check_password(self, password):
        if checkpw(password.encode('utf-8'), self.password.encode('utf-8')):
            return True
        return False

    def log_in(self, password):
        if self.password and not self.check_password(password):
            # Already Registered user with wrong credentials
            return False
        self.is_active = True
        # No password set -> User Registration OR password match
        return True

    def log_out(self):
        self.is_active = False
        return True

