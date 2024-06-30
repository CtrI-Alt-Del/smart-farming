from .create_plant_by_form_factory import CreatePlantByFormFactory
from .delete_plant_factory import DeletePlantFactory
from .filter_plants_factory import FilterPlantsFactory
from .get_plant_by_id_factory import GetPlantByIdFactory
from .get_plants_page_data_factory import GetPlantsPageDataFactory
from .update_plant_factory import UpdatePlantFactory

create_plant_by_form = CreatePlantByFormFactory.produce()
delete_plant = DeletePlantFactory.produce()
filter_plants = FilterPlantsFactory.produce()
get_plant_by_id = GetPlantByIdFactory.produce()
get_plants_page_data = GetPlantsPageDataFactory.produce()
update_plant = UpdatePlantFactory.produce()
