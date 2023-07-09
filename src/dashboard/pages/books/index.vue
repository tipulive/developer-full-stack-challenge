<template>
  <div>
    <h1>Login</h1>
    <AuthorsTable :authors="myArray"/>
  </div>
</template>

<script>
import AuthorsTable from '@/components/Books/BooksTable.vue';

export default {
    middleware: 'auth',
  components: {
    AuthorsTable
  },
  data() {
    return {
      myArray: [
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},
        { name: "Item 10",books:"test"},
        { name: "Item 11",books:"test"},
        { name: "Item 12",books:"test"},
        { name: "Item 13",books:"test"},
        { name: "Item 14",books:"test"},
        { name: "Item 10",books:"test"},
        { name: "Item 10",books:"test"},
        { name: "Item 10",books:"test"},
        { name: "Item 10",books:"test"},

      ]
    };
  },
  methods: {
    handleLogin(credentials) {
      // Implement the login logic here
      console.log('Login:', credentials);
      // Perform any necessary actions for authentication
      // For example, make an API request to authenticate the user
      // Once the user is authenticated, you can navigate to the appropriate page
    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the login page here */
</style>

