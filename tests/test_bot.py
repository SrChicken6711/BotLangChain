# Prueba de bot

from bot_engine import respond

print("Bot online")

rol : str = input("eres usuario o admin?").lower()
while True:
    
   message : str = input("Pregunta algo:")
    
   if message.lower() == 'salir':
       break        
        
   answer = respond(message, rol)
   print(f"Bot> {answer}\n")

#example = [
#    {
#        'type': 'text',
#        'text': '¡Hola! 😊 ¿Qué tal? ¿En qué te puedo ayudar hoy?',
#        'extras': {'signature': 'EokBCoYBAWkUfRPO9y3aUqRhUXKYwME9Lb0qL5T5po9c8hcFjv6dN8tqZ/h9HUFkLjXqzX7yv6e3KU2FislrgBXjYhSuMESSj1KXUstL2ZuW/2F4UxsZ7Hq2DTCD4ZcZHPRwov79wTAQbGEKOmtAjsCYKuDiAQ2fWtsDp6BQh7Y36NnrKetcuz2t1tA='}
#     }
#    ]