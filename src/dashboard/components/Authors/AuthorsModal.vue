<template>
  <div>

    <b-modal
    size="lg"
      id="authors-modal"
      title="Manage Author"
      hide-footer

    >
      <b-form-group label="Name" label-for="author-name">
        <b-form-input id="author-name"  required></b-form-input>
      </b-form-group>


      <b-form-group label="Books">
        <BooksTable/>

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

  data() {
    return {

     bookFields: [
        { key: 'name', label: 'Book Name' },
        { key: 'pages', label: 'Number of Pages' },
     ],



    };
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
    cancel() {
        console.log(this.author.books[0].author_name)
      // Handle the logic to cancel the changes and close the modal
    },
    save() {
      // Handle the logic to save the changes and close the modal
    }
  }
};
</script>

<style scoped>

/* Add your custom styling for the AuthorsModal component here */
</style>
