from flask import request

from core.use_cases.sensors_records import create_sensors_record_by_api
from core.commons import Error


def create_sensors_record_by_api_view():
    try:
        data = request.get_json()
        print(data,flush=True)
        create_sensors_record_by_api.execute(data)
        
        return "Chupa Sky Fly", 200 ##scary!!
    except Error as error:
        print(error.ui_message, flush=True)
        return error.ui_message, error.status_code
