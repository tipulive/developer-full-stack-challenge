<template>
  <div>
    <b-button variant="outline-light" @click="logout">Logout</b-button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      // Perform the logout action
      // Clear the JWT token from localStorage or any other storage mechanism
      localStorage.removeItem('jwtToken');
      // Redirect to the login page or any other desired page
      this.$router.push({ name: 'login' });
    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the LogoutButton component here */
</style>
