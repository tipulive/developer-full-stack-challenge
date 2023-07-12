<template>
  <div class="authors-search">
    <b-form-group label="Search Authors">
      <b-input-group>
        <b-form-input
          v-model="searchQuery"
          placeholder="Enter author name"
          @input="handleSearch"
        ></b-form-input>
        <b-input-group-append>
          <b-button variant="outline-secondary" @click="clearSearch">Clear</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: ''
    };
  },
  methods: {
    handleSearch() {
      // Emit the search query to the parent component or page
      this.$emit('search', this.searchQuery);
    },
    clearSearch() {
      // Clear the search query and emit an empty query to the parent component or page
      this.searchQuery = '';
      this.$emit('search', '');
    }
  }
};
</script>

<style scoped>
.authors-search {
  margin-bottom: 20px;
}
/* Add your custom styling for the AuthorsSearchInput component here */
</style>
