from flask import send_file, after_this_request, request

from core.use_cases.checklist_records import get_checklist_records_csv_file

from infra.utils.file import File


def checklist_records_csv_file_view():
    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")

    csv_file = get_checklist_records_csv_file.execute(
        start_date=start_date, end_date=end_date, plant_id=plant_id
    )
    csv_folder = csv_file["folder"]
    csv_filename = csv_file["filename"]
    csv_path = f"{csv_folder}/{csv_filename}"

    @after_this_request
    def _(response):
        File(csv_file["folder"], csv_file["filename"]).delete()

        return response

    return send_file(csv_path, as_attachment=True)
