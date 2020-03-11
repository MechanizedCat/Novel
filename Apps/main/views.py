from flask import Blueprint

main_blue = Blueprint(__name__, 'main_blue', template_folder='../templates', url_prefix='/s/')


@main_blue.route('/')
def Hello_world():
    return 'hello world'
