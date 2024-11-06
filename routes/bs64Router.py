from flask import Blueprint, render_template, request
from mt.generate64 import generateConvert
from encript.encript import service_encript

bs64Route = Blueprint('encript', __name__)

@bs64Route.route('/encript', methods=['GET', 'POST'])
def encript():
  
    result_base64 = None
    result_https = None
    
    if request.method == 'POST':
       
        input_text = request.form.get('inputText', '')

        
        if input_text.strip():
    
            result_base64 = generateConvert(input_text)
        
            result_https = "hola"
            result_https= service_encript(result_base64)
    

    return render_template('encript.html', result_base64=result_base64, result_https=result_https)
