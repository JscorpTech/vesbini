import logging
from config.env import env

from core.apps.api.models.order import OrderModel
from core.apps.bot.bot import bot
from celery import shared_task


@shared_task
def notify_order(order_id):
    try:
        order = OrderModel.objects.get(pk=order_id)
    except OrderModel.DoesNotExist:
        logging.error("order not found")
        return
    channel_id = env.str("CHANNEL_ID")
    if channel_id is None:
        logging.error("channel_id is none")
        return
    message = f"""📩 Yangi buyurtma keldi!

📝 Buyurtma ma'lumotlari:    id: #{order.pk}

☕️Buyurtma qilingan mahsulotlar: 
"""
    for item in order.items.all():  # type: ignore
        message += f"""
    {item.name}
    📂 Kategoriya: {item.product.categories.name} 
    🔢 Miqdor: {item.count}"""
    message += f"""👤 Ism: {order.user.first_name} {order.user.last_name}
    📞 Telefon: {order.user.phone}
    📥  pochta/olib ketish: {"Ha" if order.is_delivery else "Yo'q"}"""
    with open(order.items.first().product.image.path, "rb") as file:  # type: ignore
        bot.send_photo(str(channel_id), file, caption=message)
