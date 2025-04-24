def find_answer(user_input, kb):
    for category in kb:
        for key in kb[category]:
            if key in user_input:
                return kb[category][key]
    return "Hmm... Ziggy doesn't know that yet. Ask HR maybe? 😉"
