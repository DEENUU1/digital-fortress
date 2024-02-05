# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserAccount
# from subscription.models import Product, UserSubscription
# from subscription.repository.product import ProductRepository
# from subscription.repository.user_subscription import UserSubscriptionRepository
#
#
# @receiver(post_save, sender=UserAccount)
# def create_new_user_subscription(sender, instance, created, **kwargs):
#     if created:
#         # Check if product with name Free exists
#         product_repository = ProductRepository()
#         product = product_repository.get_by_name("Free")
#
#         if not product:
#             # Create product with name Free
#             product_data = {
#                 "name": "Free",
#                 "description": "Free subscription",
#                 "max_project_storage": 300,
#                 "num_of_projects": 3,
#             }
#             product = product_repository.create(product_data)
#
#         # Create user subscription
#         user_subscription_repository = UserSubscriptionRepository()
#         user_subscription_data = {
#             "user": instance,
#             "product": product,
#             "is_active": True,
#         }
#
#
#
# post_save.connect(create_new_user_subscription, sender=UserAccount)
