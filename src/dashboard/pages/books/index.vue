<template>
  <div>

    <BooksTable :authors="myArray"/>
  </div>
</template>

<script>
import BooksTable from '@/components/Books/BooksTable.vue';

export default {
middleware: 'auth',
  components: {
    BooksTable
  },
  data() {
    return {
      myArray: [
        { name: "Item 1",books:"test"},
        { name: "Item 1",books:"test"},


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

