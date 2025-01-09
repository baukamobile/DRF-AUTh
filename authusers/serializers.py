from rest_framework import serializers
from .models import AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['name','email','password']

    extra_kwargs = {
        'password':{'write_only':True}
    }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)


        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



# {
#     "name":"test1",
#     "email":"test1@gmail.com",
#     "password":"test1"
# }
# {
#     "name": "test1",
#     "email": "test1@gmail.com",
#     "password": "pbkdf2_sha256$870000$njHSZEIwz2dWRH89t18qt5$pmGUORYcTZE1f84AIlXLe/0otJVgI1bu0y1S9M5IhzE="
# }