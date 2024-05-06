from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from g4f.Provider import (
    Bing,
    Aura,
    AItianhuSpace,
    AiChatOnline,
    ChatBase,
    ChatForAi,
ChatgptAi,
ChatgptNext,
Chatxyz,
GPTalk,
Gpt6,
Koala,
Liaobots,
OnlineGpt,
You,
Vercel,
Liaobots,
)
class ChatApp(App):

    def build(self):
        # Создаем главный макет
        layout = BoxLayout(orientation='vertical')

        # Создаем текстовое поле для ввода сообщений
        self.message_input = TextInput(hint_text='Введите вопрос здесь(РАБОТАЕТ ТОЛЬКО С VPN)', multiline=False)
        self.message_input.bind(on_text_validate=self.send_message)

        # Создаем метку для вывода ответов
        self.response_label = Label()

        # Добавляем виджеты в главный макет
        layout.add_widget(self.response_label)
        layout.add_widget(self.message_input)

        return layout

    def send_message(self, instance):
        message = self.message_input.text
        # Здесь должна быть логика отправки сообщения нейросети и получения ответа
        response = self.get_response_from_neural_network(message)
        self.response_label.text = f'Sasha: {response}'
        self.message_input.text = ''

    def get_response_from_neural_network(self, message):
        import g4f 
        response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "user", "content": message}],provider=Liaobots, stream=False)
        mes=response
        return mes

if __name__ == '__main__':
    ChatApp().run()
