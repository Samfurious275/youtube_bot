# save_session.py

from instagrapi import Client

def save_login_session():
    cl = Client()
    username = "samrider1232"
    password = "samridr123123"

    print("Logging in...")
    cl.login(username, password)  # First time login (may ask for code)

    print("Saving session...")
    cl.dump_settings("session.json")
    print("✅ Session saved to session.json")

if __name__ == "__main__":
    save_login_session()
