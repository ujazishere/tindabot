from root_tinder import tindabot

swipes_desired = 400          #try keep it under 1500


bot = tindabot(swipes_desired)

bot.log_in()

bot.perform_swipes()

bot.send_new_message_to_new_matches()

bot.derive_replied_and_non_replied_ones()

