from mongoengine import Document, StringField

class Feedback(Document):
    name=StringField(max_length=200)
    image_url=StringField()
    link=StringField()