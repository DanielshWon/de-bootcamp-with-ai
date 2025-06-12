def validate_file_extension(filename):
    """파일 확장자 검증"""
    allowed_extensions = ['.txt', '.csv', '.json', '.py']
    extension = filename[filename.rfind('.'):]
    return extension in allowed_extensions