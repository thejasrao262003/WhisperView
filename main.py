from distance_new import *
from test import *
from speechtotext import *
from OCR import *

def say(text):
    os.system(f"say {text}")
def chat(prompt):
    global chat_response
    openai.api_key = "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"
    chat_response = f'If I told you this """{prompt}""" How will you answer?'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chat_response,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        say(response['choices'][0]['text'])
        return response['choices'][0]['text']

    except Exception as e:
        return "There has occurred some error..."
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Debug: print available Microphones
        print("Available Microphones:", sr.Microphone.list_microphone_names())

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    return text

def say(text):
    os.system(f"say {text}")


def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for prompt: {prompt}\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        print(response['choices'][0]["text"])
        say(response['choices'][0]["text"])
    except Exception as e:
        return "There has occurred some error..."

    #return response['choices'][0]["text"]

while True:
    text = recognize_speech()
    if "surroundings" in text:
        fun1()
        key = cv2.waitKey(1) & 0xFF
        if key==ord("q"):
            break

    elif "read" in text:
        fun4()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    elif "familiar" in text:
        face_detection()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    else:
        print("Chatting...")
        ai(text)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
