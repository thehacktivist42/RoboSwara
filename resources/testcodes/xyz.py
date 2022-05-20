def voiceSearch():
    while True:
        try:
            with sr.Microphone as src:
                r.adjust_for_ambient_noise(src, duration = 0.5)
                aud = r.listen(src)
                global txt
                txt = r.recognizer_google(aud)
                txt = txt.lower()
                return txt
            break
        except:
            print("Not recognized. Restarting.")
            time.sleep(2)
            continue
