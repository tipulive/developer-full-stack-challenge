<template>
  <div class="authors-form">
    <b-form @submit.prevent="save">
      <b-form-group label="Name" label-for="author-name">
        <b-form-input id="author-name" v-model="authorData.name" required></b-form-input>
      </b-form-group>

      <b-form-group label="Books" label-for="author-books">
        <b-form-input id="author-books" v-model="authorData.books" required></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Save</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  props: {
    author: {
      type: Object,
      default: () => ({ name: '', books: [] })
    }
  },
  data() {
    return {
      authorData: { ...this.author }
    };
  },
  methods: {
    save() {
      this.$emit('save', this.authorData);
    }
  }
};
</script>

<style scoped>
.authors-form {
  padding: 20px;
}
</style>
