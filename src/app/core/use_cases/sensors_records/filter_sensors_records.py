from datetime import date

from infra.repositories import sensors_records_repository

from core.commons import Error

class FilterSensorsRecords:
    def execute(self,plant_id:str,start_date:date,end_date:date):
        if plant_id == "all":
            plant_id = None
        try:
            records = sensors_records_repository.get_filtered_sensors_records(
                page_number=1,
                start_date=start_date,
                end_date=end_date,
                plant_id=plant_id
            )
            
            return records
        except Error as error:
            raise error