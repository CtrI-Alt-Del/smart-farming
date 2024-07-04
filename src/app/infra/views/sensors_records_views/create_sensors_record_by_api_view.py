from flask import request

from infra.factories.use_cases.sensors_records import create_sensors_record_by_api


def create_sensors_record_by_api_view():
    try:
        data = request.get_json()
        print(data, flush=True)
        create_sensors_record_by_api.execute(data)

        return "Chupa Sky Fly", 200  ##scary!!
    except Exception as error:
        return error.ui_message, error.status_code
