from rest_framework import serializers
from .models import User, CodeGenerate, RegularUser, Branch

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'user_id', 'first_name', 'last_name', 'phone_number', 'phone_number2', 'points', 'age', 'date','is_admin', 'date_joined']



class CodeGenerateSeralizers(serializers.ModelSerializer):
    user_id  = serializers.IntegerField(source='user.user_id')

    class Meta:
        model=CodeGenerate
        fields=['id','user_id', 'code', 'discount',  'created_at', 'confirmed_presence']

    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = User.objects.get(user_id=user_id)
        address = CodeGenerate.objects.create(user=user, **validated_data)
        return address




class RegularUserSeralizers(serializers.ModelSerializer):
    user_id  = serializers.IntegerField(source='user.user_id')

    class Meta:
        model = RegularUser
        fields = ('id','user_id', 'summ', 'visits', 'discount', 'date_joined', )
    
    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = User.objects.get(user_id=user_id)
        address = RegularUser.objects.create(user=user, **validated_data)
        return address


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'location', 'opening_time', 'closing_time']