from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name = "chatbot/chat.html"
