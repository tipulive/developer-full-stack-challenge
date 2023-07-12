get authors and paginate
<template>
  <div class="p-4">


<b-container >
 <b-form-group >
      <b-form-input v-model="searchQuery"  placeholder="Search by name" @input="searchBooks" />
    </b-form-group>
    <div class="text-right mb-3">
    <b-button size="sm" variant="primary" @click="addBook()">
          Add New
        </b-button>
  </div>

 <b-table striped hover :items="books" :fields="tableFields" @row-clicked="viewBook">

    <template v-slot:cell(actions)="data">
        <b-button size="sm" variant="primary"  @click="viewBook(data.item)">
          Edit
        </b-button>
        <b-button size="sm" variant="danger" @click="deleteBook(data.item)">
          Delete
        </b-button>
      </template>
 </b-table>

 <div class="text-center">
  <button @click="previousPage" :disabled="page === 1">Previous</button>
      <button @click="nextPage" :disabled="books.length < limit">Next</button>
 </div>

</b-container>

<BooksAddModal />
<BooksEditModal :myBookData="propAuthor"/>

  </div>
</template>

<script>
import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';

Vue.use(BootstrapVue);

import BooksAddModal from '@/components/Books/BooksAddModal.vue';
import BooksEditModal from '@/components/Books/BooksEditModal.vue';
export default {
    components: {

    BooksAddModal,
    BooksEditModal
  },
  data() {
    return {
        showSearch:false,
      //books: [],
      propAuthor: {},

      OpenModal:false,
      authName:"",
      searchQuery:"",
      page: 1,
      limit: 10,
      dataToSend: 'Initial Value',

      tableFields:[

       { key: 'name', label: 'Name' },
       { key: 'pages', label: 'pages' },
       { key: 'author_name', label: 'Author Name' },
       "actions"

      ],
        sortBy: 'name',
      sortDesc: false
    };
  },
  mounted() {
    this.fetchBooks();
  },
  computed: {
    books() {
      return this.$store.state.book.bookData;
    }
  },
  methods: {
    async fetchBooks() {

const payload = {
        page:this.page,
        limit:this.limit,
        search:this.searchQuery,
        sort:'asc',
      };

await this.$store.dispatch('book/fetchBooks',payload)







    },
    searchBooks() {
        this.OpenModal=false;
      this.page = 1;
      this.fetchBooks();
    },
    previousPage() {
      this.page--;
      this.fetchBooks();
    },
    nextPage() {
      this.page++;
      this.fetchBooks();
    },
     addBook() {

        this.$bvModal.show('addBook-modal');



      // Handle the logic to open the modal for editing the author
    },

     async viewBook(books) {
        //console.log(books)
        this.$bvModal.show('editBook-modal');


         this.propAuthor=books;
         const payload = {
        id:books.id,
        author_id:books.author_id,
        author_name:books.author_name,
        name:books.name,

        pages:books.pages

      };
          await this.$store.dispatch('book/updateBookPass',payload)

       console.log(this.$store.state.book.BookPass)

    },
    deleteBook(author) {
console.log(author.id)
this.$axios.delete(`/books/${author.id}`, {


      })
        .then((response) => {
this.fetchBooks();

          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });

    }
  }
};
</script>

