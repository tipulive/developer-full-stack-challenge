<template>

  <b-modal id="addBook-modal" hide-footer  title="Add Book">
    <b-form   @submit.prevent="submit">
    <b-form-group label="Name">
        <b-form-input v-model="book.name" required></b-form-input>
      <b-form-group label="Author Name">
        <BooksAuthorSelect :valueData="bookDatas" ref="childComponent"/>
      </b-form-group>
      </b-form-group>
      <b-form-group label="pages">
        <b-form-input type="number" v-model="book.pages" required></b-form-input>
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
    BooksAuthorSelect,

  },
   props: {


  },
   data() {
    return {
      name: "MyModal",
      book:{},
      bookDatas:{
        "add":true
      },
    };
  },
  methods: {
    closeModal() {
      this.$bvModal.hide("addBook-modal");
    },

    async submit(){
        const payload = {
        name:this.book.name,
        author_id:this.$refs.childComponent.value.id,
        pages:this.book.pages,
      };

await this.$store.dispatch('book/addBooks',payload)
   const payloadData = {
                    page:1,
                    limit:10,
                    search:"",
                    sort:"desc"
                  };

            await this.$store.dispatch('book/fetchBooks',payloadData)
this.$bvModal.hide("addBook-modal");


      },
  },
};
</script>
<style scoped>
footer#my-modal___BV_modal_footer_ {
    display: none !important;
}
</style>
