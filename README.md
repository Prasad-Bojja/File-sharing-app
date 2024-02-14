## File Sharing App

- This is a simple file sharing application built with Django and Django Rest Framework. It allows users to upload files, download files, and share them with others.

## Features

- File Upload: Users can upload files to the server.
- File Download: Users can download files shared by others, individually or in ZIP format.
- Folder Management: Files are organized into folders for better management.
- API Integration: Provides API endpoints for uploading and downloading files programmatically.

## Installation
- Clone the repository:

git clone https://github.com/Prasad-Bojja/File-sharing-app

## Navigate to the project directory:

- cd file-sharing-app

## Install dependencies:

- pip install -r requirements.txt

## Run migrations:
- python manage.py migrate


## Start the development server:
- python manage.py runserver

## Access the application 
- Consider adding a brief description of what users can expect to see when they access the application at http://localhost:8000.

## Usage
- File Upload: Navigate to the home page and use the file upload interface to select and upload files.
- File Download: Click on the download link to download files shared by others. You can also download multiple files in ZIP format by clicking the "Download Files" button.
- API Usage: Use the provided API endpoints for programmatically uploading and downloading files.
  
## API Endpoints
- File Upload: POST /handle/ - Upload files to the server.
- File Download: GET /download/<uid>/ - Download files individually using the unique identifier (UID) of the file. To download multiple files in ZIP format, use the /download/<uid>/ endpoint with the folder UID.
- It might be helpful to provide examples of how users can interact with the API endpoints, such as using cURL commands or tools like Postman

## Contributing
- Consider providing guidelines or expectations for contributions, such as coding standards, testing requirements, or how to submit bug reports and feature requests.
