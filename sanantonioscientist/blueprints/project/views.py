"""Houses the views for the demo Microservices architecture project"""

from flask import Blueprint, render_template


project = Blueprint(
    'project',
    __name__,
    template_folder='templates'
)


@project.route('/project')
def description():
    return render_template('project/description.html')
