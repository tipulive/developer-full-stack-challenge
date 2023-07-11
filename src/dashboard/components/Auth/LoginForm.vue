<template>
  <div>
    <b-form @submit="submitForm">
      <b-form-group label="Username" label-for="username">
        <b-form-input id="username" v-model="formData.username" required></b-form-input>
      </b-form-group>
      <b-form-group label="Password" label-for="password">
        <b-form-input id="password" type="password" v-model="formData.password" required></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
    <shared-loading-spinner v-if="loading"></shared-loading-spinner>
    <shared-error-message v-if="error" :message="error"></shared-error-message>
  </div>
</template>

<script>
import LoadingSpinner from '@/components/Shared/LoadingSpinner.vue';
import ErrorMessage from '@/components/Shared/ErrorMessage.vue';

export default {
  components: {
    'shared-loading-spinner': LoadingSpinner,
    'shared-error-message': ErrorMessage
  },
  data() {
    return {
      formData: {
        username: '',
        password: ''
      },
      loading: false,
      error: null
    };
  },
  methods: {
    submitForm() {
      this.loading = true;
      this.error = null;

      // Perform the login action
      // Send the formData.username and formData.password to the backend to authenticate the user
      // Handle the JWT token received from the backend and store it in localStorage or any other storage mechanism
      // Handle any errors that occur during the login process

      // Simulating a delay to demonstrate the loading spinner
      setTimeout(() => {
        // Replace the code within this setTimeout with the actual login logic
        const loginSuccessful = true; // Replace with the actual login response from the backend

        if (loginSuccessful) {
          const jwtToken = '...'; // Replace with the actual JWT token received from the backend
          localStorage.setItem('jwtToken', jwtToken);
          // Redirect to the desired page after successful login
          this.$router.push({ name: 'dashboard' });
        } else {
          this.error = 'Invalid username or password. Please try again.';
        }

        this.loading = false;
      }, 1500);
    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the LoginForm component here */
</style>
