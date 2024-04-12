from flask import render_template

from infra.repositories.sensors_records_repository import SensorRecordsRepository

sensors_records_repo = SensorRecordsRepository()

def last_sensors_record_page_view():
    
    last_data_and_date = sensors_records_repo.get_last_date()
    
    if last_data_and_date:
        last_date,sensors_records = last_data_and_date
        return render_template(
            "pages/last_sensors_record/index.html",datetime=last_date,sensors_records=sensors_records
        )
    else:
        return "No data found",404
