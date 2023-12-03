from flask import Flask, request, send_file, jsonify
from bing_image_downloader import downloader
import os
import shutil

app = Flask(__name__)

@app.route('/download_images/<query>/<int:num_images>', methods=['GET'])
def download_images(query, num_images):
    output_path = f'downloads/'
    downloader.download(query, limit=num_images, output_dir=output_path, adult_filter_off=True, force_replace=False)
    
    zip_filename = f'{query}_images.zip'
    shutil.make_archive(zip_filename[:-4], 'zip', output_path)
    
    response_message = f'Successfully downloaded {num_images} images for query: {query}'
    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
