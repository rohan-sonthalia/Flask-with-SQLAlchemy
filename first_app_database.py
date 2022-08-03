from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video (Name = {self.name}, Views = {self.views}, Likes = {self.likes})"

parser = reqparse.RequestParser()

parser.add_argument("name", type= str, location="form", help= "Enter Name of the video")
parser.add_argument("views", type= int, location="form", help= "Enter Views of the video")
parser.add_argument("likes", type= int, location="form", help= "Enter Likes of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}

class Index(Resource):
    def get(self):
        return "Welcome to my API"

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id= video_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):        
        args = parser.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=['likes'])
        db.session.add(video)
        db.session.commit()
        return video

api.add_resource(Index, "/")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)