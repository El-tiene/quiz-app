import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import CreatedQuestion from '../views/CreatedQuestion.vue'
import AdminPage from '../views/AdminPage.vue'
import ScorePage from '../views/ScorePage.vue'
import QuestionPage from '../views/QuestionPage.vue'
import QuestionList from '../views/QuestionList.vue'
import QuestionEdit from '../views/QuestionEdit.vue'
import QuestionDetail from '../views/QuestionDetail.vue'
import QuestionManager from '../components/QuestionsManager.vue'
import QuestionDisplay from '../components/QuestionDisplay.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: "/start-new-quiz-page",
      name: "NewQuizPage",
      component: NewQuizPage
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminPage
    },
    {
      path: '/createdQuestion',
      name: 'CreatedQuestion',
      component: CreatedQuestion
    },
    {
      path: '/scorePage',
      name: 'ScorePage',
      component: ScorePage
    },
    {
      path: '/questionPage',
      name: 'QuestionPage',
      component: QuestionPage
    },
    {
      path: '/questionList',
      name: 'QuestionList',
      component: QuestionList
    },
    {
      path: '/questionEdit',
      name: 'QuestionEdit',
      component: QuestionEdit
    },
    {
      path: '/questionDetail',
      name: 'QuestionDetail',
      component: QuestionDetail
    },
    {
      path: '/questionsManager',
      name: 'QuestionsManager',
      component: QuestionManager
    },
    {
      path: '/questionDisplay',
      name: 'QuestionDisplay',
      component: QuestionDisplay
    }

  ]
})

export default router
