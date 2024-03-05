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
        
        
        
        
# Define a function to handle incoming messages
async def message_handler(client, message):
    # Check if the message is a reply to the "Now send your message please." message
    if message.reply_to_message and message.reply_to_message.text == "Now send your message please.":
        # Get the user's message
        user_message = message.text
        # Save the user's message to the database
        await saveContactMessage(message.chat.id, user_message)
        # Send a confirmation message to the user
        await message.reply_text("Your message has been received. Thank you!")