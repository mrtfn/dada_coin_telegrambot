from SafeTrade.database.MongoDB.database import saveContactMessage
from SafeTrade import bot
from SafeTrade.helpers.start_constants import CONTACT_US_REPLAY


@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    if message.text == "CONTACT_US_BUTTON":
        # Extract the user's message
        user_message = message.text
        
        # Call your database function to save the user ID and message content
        await saveContactMessage(message.from_user.id, user_message)
        
        # Send a confirmation message to the user
        await bot.send_message(message.chat.id, CONTACT_US_REPLAY)
