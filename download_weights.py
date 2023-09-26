import gdown

def download_file_from_google_drive(file_id, output_file):
    """
    Download a file from Google Drive.
    :param file_id: The Google Drive file ID.
    :param output_file: The name of the file to save.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_file, quiet=False)

# Example usage:
file_id = "1Wgh9dWT6SbakJhvuNkSaIa1ydFtkfUW6"
out = "average_model.pth"
download_file_from_google_drive(file_id,out)
