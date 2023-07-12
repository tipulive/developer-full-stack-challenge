<template>
  <div>

    <b-modal
      id="authorEdit-modal"
      title="Edit Author"
      size="lg"
      hide-footer

    >
    <b-form   @submit.prevent="submit">
      <b-form-group label="Name" label-for="author-name">
        <b-form-input id="author-name" :value="AuthorPass.name" required></b-form-input>
      </b-form-group>
      <div class="form-group">
<button class="btn btn-primary">Save</button>
</div>
  </b-form>

      <b-form-group label="Books">
        <BooksTable  />

      </b-form-group>

    </b-modal>


  </div>
</template>

<script>

import BooksTable from '@/components/Books/BooksTable.vue';


export default {
  components: {

    BooksTable
  },
  props: {

  },

  data() {
    return {
author:{},




    };
  },
 computed: {
    AuthorPass() {

      return this.$store.state.author.AuthorPass;
    }
  },
  methods: {
    modalShown() {
      // Handle any logic when the modal is shown
       this.$emit('update:modalOpen', true);
    },
    modalHidden() {
        this.$emit('update:modalOpen', false);
        //this.modalOpen=false;
      // Handle any logic when the modal is hidden
    },
    async submit(){
console.log(this.$store.state.author.AuthorPass)
const AuthorName = document.querySelector('#author-name').value;
         const payload = {
        id:this.AuthorPass.id,
        name:AuthorName,

      };
await this.$store.dispatch('author/editAuthor',payload)

  this.$bvModal.hide('authorEdit-modal');
      },
  }
};
</script>

<style scoped>

/* Add your custom styling for the AuthorsModal component here */
</style>
