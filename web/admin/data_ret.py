import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
class firebase:
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('covid19-assistant-firebase-adminsdk-pw5iz-4ead5a82ca.json')
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://covid19-assistant.firebaseio.com/'
        })
    def test(self):
        ref = db.reference('users')
        print(ref.get())


if __name__ == "__main__":
    f = firebase()
    f.test()