from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = service_account.Credentials.from_service_account_file(
    'credentials.json', scopes=SCOPES
)

service = build('calendar', 'v3', credentials=credentials)

def create_calendar_event(data):
    event = {
        'summary': f"Delivery - {data.customer_name}",
        'location': data.delivery_address,
        'description': f"Items: {data.items}, Vehicle: {data.vehicle_type}",
        'start': {
            'dateTime': f"{data.delivery_date}T09:00:00",
            'timeZone': 'Asia/Kuala_Lumpur',
        },
        'end': {
            'dateTime': f"{data.delivery_date}T10:00:00",
            'timeZone': 'Asia/Kuala_Lumpur',
        },
    }

    service.events().insert(calendarId='primary', body=event).execute()