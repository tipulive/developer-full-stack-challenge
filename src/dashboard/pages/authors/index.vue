<template>
  <div>


 <AuthorsTable :authors="myArray"/>

  </div>
</template>

<script>
import AuthorsTable from '@/components/Authors/AuthorsTable.vue';

export default {
middleware: 'auth',
  components: {
    AuthorsTable
  },
 computed: {
    counter() {
      return this.$store.state.counter;
    },
    authorData(){
        return this.$store.state.author.authorData;
    }
  },
  data() {
    return {
      myArray: [
        { name: "Item 1",books:"test"},


      ]
    };
  },

  methods: {
    handleLogin(credentials) {
      // Implement the login logic here
      console.log('Login:', credentials);

    },

  }
};
</script>

<style scoped>
/* Add your custom styling for the login page here */
</style>
