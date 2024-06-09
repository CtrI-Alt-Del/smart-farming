from os import getenv
from typing import Literal

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, MediaFileUpload

from core.commons import Error

from infra.constants import FOLDERS

GOOGLE_DRIVE_DATABASE_BACKUP_FOLDER_ID = getenv(
    "GOOGLE_DRIVE_DATABASE_BACKUP_FOLDER_ID"
)


class CloundStorageProvider:
    def __init__(self):
        try:
            scope = ["https://www.googleapis.com/auth/drive"]
            service_account_json_key = (
                f'{FOLDERS["certificates"]}/smart-farming-drive-service-account.json'
            )
            credentials = Credentials.from_service_account_file(
                filename=service_account_json_key, scopes=scope
            )

            self.google_drive = build("drive", "v3", credentials=credentials)
        except Exception as exception:
            raise Error(exception)

    def get_files(self):
        result = (
            self.google_drive.files()
            .list(
                pageSize=1000,
                fields="nextPageToken, files(id, name, mimeType, size, modifiedTime)",
                q='name contains "de"',
            )
            .execute()
        )

        files = result.get("files", [])

        return files

    def create_file(self, file_path: str, filename: str, mimetype: Literal["text/sql"]):
        file_metadata = {
            "name": filename,
            "parents": [GOOGLE_DRIVE_DATABASE_BACKUP_FOLDER_ID],
        }
        media = MediaFileUpload(file_path, mimetype=mimetype)

        self.google_drive.files().create(
            body=file_metadata, media_body=media, fields="id"
        ).execute()
