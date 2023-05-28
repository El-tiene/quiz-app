from classQuestion import *
import sqlite3
from flask import jsonify
import datetime
from datetime import datetime

import json


def deserialize_question(data):
    
    tab=[]
    for reponse in data['possibleAnswers']:
            dictio = {
                'text': str(reponse['text']),
                'isCorrect': bool(reponse['isCorrect'])
            }
            tab.append(dictio)
    
    return Question(
        None,
        title=data['title'],
        text=data['text'],
        image=data['image'],
        position=data['position'],
        possible_answers=tab
    )

def convert_to_json(question):
    data = {
        'id': question.id,
        'text': question.text,
        'position': question.position,
        'title': question.title,
        'image': question.image,
        'possibleAnswers': question.possible_answers
    }
    return data


def createQuestion(request):
    jsonObject = request.get_json()
    question= deserialize_question(jsonObject)

    try:
        conn = sqlite3.connect('MyDataBase.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(*) FROM QUESTION WHERE position = {question.position}")
        count = cursor.fetchone()[0]

        if count>0:
            cursor.execute(f"UPDATE QUESTION SET position = position + 1 WHERE position >= {question.position}")
            cursor.execute(f"UPDATE possibleAnswers SET positionquestion = positionquestion + 1 WHERE positionquestion >= {question.position}")

        cursor.execute("INSERT INTO question (title, text, image, position) VALUES (?, ?, ?, ?)",
                                    (question.title, question.text, question.image, question.position))
        
        
        question_id = cursor.lastrowid  # Récupération de l'identifiant de la question créée
        conn.commit()

        
        # insertion des réponses possibles
        for reponse in question.possible_answers:
            cursor.execute(
                "INSERT INTO possibleAnswers (text, isCorrect, positionquestion) VALUES (?, ?, ?)",
                (reponse['text'], str(reponse['isCorrect']), question.position)
            )
        conn.commit()
        conn.close()
        return jsonify({'id': question_id}), 200  # Retourne l'identifiant de la question
        
    except sqlite3.Error as e:
        print("Erreur",e)
        return "erreur"


def get_Quizz_Info():
    try:
        conn = sqlite3.connect('MyDataBase.db')
        cursor = conn.cursor()

        # Récupérer le nombre de questions
        cursor.execute("SELECT COUNT(*) FROM Question")
        size = cursor.fetchone()[0]

        # Récupérer les scores passés
        cursor.execute("SELECT playerName, score, date FROM participationResult ORDER BY score DESC")
        scores = cursor.fetchall()

        # Formatter les dates au format dd/MM/yyyy hh:mm:ss
        scores = [
            {
                'playerName': score[0],
                'score': score[1],
                #'date': datetime.strptime(score[2], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
            }
            for score in scores
        ]

        conn.close()

        # Créer le payload de retour
        payload = {
            'size': size,
            'scores': scores
        }

        return payload, 200

    except sqlite3.Error as e:
        print("Erreur lors de la récupération des informations du quiz :", e)
        return json.dumps({'error': 'An error occurred while retrieving quiz information'}), 500
    

def rebuildBDrebuildBD():
    try:
        with sqlite3.connect('MyDataBase.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM question")
            cursor.execute("DELETE FROM participationResult")
            cursor.execute("DELETE FROM sqlite_sequence")
            cursor.execute("DELETE FROM possibleAnswers")

            conn.commit()

            return 'Ok',200
    except sqlite3.Error as e:
        print("Erreur :", e)
        return 'An error occurred while getting deleting all infos', 500

def getQuestionById(request, questionId):
    try:
        with sqlite3.connect('MyDataBase.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM question WHERE id = {questionId}")
            question_data = cursor.fetchone()

            if question_data is None:
                return 'Question not found', 404

            question = Question(
                id=question_data[0],
                title=question_data[1],
                text=question_data[3],
                image=question_data[4],
                position=question_data[2],
                possible_answers=[]
            )
            

            cursor.execute(f"SELECT * FROM possibleAnswers WHERE positionquestion = {question.position}")
            possible_answers_data = cursor.fetchall()

            for answer_data in possible_answers_data:
                answer = {
                    'text': answer_data[1],
                    'isCorrect': bool(answer_data[2] == 'True')
                }
                question.possible_answers.append(answer)

            question_json = convert_to_json(question)

            return question_json, 200
    except sqlite3.Error as e:
        print("An error occurred while retrieving the question from the database:", e)
        return 'Internal Server Error', 500
    
def getQuestionByPosition(position):
    try:
        with sqlite3.connect('MyDataBase.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM question WHERE position = {position}")
            question_data = cursor.fetchone()

            if question_data is None:
                return 'Question not found', 404

            question = Question(
                id=question_data[0],
                title=question_data[1],
                text=question_data[3],
                image=question_data[4],
                position=question_data[2],
                possible_answers=[]
            )
            

            cursor.execute(f"SELECT * FROM possibleAnswers WHERE positionquestion = {question.position}")
            possible_answers_data = cursor.fetchall()

            for answer_data in possible_answers_data:
                answer = {
                    'text': answer_data[1],
                    'isCorrect': bool(answer_data[2] == 'True')
                }
                question.possible_answers.append(answer)

            question_json = convert_to_json(question)
            
            return question_json, 200
    except sqlite3.Error as e:
        print("An error occurred while retrieving the question from the database:", e)
        return 'Internal Server Error', 500
    

from flask import request, jsonify
import sqlite3


def submit_participant_answers(request):
    # Récupérer les données de la requête
    jsonObject= request.get_json()
    player_name = jsonObject['playerName']
    userAnswers = request.json.get('answers')


    try:
        # Se connecter à la base de données
        conn = sqlite3.connect('MyDataBase.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

         # Obtenir les questions du quiz dans l'ordre
        cursor.execute("SELECT * FROM question ORDER BY position")
        quiz_questions = cursor.fetchall()

        # Vérifier si le nombre de réponses correspond au nombre de questions
        if len(userAnswers) != len(quiz_questions):
            return 'Invalid number of answers', 400

        score=0
        for indexUserAnswer in range(0,10):
            
            cursor.execute(f"SELECT * FROM possibleAnswers WHERE positionquestion = {indexUserAnswer+1}")
            possibleAnswers = cursor.fetchall()
            
            userAnswer=userAnswers[indexUserAnswer]
            for relativeIndex, answer in enumerate(possibleAnswers,start=1):
                if(userAnswer==relativeIndex):
                    bool=answer['isCorrect']
                    if(answer['isCorrect']=='True'):
                        score+=1

        # Insérer le résultat de la participation dans la base de données
        cursor.execute("INSERT INTO participationResult (playerName, score) VALUES (?, ?)",
                       (player_name, score))
        conn.commit()

        # Préparer la réponse
        response_data = {
            'playerName': player_name,
            'score': score
        }

        return jsonify(response_data), 200

    except sqlite3.Error as e:
        print("An error occurred while submitting participant's answers:", e)
        return 'Internal Server Error', 500

    finally:
        if conn:
            conn.close()

def delete_question(questionId):
    try:
        # Supprimer la question de la base de données
        conn = sqlite3.connect('MyDataBase.db')
        cursor = conn.cursor()

        # Vérifier si la question existe
        cursor.execute("SELECT COUNT(*) FROM question WHERE id = ?", (questionId,))
        count = cursor.fetchone()[0]
        if count == 0:
            return '', 404  # Question non trouvée, retourner 404 - Not Found
        
        cursor.execute("SELECT position FROM QUESTION WHERE id = ?", (questionId,))
        position = cursor.fetchone()[0]

        # Supprimer la question
        cursor.execute("DELETE FROM question WHERE id = ?", (questionId,))
        cursor.execute("DELETE FROM possibleAnswers WHERE positionQuestion = ?", (position,))

        cursor.execute(f"UPDATE QUESTION SET position = position - 1 WHERE position > {position} ")
        cursor.execute(f"UPDATE possibleAnswers SET positionquestion = positionquestion - 1 WHERE positionquestion > {position}")

        conn.commit()
        conn.close()

        return '', 204  # Suppression réussie, retourner 204 - No Content

    except sqlite3.Error as e:
        print("Erreur lors de la suppression de la question :", e)
        return '', 500  # Erreur de serveur, retourner 500 - Internal Server Error




def delete_questions():
    try:
        # Supprimer toutes les questions et leurs réponses de la base de données
        conn = sqlite3.connect('MyDataBase.db')
        cursor = conn.cursor()

        # Supprimer les réponses des questions
        cursor.execute("DELETE FROM possibleAnswers")
        
        # Supprimer les questions
        cursor.execute("DELETE FROM question")
        
        conn.commit()
        conn.close()

        return '', 204  # Suppression réussie, retourner 204 - No Content

    except sqlite3.Error as e:
        print("Erreur lors de la suppression des questions :", e)
        return '', 500  # Erreur de serveur, retourner 500 - Internal Server Error





def delete_all_participations():
    try:
        # Supprimer toutes les participations de la base de données
        conn = sqlite3.connect('MyDataBase.db')
        cursor = conn.cursor()

        # Supprimer toutes les participations
        cursor.execute("DELETE FROM participationResult")
        
        conn.commit()
        conn.close()

        return '', 204  # Suppression réussie, retourner 204 - No Content

    except sqlite3.Error as e:
        print("Erreur lors de la suppression des participations :", e)
        return '', 500  # Erreur de serveur, retourner 500 - Internal Server Error


def update_question(questionId):    
    jsonObject = request.get_json()
    question= deserialize_question(jsonObject)
        
    try:
        with sqlite3.connect('MyDataBase.db') as conn:
            cursor = conn.cursor()
            
            # Vérifier l'existence de la question
            cursor.execute("SELECT * FROM QUESTION WHERE id = ?", (questionId,))
            existing_question = cursor.fetchone()
            
            if existing_question is None:
                return 'Request respond Not Found', 404
            
            position_source = existing_question[2]
            position_destination = question.position

            if position_destination == position_source:
                # Mise à jour de la question à la même position
                update_query = "UPDATE QUESTION SET title = ?, text = ?, image = ?, position = ? WHERE id = ?"
                cursor.execute(update_query, (
                    question.title,
                    question.text,
                    question.image,
                    question.position,
                    questionId
                ))
                
               
                cursor.execute("DELETE FROM possibleAnswers WHERE positionquestion = ?", (position_source,))
                
                for answer in question.possible_answers:
                    cursor.execute(
                        "INSERT INTO possibleAnswers (text, isCorrect, positionquestion) VALUES (?, ?, ?)",
                        (answer['text'], str(answer['isCorrect']), position_source)
                    )

                return 'Question mise à jour', 204
            else:
                
                cursor.execute("DELETE FROM QUESTION WHERE position = ?", (position_source,))
                cursor.execute("DELETE FROM possibleAnswers WHERE positionquestion = ?", (position_source,))
                
                if position_source > position_destination:
                    cursor.execute("UPDATE QUESTION SET position = position + 1 WHERE position >= ? AND position < ?", (position_destination, position_source))
                    cursor.execute("UPDATE possibleAnswers SET positionquestion = positionquestion + 1 WHERE positionquestion >= ? AND positionquestion < ?", (position_destination, position_source))
                if position_source < position_destination:
                    cursor.execute("UPDATE QUESTION SET position = position - 1 WHERE position > ? AND position <= ?", (position_source, position_destination))
                    cursor.execute("UPDATE possibleAnswers SET positionquestion = positionquestion - 1 WHERE positionquestion > ? AND positionquestion <= ?", (position_source, position_destination))
                
                cursor.execute("INSERT INTO QUESTION (id, title, text, image, position) VALUES (?, ?, ?, ?, ?)",
                    (questionId, question.title, question.text, question.image, question.position)
                )

                for answer in question.possible_answers:
                    cursor.execute(
                        "INSERT INTO possibleAnswers (text, isCorrect, positionquestion) VALUES (?, ?, ?)",
                        (answer['text'], str(answer['isCorrect']), position_destination)
                    )
                
                conn.commit()
    
            return 'Question updated (other position)', 204
    except sqlite3.Error as e:
        print("Error occurred while updating question and answers by ID:", e)
        return 'An error occurred while updating the question', 500




