addcntr = []


@bot.message_handler(commands=['addcounter', 'Addcounter'])
def addc_message(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, ADDCOUNTER_NEA_MSG.encode("utf-8"), parse_mode="Markdown")
    return
  if (message.text.split()[1] == "add"):
    if userid in addcntr:
      return
    bot.send_message(message.chat.id, "Send your message now!")
    addcntr.append(userid)
  else:
    bot.reply_to(message, ADDCOUNTER_NEA_MSG.encode("utf-8"), parse_mode="Markdown")
    return
  
