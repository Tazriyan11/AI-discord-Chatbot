from random import choice, randint

def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == ' ':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'yo' in lowered:
        return 'Yo! What\'s up?'
    elif 'what\'s popping' in lowered:
        return 'Not much, just chilling. How about you?'
    elif 'howdy' in lowered:
        return 'Howdy! What can I do for you today?'
    elif 'greetings' in lowered:
        return 'Greetings! How may I help you?'
    elif 'sup' in lowered:
        return 'Sup! How\'s it going?'
    elif 'how\'s life' in lowered:
        return 'Life\'s good! How about yours?'
    elif 'long time no see' in lowered:
        return 'Indeed! How have you been?'
    elif 'nice to meet you' in lowered:
        return 'Likewise! What can I assist you with?'
    elif 'pleased to meet you' in lowered:
        return 'Pleasure is all mine! How can I help you?'
    elif 'how\'s everything' in lowered:
        return 'Everything\'s going well! How about you?'
    elif 'how\'s your day' in lowered:
        return 'It\'s been good so far, thank you for asking! How about yours?'
    elif 'what is the meaning of life' in lowered:
        return ('The meaning of life is a deeply philosophical question with no single answer. '
                'Some people find meaning in relationships, others in personal achievements or '
                'spiritual beliefs. What do you think gives life meaning?')
    elif 'how do we know what is right and wrong' in lowered:
        return ('Determining what is right and wrong is a fundamental question in ethics. '
                'It\'s influenced by cultural norms, personal values, and philosophical principles.'
                'Your approach to ethical decision-making?')
    elif 'what happens after we die' in lowered:
        return ('The answer to that question depends on one\'sbeliefs and cultural background.'
                'Some believe in an afterlife, others in reincarnation, and some think it\'s '
                'simply the end of consciousness. What are your thoughts on this?')
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that'])



