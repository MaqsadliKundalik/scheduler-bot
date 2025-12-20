from tortoise import models, fields

class User(models.Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.CharField(max_length=15, unique=True)
    name = fields.CharField(max_length=300)
    phone_number = fields.CharField(max_length=20, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ConsultationState(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='consultations')
    age = fields.IntField(null=True)
    education_or_work = fields.TextField(null=True)
    question1 = fields.TextField(null=True)
    question2 = fields.TextField(null=True)
    question3 = fields.TextField(null=True)
    question4 = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"ConsultationState of {self.user.name}"