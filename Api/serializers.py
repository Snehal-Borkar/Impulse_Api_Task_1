
from rest_framework import serializers
from .models import Sample_Details
class Sample_Details_Serializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=70)
    description=serializers.CharField(max_length=70)
    email=serializers.EmailField()
    # createdAt=serializers.DateTimeField(auto_now_add=True)
    class Meta:
        model =Sample_Details
        fields=['id','name','description','email','createdAt'] 