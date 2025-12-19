from tortoise import models, fields

class Post(models.Model):
    id = fields.IntField(pk=True)
    from_chat_id = fields.CharField(max_length=50)
    message_id = fields.IntField()
    send_time = fields.TimeDeltaField()
    
    def __str__(self):
        return self.from_chat_id
    
class ViewsPosts(models.Model):
    id = fields.IntField(pk=True)
    post = fields.ForeignKeyField('models.Post', related_name='views')
    user_telegram_id = fields.CharField(max_length=50)
    message_id = fields.IntField(null=True)
    viewed_at = fields.DatetimeField(auto_now_add=True)
    
    def __str__(self):
        return f"View by {self.user_telegram_id} on {self.viewed_at}"