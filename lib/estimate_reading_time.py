def estimate_reading_time(text):
    reading_time = 200
    if text == "":
        return 0
    return len(text.split(" ")) / reading_time