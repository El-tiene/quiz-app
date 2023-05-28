from flask import Flask
from flask_cors import CORS
from flask import Flask, request
import hashlib
from jwt_utils import decode_token, build_token
from questions import *
from generateDataBase import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello le sang, {x}. Welcome !"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return get_Quizz_Info()

@app.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	tried_password=payload['password'].encode('UTF-8')
	hashed=hashlib.md5(tried_password).digest()

	if hashed==b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
		token=build_token()
		return {"token":token},200

	else:
		return 'Unauthorized', 401
	
@app.route('/questions',methods=['POST'])
def addQuestion():
	if(verifyAuth()):
		return createQuestion(request)
	else:
		return 'Unauthorized', 401
        
#EndPoint rebuild-bd
@app.route('/rebuild-db', methods=['POST'])
def rebuild_bd():
	if(verifyAuth()):
		return create_database_schema()
	else:
		return 'Unauthorized', 401
        

# Get question by id
@app.route('/questions/<questionId>', methods=['GET'])
def get_question_by_id(questionId):
    return getQuestionById(request, questionId)

# Get question by position
@app.route('/questions', methods=['GET'])
def get_question_by_position():
    position = request.args.get('position')
    return getQuestionByPosition( position)

# Submit player's quiz answers
@app.route('/participations', methods=['POST'])
def submit_participation():
    return submit_participant_answers(request)



#endpoints d'administration authentifiés

# Update one question
@app.route('/questions/<int:questionId>', methods=['PUT'])
def updateQuestion(questionId):
    if(verifyAuth()):
        return update_question(questionId)
    else:
        return 'Unauthorized', 401


# Delete one question
@app.route('/questions/<int:questionId>', methods=['DELETE'])
def deleteQuestion(questionId):
    if(verifyAuth()):
        return delete_question(questionId)
    else:
        return 'Unauthorized', 401
    

# Delete all questions
@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    if(verifyAuth()):
        return delete_questions()
    else:
        return 'Unauthorized', 401

# Delete all participations
@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipations():
    if(verifyAuth()):
        return delete_all_participations()
    else:
        return 'Unauthorized', 401



def verifyAuth():
     token = request.headers.get('Authorization')
     if (token):
          try : 
               decode_token(token.replace("Bearer ", ""))
               return True
          except Exception as e:
               print(e)
               return False
     else:
          return False	

if __name__ == "__main__":
    app.run()