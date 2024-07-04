from flask import send_file, after_this_request, request

from infra.factories.use_cases.checklist_records import get_checklist_records_csv_file
from infra.utils.file import File
from infra.constants import FOLDERS


def checklist_records_csv_file_view():
    try:
        start_date = request.args.get("start-date", None)
        end_date = request.args.get("end-date", None)
        plant_id = request.args.get("plant", "all")

        csv_folder = FOLDERS["tmp"]

        csv_filename = get_checklist_records_csv_file.execute(
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            folder=csv_folder,
        )
        csv_path = f"{csv_folder}/{csv_filename}"

        @after_this_request
        def _(response):
            File(csv_folder, csv_filename).delete()

            return response

        return send_file(csv_path, as_attachment=True)
    except Exception as error:
        print(error, flush=True)
