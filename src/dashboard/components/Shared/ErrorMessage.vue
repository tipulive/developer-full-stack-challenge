<template>
  <div class="error-message">
    <b-alert variant="danger" show dismissible @dismissed="clearError">{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true
    }
  },
  methods: {
    clearError() {
      // Emit an event or perform any necessary action to clear the error message
    }
  }
};
</script>

<style scoped>
.error-message {
  margin-bottom: 20px;
}
</style>
