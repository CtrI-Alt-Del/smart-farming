from core.commons import LineChart, OrderedPlants
from core.errors.plants import PlantNotFoundError
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    UsersRepositoryInterface,
    SensorRecordsRepositoryInterface,
)
from core.constants import ADMIN_USER_EMAIL


class GetSensorsRecordsDashboardPageData:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        users_repository: UsersRepositoryInterface,
        sensors_records_repository: SensorRecordsRepositoryInterface,
    ):
        self._plants_repository = plants_repository
        self._users_repository = users_repository
        self._sensors_records_repository = sensors_records_repository

    def execute(self):
        plants = self._plants_repository.get_plants()

        if len(plants) == 0:
            raise PlantNotFoundError("Nenhuma planta encontrada")

        active_plant_id = self._users_repository.get_user_active_plant_id(
            ADMIN_USER_EMAIL
        )

        ordered_plants = OrderedPlants(plants, active_plant_id)

        records = self._sensors_records_repository.get_sensor_records_for_line_charts()

        if len(records) == 0:
            raise SensorsRecordNotFoundError(
                ui_message="Nenhum registro dos sensores encontrado"
            )

        soil_humidity_chart = LineChart(records["soil_humidity_line_chart_records"])
        ambient_humidity_chart = LineChart(
            records["ambient_humidity_line_chart_records"]
        )
        temperature_chart = LineChart(records["temperature_line_chart_records"])
        water_volume_chart = LineChart(records["water_volume_line_chart_records"])

        plants = ordered_plants.get_value()

        return {
            "soil_humidity_chart_data": soil_humidity_chart.get_data(plants),
            "ambient_humidity_chart_data": ambient_humidity_chart.get_data(plants),
            "temperature_chart_data": temperature_chart.get_data(plants),
            "water_volume_chart_data": water_volume_chart.get_data(plants),
            "plants": plants,
            "active_plant_id": active_plant_id,
        }
