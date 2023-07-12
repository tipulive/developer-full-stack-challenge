<template>
  <div>

    <b-modal
      id="authorAdd-modal"
      title="Add Author"
      size="lg"
      hide-footer
    > <b-form   @submit.prevent="submit">
      <b-form-group label="Name" label-for="author-name">
        <b-form-input id="author-name" v-model="author.name"  required></b-form-input>
      </b-form-group>
<div class="form-group">
<button class="btn btn-primary">Submit</button>
</div>
</b-form>
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
    props: {


  },

  data() {
    return {
author:{},
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
     async submit(){

         const payload = {
       name:this.author.name,
      };

await this.$store.dispatch('author/addAuthors',payload)
   const payloadData = {
                    page:1,
                    limit:10,
                    search:"",
                    sort:"desc"
                  };

this.$bvModal.hide('authorAdd-modal');
           // await this.$store.dispatch('author/fetchAuthors',payloadData)




      },

  }
};
</script>

<style scoped>

/* Add your custom styling for the AuthorsModal component here */
</style>
