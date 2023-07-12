<template>
  <div>
<b-container>
    <LoginForm  />
     </b-container>
  </div>
</template>

<script>
import LoginForm from '@/components/Auth/LoginForm.vue';

export default {
  components: {
    LoginForm
  },

};
</script>

<style scoped>
/* Add your custom styling for the login page here */
</style>
