from core.constants import LEAF_APPEARANCES, LEAF_COLORS

from infra.repositories import checklist_records_repository


class GetChecklistRecordsDashboardPageData:
    def execute(self):
        records = (
            checklist_records_repository.get_ordered_by_date_leaf_appearance_and_leaf_color_records()
        )

        date = records[0]["date"]
        is_repeated_date = False

        leaf_appearances_records_days_count = {
            leaf_apearance: 0 for leaf_apearance in LEAF_APPEARANCES
        }

        leaf_colors_records_days_count = {leaf_color: 0 for leaf_color in LEAF_COLORS}

        for leaf_appearance in LEAF_APPEARANCES:
            if leaf_appearance != "MURCHA":
                continue

            for record in records:
                print(
                    "record",
                    record["date"],
                    record["leaf_appearance"],
                    flush=True,
                    end="",
                )
                print("date", date, flush=True)
                if not (
                    record["leaf_appearance"] == leaf_appearance
                    and record["date"] == date
                    and not is_repeated_date
                ):
                    date = record["date"]
                    is_repeated_date = False
                else:
                    leaf_appearances_records_days_count[leaf_appearance] += 1
                    is_repeated_date = True

        return {
            "leaf_appearances_records_days_count": leaf_appearances_records_days_count,
            "leaf_colors_records_days_count": leaf_colors_records_days_count,
        }
