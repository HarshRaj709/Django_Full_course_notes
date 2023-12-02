from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
    print('-------------------------------------------')
    print('logged-in signals... Run Intro..')
    print('sender:',sender)
    print('request:',request)
    print('user_password:',user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender = User)
def logged_out(sender,request,user,**kwargs):
    print('-------------------------------------------')
    print('logged-out signals... Run Intro..')
    print('sender:',sender)
    print('request:',request)
    print('user_password:',user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(login_success,sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print('-------------------------------------------')
    print('login_failed signals... Run Intro..')
    print('sender:',sender)
    print('credentils:',credentials)
    print('request:',request)
    print(f'kwargs: {kwargs}')

# @receiver(pre_save,sender = User)
# def at_beginning_save(sender,instance,**kwargs):
#     print('-------------------------------------------')
#     print('Pre_save_signals... Run Intro..')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs: {kwargs}')

# @receiver(post_save,sender = User)
# def at_ending_save(sender,instance,created,**kwargs):
#     if created:
#         print('-------------------------------------------')
#         print('Post_save_signals... Run Intro..')
#         print('new record')
#         print('sender:',sender)
#         print('instance:',instance)
#         print('created',created)
#         print(f'kwargs: {kwargs}')
#     else:
#         print('-------------------------------------------')
#         print('Post_save_signals... Run Intro..')
#         print('Record Updated')
#         print('sender:',sender)
#         print('instance:',instance)
#         print('created',created)
#         print(f'kwargs: {kwargs}')


# @receiver(pre_delete,sender=User)
# def at_beginnig_delete(sender,instance,**kwargs):
#     print('-------------------------------------------')
#     print('Pre_delete_signals... Run Intro..')
#     print('Record Deleted')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs: {kwargs}')

# @receiver(post_delete,sender=User)
# def at_ending_delete(sender,instance,**kwargs):
#     print('-------------------------------------------')
#     print('Post_delete_signals... Run Intro..')
#     print('Record Deleted')
#     print('sender:',sender)
#     print('instance:',instance)
#     print(f'kwargs: {kwargs}')


# @receiver(pre_init,sender=User)
# def at_beginnig_init(sender,*args,**kwargs):
#     print('-------------------------------------------')
#     print('At begning init... Run Intro..')
#     print('Record Deleted')
#     print('sender:',sender)
#     print(f'Args:{args}')
#     print(f'kwargs: {kwargs}')

# @receiver(post_init,sender=User)
# def at_ending_init(sender,*args,**kwargs):
    # print('-------------------------------------------')
    # print('At ending init... Run Intro..')
    # print('Record Deleted')
    # print('sender:',sender)
    # print(f'Args:{args}')
    # print(f'kwargs: {kwargs}')

# @receiver(request_started)
# def at_begning_request(sender,environ,**kwargs):
#         print('-------------------------------------------')
#         print('At beginning Request... Run Intro..')
#         print('sender:',sender)
#         print('Environ:',environ)
#         print(f'kwargs: {kwargs}')

# @receiver(request_finished)
# def at_ending_request(sender,**kwargs):
#         print('-------------------------------------------')
#         print('At endinging Request... Run Intro..')
#         print('sender:',sender)
#         print(f'kwargs: {kwargs}')

# @receiver(got_request_exception)
# def at_req_exception(sender,request,**kwargs):
#         print('-------------------------------------------')
#         print('At Exception Request... Run Intro..')
#         print('sender:',sender)
#         print('request:',request)
#         print(f'kwargs: {kwargs}')

@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('----------------------------------------------------------------------')
    print('At migration start')
    print('sender:',sender)
    print('App_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('Using',using)
    print('Plan:',plan)
    print('Apps:',apps)
    print(f'Kwargs: {kwargs}')

@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('----------------------------------------------------------------------')
    print('At migrations End')
    print('sender:',sender)
    print('App_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('Using',using)
    print('Plan:',plan)
    print('Apps:',apps)
    print(f'Kwargs: {kwargs}')


@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print('----------------------------------------------------------------------')
    print('Initial connection to the databases.....')
    print('sender:',sender)
    print('connections:',connection)
    print(f'Kwargs: {kwargs}')
