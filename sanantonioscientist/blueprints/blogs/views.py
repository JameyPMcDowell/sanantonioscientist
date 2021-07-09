from flask import Blueprint, render_template


blogs = Blueprint(
    'blogs',
    __name__,
    template_folder='templates'
)


@blogs.route('/why_microservices')
def microservice_intro():
    return render_template('blogs/why_microservices.html')

@blogs.route('/docker_intro')
def docker_intro():
    return render_template('blogs/docker_intro.html')

@blogs.route('/preprocessing_microservice_with_R')
def preprocessing_microservice_with_r():
    return render_template('blogs/preprocessing_microservice_with_R.html')