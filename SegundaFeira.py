from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from googletrans import Translator


class TradutorApp(App):
    def build(self):
        self.translator = Translator()
        layout = BoxLayout(orientation='vertical')

        self.label_input = Label(text='Texto a ser traduzido:', size_hint_y=None, height=30)
        layout.add_widget(self.label_input)

        self.input_text = TextInput(hint_text='Digite aqui...', multiline=False)
        layout.add_widget(self.input_text)

        self.btn_translate = Button(text='Traduzir', on_press=self.traduzir)
        layout.add_widget(self.btn_translate)

        self.output_label = Label(text='', size_hint_y=None, height=30)
        layout.add_widget(self.output_label)

        return layout

    def traduzir(self, instance):
        texto_input = self.input_text.text.strip()
        if texto_input:
            traducao = self.translator.translate(texto_input, src='pt', dest='en')
            self.output_label.text = f'Tradução: {traducao.text}'
        else:
            self.output_label.text = 'Por favor, insira um texto para tradução.'


if __name__ == '__main__':
    TradutorApp().run()

