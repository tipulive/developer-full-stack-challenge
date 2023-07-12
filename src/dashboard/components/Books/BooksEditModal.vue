<template>

  <b-modal id="editBook-modal" hide-footer title="Edit Book">

    <b-form   @submit.prevent="submit">

    <b-form-group label="Name">
        <b-form-input :value="BookPass.name"  id="BookName" ref="myInput"></b-form-input>
      </b-form-group>
          <b-form-group label="Author Name">
        <BooksAuthorSelect :valueData="myBookData" ref="childComponent"/>
      </b-form-group>
      <b-form-group label="pages">
        <b-form-input type="number" :value="BookPass.pages" id="BookPage"></b-form-input>
      </b-form-group>
<div class="form-group">
<button class="btn btn-primary">Submit</button>
</div>
    </b-form>
  </b-modal>
</template>
<script>
import  BooksAuthorSelect from '@/components/Books/BooksAuthorSelect.vue';
export default {
    components: {
    BooksAuthorSelect
  },
 props: {

    myBookData: {
      type: Object,
      required: true
    },
  },

   data() {

    return {
      name: "MyModal",
      BookDetail:{},

    };
  },
   computed: {
    BookPass() {

      return this.$store.state.book.BookPass;
    }
  },

  methods: {
    closeModal() {
      this.$bvModal.hide("editBook-modal");
    },

    async submit(){

  const BookName = document.querySelector('#BookName').value;
  const BookPage = document.querySelector('#BookPage').value;




 const payload = {
        id:this.BookPass.id,
        name:BookName,
        author_id:this.$refs.childComponent.value.id,
        pages:BookPage,
      };

await this.$store.dispatch('book/editBook',payload)



this.$bvModal.hide("editBook-modal");

      },
  },

};
</script>
<style scoped>
footer#my-modal___BV_modal_footer_ {
    display: none !important;
}
</style>
