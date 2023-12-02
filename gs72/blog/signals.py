from django.dispatch import Signal, receiver

notification = Signal(['request','user'])


#receiver_function
@receiver(notification)
def show_notification(sender,**kwargs):
    print('sender:',sender)
    print(f'kwargs: {kwargs}')
    print('notification')