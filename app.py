import re 
import uuid 
from Logger import Logging
from flask import Flask, render_template, request , send_file
from flask_cors import cross_origin

logger_obj = Logging('Advance Image Downloader')
logger_obj.initialize_logger()

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    """
    Function is responsible for showing the home page
    """
    try:
        if request.method == 'GET':
            logger_obj.print_log('Inside the home function', 'info')
            logger_obj.print_log('Rendering the index.html template', 'info')
            return render_template('index.html')
        else:
            logger_obj.print_log('(app.py) - Something went wrong Method not allowed', 'exception')
            return render_template('error.html', msg='Method not allowed')
    except Exception as e:
        logger_obj.print_log('(app.py) - Something went wrong ' + str(e), 'exception')
        return render_template('error.html', msg=str(e))
    
@app.route('/job_submitted', methods=['POST'])
@cross_origin()
def job_submitted():
    """
    The function is responsible for performing the various actions after the job is submitted by the user
    """
    try:
        if request.method == 'POST':
            logger_obj.print_log('Inside the job_submitted function', 'info')

            # Handling the user input
            search_query = request.form['search-query'].lower()
            date = request.form['date']
            time = request.form['time']
            email = request.form['email'].lower()
            no_images = request.form['images']

            return render_template('job_submitted.html')
        else:
            logger_obj.print_log('(app.py) - Something went wrong ')
            return render_template('error.html' )

    except ValueError:
        logger_obj.print_log('(app.py) - Something went wrong. No of images must be a number', 'exception')
        return render_template('error.html', msg='No of images must be a number')

    except Exception as e:
        logger_obj.print_log('(app.py) - Something went wrong ' + str(e), 'exception')
        return render_template('error.html', msg=str(e))
    
@app.route('/download/<search_term>/<uuid:req_id>', methods=['GET'])
@cross_origin()
def download(search_term, req_id):
    """
    Function is responsible for sending the zip file to the user
    :param search_term: Search query of the user
    :param req_id: Unique request ID of the user
    :return: Zip file created
    """
    try:
        logger_obj.print_log('Inside the download route', 'info')
        str_req_id = str(req_id)

        # Sending the downloadable file to the user
        return send_file(str_req_id + '_zipfile.zip', as_attachment=True, attachment_filename=search_term + '.zip')

    except Exception as e:
        logger_obj.print_log('(app.py) - Something went wrong ' + str(e), 'exception')
        return render_template('error.html', msg='This link has expired')  
    
if __name__ == Flask("__main__"):
    app.debug = True
    app.run()