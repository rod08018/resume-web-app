import datetime
import oyaml as yaml
from flask import Flask
from flask import render_template
import settings
from models.models import BlogModel, Base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
app = Flask(__name__)
website_data = yaml.load(open('_config.yaml', encoding="utf-8"), Loader=yaml.FullLoader)


def get_connection():

    url = r"sqlite:///"+settings.file_path

    if not database_exists(url):
        create_database(url)
    con = create_engine(url).connect()

    return con
    
    
def insert(model):
    """This method insert the specified model into database
    Args:
        model (BaseModel): specified model 
    """
    con = get_connection()
    session = sessionmaker(bind=con, autocommit=False, autoflush=False)
    db = session()
    db.add(model)
    db.commit()
    

@app.route('/')
def index():

    return render_template('index.html', data=website_data)


@app.route('/blog')
def blog():
    url = r"sqlite:///" + settings.file_path
    con = create_engine(url)
    df = pd.read_sql_query("SELECT * from posts", con)
    print(df)
    posts = list(df.to_records(index=False))
    return render_template(r'blog.html', data=website_data, posts=posts)
    

if __name__ == '__main__':

    app.config['JSON_SORT_KEYS'] = False
    Base.metadata.create_all(get_connection())  # pragma: no cover
    url = r"sqlite:///" + settings.file_path
    if not database_exists(url):
        model = BlogModel(
            id='1',
            title='new post',
            body='this post was very fun',
            created=datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
            author_id=0,
            username='joserodriguez')
        create_database(url)
        insert(model)
    app.run(debug=True)
