import telebot
import pyowm
owm=pyowm.OWM('399fff2a85811608c3de584ecda87438',language='UA')
bot=telebot.TeleBot('1069702658:AAGehKe3es6yvYZmsHdg9EQTUs1pqpTW_eI')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привіт')
@bot.message_handler(content_types=['text'])

def start_text(message):
    try:
        observation = owm.weather_at_place(message.text)
        w=observation.get_weather()
        temp=w.get_temperature(unit='celsius')
        answer = f"В місті {message.text} зараз {w.get_detailed_status()} \n"
        answer+=f"Температура зараз :  { temp['temp'] } °C \n"
        answer+=f"Мінімальна температура :  { temp['temp_min'] } °C \n"
        answer+=f"Максимальна температура  :  { temp['temp_max'] } °C \n"
        answer+=f"Швидкість вітру: {w.get_wind()['speed']} \n"
        answer+=f"Вологість: {w.get_humidity()}  \n"
        answer+=f"Хмарність: {w.get_clouds()  }  % \n  "
        bot.send_message(message.chat.id, answer)
        # answer+=w.get_weather_icon_url()
        i = 'дощ';n= 'злива';j='сонце';l='чисте небо';k='хмарно';m='похмуро'
        if i  in w.get_detailed_status():
            bot.send_photo(message.chat.id,open('D:\ПогодаБот\p2.png' ,'rb'))
        if n in w.get_detailed_status():
            bot.send_photo(message.chat.id,open('D:\ПогодаБот\p2.png' ,'rb'))
        if j in w.get_detailed_status():
            bot.send_photo(message.chat.id,open('D:\ПогодаБот\p4.png' ,'rb'))
        if l in w.get_detailed_status():
            bot.send_photo(message.chat.id,open('D:\ПогодаБот\p4.png' ,'rb'))
        if m in w.get_detailed_status():
            bot.send_photo(message.chat.id,open('D:\ПогодаБот\p5.png' ,'rb'))
        if k in w.get_detailed_status():
            bot.send_photo(message.chat.id, open('D:\ПогодаБот\p5.png','rb'))

    except pyowm.exceptions.api_response_error.NotFoundError:
      bot.send_message(message.chat.id, 'Місто не знайдено. Спробуйте ще раз.')

if __name__ == '__main__':
    bot.polling(none_stop = True)
