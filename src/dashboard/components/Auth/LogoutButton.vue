<template>
  <div>
    <b-button variant="outline-light" @click="logout">Logout</b-button>
  </div>
</template>

<script>
export default {
  methods: {
    async logout() {
      // Perform the logout action

            const payloadData ="logout";
await this.$store.dispatch('user/Logout',payloadData)
      const payload=false;
    this.$store.commit('user/update_login', payload);//hide some link


      // Redirect to the login page or any other desired page
      this.$router.push({ name:'login' });
    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the LogoutButton component here */
</style>
