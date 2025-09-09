from config.env import env

CLICK_SERVICE_ID = env.str("CLICK_SERVICE_ID")
CLICK_MERCHANT_ID = env.str("CLICK_MERCHANT_ID")
CLICK_SECRET_KEY = env.str("CLICK_SECRET_KEY")
CLICK_ACCOUNT_MODEL = "core.apps.api.models.order.OrderModel"  # your order model path.
CLICK_AMOUNT_FIELD = "amount"  # your amount field that's belongs to your order model

CLICK_COMMISSION_PERCENT = 0
CLICK_DISABLE_ADMIN = True  # (optionally configuration if you want to disable change to True)
