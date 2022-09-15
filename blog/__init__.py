from blog import blog
def create_app():
    app = ...
    # existing code omitted

    
    app.register_blueprint(blog.bp)
    app.add_url_rule('/blog', endpoint='blog')

    return app