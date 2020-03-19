import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

class logs:
    def __init__(self):
        cred = credentials.Certificate('covid19-assistant-firebase-adminsdk-pw5iz-4ead5a82ca.json')
        try:
            firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://covid19-assistant.firebaseio.com/'
        })
        except:
            print("already initialized")
        self.compare_date = str(datetime.date.today() - datetime.timedelta(days=14))
        self.medical_data = {}
        self.norm = {'a1':0, 'a2':0, 'a3':0, 'a4':0, 'b1':0, 'b2':0, 'b3':0}
        self.data_len = 1
        self.return_data = {}

    def filter_data(self, user_id):
        ref = db.reference("users/"  + user_id + "/log")
        data = ref.get()
        timestamps = data.keys()
        for time in timestamps:
            if(time>self.compare_date):
                self.medical_data[time] = data[time]

    def generate_score(self):
        # print(self.medical_data)
        for day in self.medical_data.keys():
            for symptom in self.medical_data[day].split(','):
                self.norm[symptom] += 1
        self.data_len = len(self.medical_data)

        #sum of all symtomps for each day/len(data)
        for symptom in self.norm.keys():
            self.norm[symptom] = self.norm[symptom] / self.data_len

        normalized_sum = 0

        for symptom in self.norm.keys():
            normalized_sum += self.norm[symptom]
        return normalized_sum/7    
                
    def get_report(self, user_id):
        self.filter_data(user_id)
        score = self.generate_score()

        self.return_data['length'] = self.data_len
        self.return_data['smp_log'] = self.medical_data
        self.return_data['score'] = score

        return self.return_data   


if __name__ == "__main__":
    f = logs()
    r = f.get_report("etEO6dckE3QrvSu6yEwvVqnPvIG")
    print(r)



    # "etEO6dckE3QrvSu6yEwvVqnPvIG3"