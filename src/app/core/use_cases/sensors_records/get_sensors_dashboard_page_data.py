from core.commons import LineChart, Error

from infra.repositories import sensors_records_repository, plants_repository


class GetSensorDashboardPageData:
    def execute(self):
        plants = plants_repository.get_plants()

        if len(plants) == 0:
            raise Error("Nenhuma planta encontrada", status_code=404)

        sensors_records = (
            sensors_records_repository.get_sensor_records_grouped_by_date()
        )

        if len(sensors_records) == 0:
            raise Error("Nenhum registro dos sensores encontrado", status_code=404)

        soil_humidity_chart = LineChart(sensors_records, "soil_humidity")
        ambient_humidity_chart = LineChart(sensors_records, "ambient_humidity")
        temperature_chart = LineChart(sensors_records, "temperature")
        water_volume_chart = LineChart(sensors_records, "water_volume")

        return {
            "soil_humidity_chart_data": soil_humidity_chart.get_data(plants),
            "ambient_humidity_chart_data": ambient_humidity_chart.get_data(plants),
            "temperature_chart_data": temperature_chart.get_data(plants),
            "water_volume_chart_data": water_volume_chart.get_data(plants),
            "plants": plants,
        }
