import uuid


def instance_file_directory_path(instance, filename):
    return f'{instance._meta.model_name}/{uuid.uuid4()}/{filename}'
