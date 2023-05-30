import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  
  getQuestionById(questionId) {
    return this.call("get", `questions/${questionId}`);
  },

  getQuestionByPosition(position) {
    return this.call("get", `/questions?position=${position}`);
  },

  submitParticipantAnswers(answers) {
    return this.call("post", "participations", answers);
  },
  
  login(password) {
    return this.call("post", "login", { password });
  },
  
  addQuestion(question) {
    return this.call("post", "questions", question);
  },
  
  rebuildDatabase() {
    return this.call("post", "rebuild-db");
  },
  
  submitParticipation(answers) {
    return this.call("post", "participations", answers);
  },
  
  updateQuestion(questionId, question) {
    return this.call("put", `questions/${questionId}`, question);
  },
  
  deleteQuestion(questionId) {
    return this.call("delete", `questions/${questionId}`);
  },
  
  deleteAllQuestions() {
    return this.call("delete", "questions/all");
  },
  
  deleteAllParticipations() {
    return this.call("delete", "participations/all");
  },
  

};
