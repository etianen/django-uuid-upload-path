"""
Generate short UUIDs and use them as paths
for uploaded media files in Django.

Developed by Dave Hall.

<http://www.etianen.com/>
"""


__version__ = (1, 0, 0)


from uuid_upload_path.uuid import uuid
from uuid_upload_path.storage import upload_to_factory, upload_to
