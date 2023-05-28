<template>
  <div class="admin-page">
    <h1>Espace Admin</h1>
    <form @submit.prevent="submitPassword">
      <div>
        <input type="password" v-model="password" placeholder="Mot de passe" />
        <button type="button" class="btn btn-primary" @click="checkPassword">Connexion</button>
        <p v-if="showErrorMessage" class="error-message">Mauvais mot de passe</p>
      </div>
    </form>

  </div>
</template>

<script>
export default {
  data() {
    return {
      password: '',
      showErrorMessage: false,
    };
  },
  methods: {
    checkPassword() {
      if (this.password === 'flask2023') {
        this.$router.push('/QuestionList');
      } else {
        this.showErrorMessage = true;
      }
    },
  },
};
</script>

<style>
.error-message {
  color: red;
}

.admin-page {
  max-width: 60px;
  margin-left: -90px;
  color: yellow;
}

.admin-page h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.admin-page form {
  margin-top: 20px;
}

.admin-page .error-message {
  color: red;
}

.admin-page {
  max-width: 400px;
  text-align: center;
}

.success-message {
  color: green;
  margin-top: 20px;
}

.error-message {
  color: red;
  margin-top: 20px;
}

.admin-page button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.admin-page button:hover {
  background-color: #0056b3;
}
</style>


