
from django.conf import settings
import stripe
from django.contrib.auth.signals import user_logged_in
from .models import UserStripe, EmailConfirmed
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

stripe.api_key = settings.STRIPE_SECRET_KEY
User = get_user_model()
# def get_or_create_stripe(sender, user, *args, **kwargs):
# 	# print(sender)
# 	# print(user)
# 	print('something')
# 	try:
# 		print('sk1')
# 		user.userstripe.stripe_id
# 	except UserStripe.DoesNotExist:
# 		print('sk2')
# 		customer = stripe.Customer.create(
# 		email = str(user.email)
# 			)
# 		new_user_stripe = UserStripe.objects.create(user = user,
# 				stripe_id = customer.id
# 			)
# 	except:
# 		print('sk3')
# 		pass
# user_logged_in.connect(get_or_create_stripe)
def get_Create_userstripe(user):
	new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
	if created:
		customer = stripe.Customer.create(
		email = str(user.email)
			)
		print('created ',customer.id)
		new_user_stripe.stripe_id = customer.id
		new_user_stripe.save()
def user_created(sender, instance, created, *args, **kwargs):
	user = instance
	if created:
		get_Create_userstripe(user)
		email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
		if email_is_created:
			# create hash
			# send email
			pass


post_save.connect(user_created, sender=User)