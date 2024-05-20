from math import ceil

from core.commons import Pagination,Date,Error

from core.entities import SensorsRecord,Plant

from infra.repositories import plants_repository, sensors_records_repository
from datetime import date


class GetSensorsRecordsTablePageData:
    def execute(self,start_date:str,end_date:str,plant_id:str, page_number: int = 1, should_get_plants: bool = False) -> tuple[list[SensorsRecord],int,list[Plant]]:
        try:
            plants = []
            if should_get_plants:
                plants = plants_repository.get_plants()
            filters = self.__handle_filters(plant_id=plant_id,start_date=start_date,end_date=end_date)

            sensors_count = sensors_records_repository.get_sensors_records_count()

            pagination = Pagination(page_number,sensors_count)


            current_page_number,last_page_number = (pagination.get_current_and_last_page_numbers())

            sensors_records = (sensors_records_repository.get_filtered_sensors_records(
                page_number=current_page_number,
                plant_id=filters["plant_id"],
                start_date=filters["start_date"],
                end_date=filters["end_date"] 
                )   
            )

            return {
                "sensors_records": sensors_records,
                "plants": plants,
                "last_page_number": last_page_number,
                "current_page_number": current_page_number,
            }
            
            
            
            
        except Error as error:
            return error
    def __handle_filters(
        self,
        start_date:str,
        end_date:str,
        plant_id:str
    ):
        if plant_id == "all":
            plant_id = None
        if start_date != "" and isinstance(start_date,str):
            start_date = Date(start_date).get_value()
        if end_date != "" and isinstance(end_date,str):
            end_date = Date(end_date).get_value()
        has_filters = plant_id is not None or (isinstance(start_date,date) and isinstance(end_date,date))
        
        return{
            "plant_id":plant_id,
            "start_date":start_date,
            "end_date":end_date
        }