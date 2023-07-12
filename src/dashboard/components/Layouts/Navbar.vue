<template>
  <div>
    <b-navbar type="dark" variant="dark" toggleable="lg">
      <b-container fluid>
        <b-navbar-brand href="#">Logo</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <template v-if="isLoggedIn">
            <b-nav-item>
            <router-link to="/authors">Authors</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link to="/books">Books</router-link>
          </b-nav-item>
          <auth-logout-button @logout="logout"></auth-logout-button>
            </template>
            <template v-else>
             <b-nav-item :to="{ name: 'login' }">Login</b-nav-item>
            </template>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
import AuthLogoutButton from '@/components/Auth/LogoutButton.vue';

export default {
  components: {
    AuthLogoutButton
  },
  data() {
    return {
      //isLoggedIn: false // Set this to true when the user is logged in
    };
  },
computed: {
  isLoggedIn() {
    return this.$store.state.user.isLoggedIn;
  }
},
  methods: {
    logout() {
      // Handle the logout action
      console.log('User logged out');
      // Implement any necessary actions for logging out
      // For example, clear user authentication tokens, redirect to login page, etc.
      this.isLoggedIn = false; // Update the logged-in state
    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the Navbar component here */
.navbar-custom {
  /* Add your custom styles for the navbar here */
}
</style>
