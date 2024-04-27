from core.commons import Error

from infra.repositories import sensors_records_repository

class DeleteSensorsRecord:
    def execute(self,sensors_records_ids: list[str]) -> None:
        try:
            for id in sensors_records_ids:
                if id and isinstance(id,str):
                    has_sensors_record = bool(
                        sensors_records_repository.get_sensors_record_by_id(id)
                    )
                    
                    if not has_sensors_record:
                        raise Error(
                            ui_message="Registro dos sensors não encontrado",
                            internal_message="Sensors record not found",
                        )
                    sensors_records_repository.delete_sensors_record_by_id(id)
        except Error as error:
            raise error