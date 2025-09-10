from config.env import env

PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")
PAYME_ACCOUNT_FIELD = "id"
PAYME_ACCOUNT_MODEL = "core.apps.api.models.order.OrderModel"
PAYME_AMOUNT_FIELD = "amount"
PAYME_ONE_TIME_PAYMENT = True

PAYME_DISABLE_ADMIN = False
