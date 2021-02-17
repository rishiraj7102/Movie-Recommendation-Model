from flask import Flask,request,jsonify
import util,movie_recommender_starter
app=Flask(__name__)

@app.route('/get_movie_names',methods=['GET'])
def get_movie_names():
    response=jsonify({
        'Movie_Names':util.get_movie_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/get_recommendations',methods=['GET','POST'])
def get_recommendations():
    user_movie=str(request.form['user_movie'])
    response=jsonify({
        'Recommended_Movies':movie_recommender_starter.recommend_movies(user_movie)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=='__main__':
    util.load_movies()
    app.run()