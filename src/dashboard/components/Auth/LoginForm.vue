<template>
  <div>
   <b-form   @submit.prevent="submitForm">
<b-form-group label="Username" label-for="username">
        <b-form-input id="username" v-model="formData.username" required></b-form-input>
      </b-form-group>
      <b-form-group label="Password" label-for="password">
        <b-form-input id="password" type="password" v-model="formData.password" required></b-form-input>
      </b-form-group>

<div class="form-group">
<button class="btn btn-primary">Login</button>
</div>
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
    async submitForm() {
      this.loading = true;
      this.error = null;
      const payload =this.formData;
await this.$store.dispatch('user/LoginUser',payload)

//console.log(await this.$store.dispatch('user/LoginUser',payload))

localStorage.setItem(process.env.TOKEN_KEY,this.$store.state.user.UserData.access_token);
const payloadData=true;
this.$store.commit('user/update_login',payloadData);
this.$router.push('/authors');


    }
  }
};
</script>

<style scoped>
/* Add your custom styling for the LoginForm component here */
</style>
