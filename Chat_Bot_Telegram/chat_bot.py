#The variables annotated with final in the typing module indicate that they should not be reassigned or overridden.
from  typing import Final
from telegram  import Update
from telegram.ext import CallbackContext, CommandHandler, Application, MessageHandler, filters
import difflib
# THIS IS MY TOKEN, THE FATHERBOT GAVE ME THIS TOKEN PLEASE SEARSH FOR IT 
TOKEN : Final ='6731966379:AAFTMppaq-OYSpYyWOtjXn2pq4-fvv8c_II'
bot :Final='@yyyyassinbot'
#print(bot)
#command : chat_bot
async def start_cmd(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello and welcome to my bot_chat 😊")

async def help_cmd(update: Update, context: CallbackContext):
    await update.message.reply_text("How can I help you today?")

async def custom_cmd(update: Update, context: CallbackContext):
    await update.message.reply_text("This is a custom command")

def reponse(text : str) -> str :
    quetion = text.lower()
    if "hello" in quetion or "hi" in quetion:
        return ("Hi bro")
    elif "how are you" in quetion :
            return ("Pretty good and you")
    elif "i'm good" in quetion or "i'm fine" in quetion :
            return ("How can i help you?")
    elif "what is mean python" in quetion :
             return "Python is a high-level, interpreted programming language known for its simplicity and readability."
    elif "give me examples" in quetion or difflib.get_close_matches("give me examples", [quetion]):
             return "the code is\nimport random\nnum = random.randint(1, 10)\nif(num == 10) :\nprint('Yassin')\nThis is a simple example"
    else:
            return("Sorry, I don't know what you want ? Please explain me Again.")
        
# use the type_massage('group' or 'previte') and use the input from user
                
async def users_message(update: Update, context: CallbackContext):
    type_message: str = update.message.chat.type
    text_user : str = update.message.text
    #print the id and type message and message the user

    print(f"Users_id :{update.message.chat.id} in {type_message} = '{text_user}'")
    # handele the reoponse

    if(type_message == 'group'):
         if(bot in text_user):
            new_text:str = text_user.replace(bot,'').strip()
            reponse_users :str = reponse(new_text)
         else :
              return
    else :
        reponse_users :str = reponse(text_user)
    
    print('Bot :',reponse_users )
    await update.message.reply_text(reponse_users )




if __name__ == "__main__":
    print("START THE MY CHAT_BOT PROGRAM :)")

    dp = Application.builder().token(TOKEN).build()
    # commond
    dp.add_handler(CommandHandler("start", start_cmd))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(CommandHandler("custom", custom_cmd))
    #message
    dp.add_handler(MessageHandler(filters.TEXT , users_message))

    print("Polling...")
    dp.run_polling(poll_interval=5) 